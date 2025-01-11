from collections import deque
from io import StringIO
from typing import final

from attrs import field, frozen
from deprecated.sphinx import deprecated  # type: ignore

from .typings import Content


@final
@frozen
class Document:
    _contents: deque[Content] = field(factory=deque, init=False)
    _import_statements: deque[Content] = field(factory=deque, init=False)
    _set_rules: deque[Content] = field(factory=deque, init=False)
    _show_rules: deque[Content] = field(factory=deque, init=False)

    @deprecated(
        version='1.0.2',
        reason='The method will be removed since version 1.1.x. Use `add_content` instead.',
    )
    def add_block(self, block: Content, /) -> None:
        """Add a block to the document.

        Args:
            block (Content): The block to be added.
        """
        self._contents.append(block)

    def add_content(self, content: Content, /) -> None:
        """Add a content to the document.

        Args:
            content (Content): The content to be added.
        """
        self._contents.append(content)

    def add_import(self, statement: Content, /) -> None:
        """Import names to the document.

        Args:
            statement (Content): The import statement. Use `std.import_` to generate standard code.

        See also:
            `std.import_`
        """
        self._import_statements.append(statement)

    def add_set_rule(self, set_rule: Content, /) -> None:
        """Add a set rule to the document.

        Args:
            set_rule (Content): The set rule to be added. Use `std.set_` to generate standard code.

        See also:
            `std.set_`
        """
        self._set_rules.append(set_rule)

    def add_show_rule(self, show_rule: Content, /) -> None:
        """Add a show rule to the document.

        Args:
            show_rule (Content): The show rule to be added. Use `std.show_` to generate standard code.

        See also:
            `std.show_`
        """
        self._show_rules.append(show_rule)

    @deprecated(
        version='1.0.3',
        reason='The method will be removed since version 1.1.x. Use `print` in standard library instead.',
    )
    def save(self, path: str, /) -> None:
        """Save the document to a file.

        Args:
            path (str): The path of the file to be saved.
        """
        with open(path, 'w') as f:
            f.write(str(self))

    def __str__(self) -> str:
        """Incorporate import statements, set rules, show rules and contents into a single string.

        Returns:
            str: The content of the document.
        """
        with StringIO() as stream:
            if self._import_statements:
                stream.write('\n'.join(self._import_statements))
                stream.write('\n\n')
            if self._set_rules:
                stream.write('\n'.join(self._set_rules))
                stream.write('\n\n')
            if self._show_rules:
                stream.write('\n'.join(self._show_rules))
                stream.write('\n\n')
            stream.write('\n\n'.join(self._contents))
            return stream.getvalue()


__all__ = ['Document']
