from typing import Any, Optional

from .._utils import attach_func, implement, instance, positional
from ..typings import Block


@implement(
    True,
    original_name='arguments.at',
    hyperlink='https://typst.app/docs/reference/foundations/arguments/#definitions-at',
)
def _arguments_at(self: Block, key: str | int, /, *, default: Optional[Any]) -> Block:
    return instance(_arguments_at, self, key, default=default)


@implement(
    True,
    original_name='arguments.pos',
    hyperlink='https://typst.app/docs/reference/foundations/arguments/#definitions-pos',
)
def _arguments_pos(self: Block, /) -> Block:
    return instance(_arguments_pos, self)


@implement(
    True,
    original_name='arguments.named',
    hyperlink='https://typst.app/docs/reference/foundations/arguments/#definitions-named',
)
def _arguments_named(self: Block, /) -> Block:
    return instance(_arguments_named, self)


@attach_func(_arguments_at, 'at')
@attach_func(_arguments_pos, 'pos')
@attach_func(_arguments_named, 'named')
@implement(
    True,
    original_name='arguments',
    hyperlink='https://typst.app/docs/reference/foundations/arguments/',
)
def arguments(*args: Any) -> Block:
    return positional(arguments, *args)
