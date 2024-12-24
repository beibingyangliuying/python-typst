from typing import Callable, Optional

from attrs import field, frozen
from pymonad.reader import Pipe  # type:ignore

from ..typings import TypstFunc
from cytoolz.curried import map  # type:ignore


def attach_func(
    func: TypstFunc, name: Optional[str] = None, /
) -> Callable[[Callable], Callable]:
    """Attach a typst function to another function.

    Args:
        func (TypstFunc): The function to attach.
        name (Optional[str], optional): The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        Callable[[Callable], Callable]: The decorator function.
    """

    def wrapper(_func: Callable) -> Callable:
        _name = name if name else _func.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}.')
        setattr(_func, _name, func)
        return _func

    return wrapper


@frozen
class _Implement:
    is_standard: bool
    name: str
    original_name: str | None = field(default=None)
    hyperlink: str | None = field(default=None)

    @original_name.validator
    def _check_original_name(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError(f'Only standard functions can have {attribute.name}.')
        elif self.is_standard and not value:
            raise ValueError(f'Standard functions must have {attribute.name}.')

    @hyperlink.validator
    def _check_hyperlink(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError(f'Only standard functions can have {attribute.name}.')
        elif self.is_standard and not value:
            raise ValueError(f'Standard functions must have {attribute.name}.')

    def __str__(self) -> str:
        return (
            '| '
            + ' | '.join(
                Pipe([self.is_standard, self.name])
                .map(
                    lambda x: x
                    + [
                        self.original_name,
                        f'[{self.original_name}]({self.hyperlink})',
                    ]
                    if self.is_standard
                    else x + ['', '']
                )
                .map(map(str))
                .flush()
            )
            + ' |'
        )


def implement(
    is_standard: bool,
    /,
    *,
    original_name: Optional[str] = None,
    hyperlink: Optional[str] = None,
) -> Callable[[Callable], Callable]:
    """Set `_implement` attribute of a function. The attribute type is `_Implement`.

    Args:
        is_standard (bool): Whether the function is standard implemented.
        original_name (Optional[str], optional): The original function name in typst. Defaults to None.
        hyperlink (Optional[str], optional): The hyperlink of the documentation in typst. Defaults to None.

    Returns:
        Callable[[Callable], Callable]: The decorator function.
    """

    def wrapper(_func: Callable) -> Callable:
        setattr(
            _func,
            '_implement',
            _Implement(is_standard, _func.__name__, original_name, hyperlink),
        )
        return _func

    return wrapper
