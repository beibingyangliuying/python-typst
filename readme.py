import pyperclip

from typstpy import std, subpar  # noqa: F401
from typstpy._core import _Implement


def main() -> None:
    """Copy generated README support sections to the clipboard."""
    content = '\n'.join([_Implement.implement_table(), _Implement.code_examples()])
    pyperclip.copy(content)


if __name__ == '__main__':
    main()
