from collections import deque
from io import StringIO
from typing import final

from attrs import field, frozen

from .typings import Block


@final
@frozen
class Document:
    _blocks: deque[Block] = field(factory=deque, converter=deque)
    _imports: deque[Block] = field(factory=deque, converter=deque)
    _set_rules: deque[Block] = field(factory=deque, converter=deque)
    _show_rules: deque[Block] = field(factory=deque, converter=deque)

    def add_block(self, block: Block, /) -> None:
        """Add a block to the document.

        Args:
            block (Block): The block to be added.
        """
        self._blocks.append(block)

    def add_import(self, block: Block) -> None:
        """Import names to the document.

        Args:
            block (Block): The block to be imported. Use `std.import_` to generate standard code.

        See also:
            `std.import_`
        """
        self._imports.append(block)

    def add_set_rule(self, block: Block) -> None:
        """Add a set rule to the document.

        Args:
            block (Block): The block to be added. Use `std.set_` to generate standard code.

        See also:
            `std.set_`
        """
        self._set_rules.append(block)

    def add_show_rule(self, block: Block) -> None:
        """Add a show rule to the document.

        Args:
            block (Block): The block to be added. Use `std.show_` to generate standard code.

        See also:
            `std.show_`
        """
        self._show_rules.append(block)

    def save(self, path: str, /) -> None:
        """Save the document to a file.

        Args:
            path (str): The path of the file to be saved.
        """
        with open(path, 'w') as f:
            f.write(str(self))

    def __str__(self) -> str:
        """Incorporate imports, set rules, show rules and blocks into a single string.

        Returns:
            str: The content of the document.
        """
        with StringIO() as stream:
            if self._imports:
                stream.write('\n'.join(self._imports))
                stream.write('\n\n')
            if self._set_rules:
                stream.write('\n'.join(self._set_rules))
                stream.write('\n\n')
            if self._show_rules:
                stream.write('\n'.join(self._show_rules))
                stream.write('\n\n')
            stream.write('\n\n'.join(self._blocks))
            return stream.getvalue()


__all__ = ['Document']
