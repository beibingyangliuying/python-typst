from io import StringIO
from typing import final

from attrs import field, frozen


@final
@frozen
class Document:
    _contents = field(factory=list, init=False)
    _import_statements = field(factory=list, init=False)
    _set_rules = field(factory=list, init=False)
    _show_rules = field(factory=list, init=False)

    def add_content(self, content, /):
        """Add a content to the document.

        Args:
            content: The content to be added.
        """
        self._contents.append(content)

    def add_import(self, statement, /):
        """Import names to the document.

        Args:
            statement: The import statement. Use `std.import_` to generate standard code.

        See also:
            `std.import_`
        """
        self._import_statements.append(statement)

    def add_set_rule(self, set_rule, /):
        """Add a set rule to the document.

        Args:
            set_rule: The set rule to be added. Use `std.set_` to generate standard code.

        See also:
            `std.set_`
        """
        self._set_rules.append(set_rule)

    def add_show_rule(self, show_rule, /):
        """Add a show rule to the document.

        Args:
            show_rule: The show rule to be added. Use `std.show_` to generate standard code.

        See also:
            `std.show_`
        """
        self._show_rules.append(show_rule)

    def __str__(self):
        """Incorporate import statements, set rules, show rules and contents into a single string.

        Returns:
            The content of the document.
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
