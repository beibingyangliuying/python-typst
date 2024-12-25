from collections import deque
from typing import final

from attrs import field, frozen
from .typings import Block


@final
@frozen
class Document:
    _blocks: deque[str] = field(factory=deque, converter=deque)
    _set_rules: deque[str] = field(factory=deque, converter=deque)
    _show_rules: deque[str] = field(factory=deque, converter=deque)

    def add_block(self, block: Block, /) -> None:
        self._blocks.append(block)

    def save(self, path: str) -> None:
        with open(path, 'w') as f:
            f.write(str(self))

    def __str__(self) -> str:
        return '\n\n'.join(self._blocks)
