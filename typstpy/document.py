from collections import deque
from typing import final

from attrs import field, frozen

from .param_types import Block


@final
@frozen
class Document:
    _blocks: deque[Block] = field(factory=deque, init=False, repr=False)

    def add_block(self, block: Block) -> None:
        self._blocks.append(block)

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(str(self))

    def __str__(self) -> Block:
        return "\n\n".join(self._blocks)
