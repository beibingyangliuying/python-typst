"""Classes in this module should only be used as parameter types in the `functions` module."""

from typing import TypeAlias

from attrs import field, frozen

from .utils import FormatType, format

Block: TypeAlias = str
"""Executable typst block."""


@frozen
class Content:
    content: Block = field()

    @content.validator
    def _check_content(self, attribute, value):
        # todo: Check if the content is executable typst block.
        pass

    def _can_simplify(self) -> bool:
        return self.content.startswith("#")

    @staticmethod
    def examine_sharp(content: Block) -> str:
        return content.lstrip("#")

    def __str__(self) -> str:
        if self._can_simplify():
            return Content.examine_sharp(self.content)
        return f"[{self.content}]"


@frozen
class Label:
    label: str = field()

    @label.validator
    def _check_label(self, attribute, value):
        # todo: Check for illegal characters in label.
        pass

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
