"""Function decorators."""

from typing import Callable, Optional

from attrs import field, frozen


def attach_func(func: Callable, name: Optional[str] = None) -> Callable:
    def wrapper(_func: Callable) -> Callable:
        _name = name if name else _func.__name__
        if _name.startswith("_"):
            raise ValueError(f"Invalid name: {_name}.")
        setattr(_func, _name, func)
        return _func

    return wrapper


@frozen
class Implement:
    is_standard: bool = field()
    name: str = field()
    original_name: str | None = field(default=None)
    hyperlink: str | None = field(default=None)

    @original_name.validator
    def _check_original_name(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError("Only standard functions can have an original name.")
        elif self.is_standard and not value:
            raise ValueError("Standard functions must have an original name.")

    @hyperlink.validator
    def _check_hyperlink(self, attribute, value):
        if not self.is_standard and value:
            raise ValueError("Only standard functions can have a hyperlink.")
        elif self.is_standard and not value:
            raise ValueError("Standard functions must have a hyperlink.")

    def to_markdown(self) -> str:
        return rf"| {self.is_standard} | {self.name} | {self.original_name} | [{self.original_name}]({self.hyperlink}) |"


def implement(
    is_standard: bool,
    original_name: Optional[str] = None,
    hyperlink: Optional[str] = None,
) -> Callable:
    def wrapper(_func: Callable) -> Callable:
        setattr(
            _func,
            "_implement",
            Implement(is_standard, _func.__name__, original_name, hyperlink),
        )
        return _func

    return wrapper
