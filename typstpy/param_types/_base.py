from abc import ABC
from enum import Enum
from functools import cached_property
from itertools import starmap
from typing import Union, final

from attrs import field, frozen, validators
from cytoolz.curried import curry, map, memoize  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from ._format import FormatType, format


class _Sign(Enum):
    """The sign of a `ValueUnit`."""

    PLUS = "+"
    MINUS = "-"

    @property
    @memoize
    def inv(self) -> "_Sign":
        match self:
            case _Sign.PLUS:
                return _Sign.MINUS
            case _Sign.MINUS:
                return _Sign.PLUS

    def __str__(self) -> str:
        return str(self.value)


@frozen(slots=False)
class _ValueUnit(ABC):
    """Represent a field with a float value and a unit."""

    value: float = field(repr=format(FormatType.FLOAT))
    unit: str

    @final
    def __pos__(self) -> "_ValueUnit":
        return self

    @final
    def __neg__(self) -> "_ValueUnit":
        return self.__class__(-self.value, self.unit)

    @final
    def __add__(self, other: Union["_ValueUnit", "_ValueUnits"]) -> "_ValueUnits":
        if isinstance(other, _ValueUnit):
            return _ValueUnits((self, other), (_Sign.PLUS, _Sign.PLUS))
        elif isinstance(other, _ValueUnits):
            return _ValueUnits((self,) + other.items, (_Sign.PLUS,) + other.signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'."
            )

    @final
    def __sub__(self, other: Union["_ValueUnit", "_ValueUnits"]) -> "_ValueUnits":
        if isinstance(other, _ValueUnit):
            return _ValueUnits((self, other), (_Sign.PLUS, _Sign.MINUS))
        elif isinstance(other, _ValueUnits):
            return _ValueUnits((self,) + other.items, (_Sign.PLUS,) + other.inv_signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'."
            )

    @final
    def __str__(self) -> str:
        return f"{format(FormatType.FLOAT)(self.value)}{self.unit}"

    @final
    def _with_sign(self, sign: _Sign) -> str:
        """Add a sign to a `ValueUnit` and return it as a string.

        Args:
            sign (Sign): The sign to add.

        Raises:
            ValueError: Invalid sign.

        Returns:
            str: The `ValueUnit` with the sign added.
        """
        match sign:
            case _Sign.PLUS:
                if self.value >= 0:
                    return f"{sign}{self}"
                return f"{self}"
            case _Sign.MINUS:
                if self.value >= 0:
                    return f"{sign}{self}"
                return f"{_Sign.PLUS}{-self}"


@final
@frozen
class _ValueUnits:
    """Represent a series of `ValueUnit`s."""

    items: tuple[_ValueUnit, ...] = field(
        validator=validators.deep_iterable(validators.instance_of(_ValueUnit))
    )
    signs: tuple[_Sign, ...] = field(
        validator=validators.deep_iterable(validators.instance_of(_Sign))
    )

    @cached_property
    def inv_signs(self) -> tuple[_Sign, ...]:
        return Pipe(self.signs).map(map(lambda x: x.inv)).map(tuple).flush()

    def __add__(self, other: Union["_ValueUnit", "_ValueUnits"]) -> "_ValueUnits":
        if isinstance(other, _ValueUnit):
            return _ValueUnits(self.items + (other,), self.signs + (_Sign.PLUS,))
        elif isinstance(other, _ValueUnits):
            return _ValueUnits(self.items + other.items, self.signs + other.signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'."
            )

    def __sub__(self, other: Union["_ValueUnit", "_ValueUnits"]) -> "_ValueUnits":
        if isinstance(other, _ValueUnit):
            return _ValueUnits(self.items + (other,), self.signs + (_Sign.MINUS,))
        elif isinstance(other, _ValueUnits):
            return _ValueUnits(self.items + other.items, self.signs + other.inv_signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for -: '{self.__class__}' and '{type(other)}'."
            )

    def __str__(self) -> str:
        return (
            Pipe(zip(self.items, self.signs))
            .map(curry(starmap)(lambda x, y: _ValueUnit._with_sign(x, y)))
            .map(lambda x: ("".join(x)).lstrip("+"))
            .flush()
        )
