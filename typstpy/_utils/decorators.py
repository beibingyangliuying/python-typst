"""Function decorators."""

from typing import Callable, Optional

from attrs import field, frozen


def attach_func(func: Callable, name: Optional[str] = None) -> Callable:
    """Attach a function to another function.

    Args:
        func (Callable): The function to be attached.
        name (Optional[str], optional): The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Returns:
        Callable: The decorator function.
    """

    def wrapper(_func: Callable) -> Callable:
        _name = name if name else _func.__name__
        if _name.startswith("_"):
            raise ValueError(f"Invalid name: {_name}.")
        setattr(_func, _name, func)
        return _func

    return wrapper


@frozen
class Implement:
    is_standard: bool
    name: str
    original_name: str | None = field(default=None)
    hyperlink: str | None = field(default=None)

    @original_name.validator
    def _check_original_name(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError(f"Only standard functions can have {attribute.name}.")
        elif self.is_standard and not value:
            raise ValueError(f"Standard functions must have {attribute.name}.")

    @hyperlink.validator
    def _check_hyperlink(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError(f"Only standard functions can have {attribute.name}.")
        elif self.is_standard and not value:
            raise ValueError(f"Standard functions must have {attribute.name}.")

    def to_markdown(self) -> str:
        """Convert to a table's row in markdown format.

        Returns:
            str: The table's row in markdown format.
        """
        return rf"| {self.is_standard} | {self.name} | {self.original_name} | [{self.original_name}]({self.hyperlink}) |"


def implement(
    is_standard: bool,
    original_name: Optional[str] = None,
    hyperlink: Optional[str] = None,
) -> Callable:
    """Set `_implement` attribute to a function. The type of the attribute is `Implement`.

    Args:
        is_standard (bool): Whether the function is standard implemented.
        original_name (Optional[str], optional): The original function name in typst. Defaults to None.
        hyperlink (Optional[str], optional): The hyperlink of the documentation in typst. Defaults to None.

    Returns:
        Callable: The decorator function.
    """

    def wrapper(_func: Callable) -> Callable:
        setattr(
            _func,
            "_implement",
            Implement(is_standard, _func.__name__, original_name, hyperlink),
        )
        return _func

    return wrapper
