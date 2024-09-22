from attrs import field, frozen

from utils import FormatType, format


@frozen
class Content:
    content: str = field()

    def __str__(self) -> str:
        return f"[{self.content}]"


@frozen
class Label:
    label: str = field()

    def __str__(self) -> str:
        return f"<{self.label}>"


@frozen
class Length:
    value: float = field(repr=format(FormatType.FLOAT))
    unit: str = field()

    @unit.validator
    def _check_unit(self, attribute, value):
        if value not in ("pt", "mm", "cm", "em"):
            raise ValueError(f"Invalid unit: {value}.")

    def __str__(self) -> str:
        return f"{format(FormatType.FLOAT)(self.value)}{self.unit}"


@frozen
class Relative:
    value: float = field(repr=format(FormatType.FLOAT))

    def __str__(self) -> str:
        return f"{format(FormatType.FLOAT)(self.value)}%"
