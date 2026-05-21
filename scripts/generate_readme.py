from __future__ import annotations

import argparse
import sys

try:
    from ._example_collect import ensure_registry_loaded
except ImportError:  # pragma: no cover - supports direct script execution.
    from _example_collect import ensure_registry_loaded

from typstpy._core import _Implement


def build_content(section: str) -> str:
    """Build generated README support content."""
    ensure_registry_loaded()
    parts = []
    if section in {'all', 'table'}:
        parts.append(_Implement.implement_table())
    if section in {'all', 'examples'}:
        parts.append(_Implement.code_examples())
    return '\n'.join(parts)


def main(argv: list[str] | None = None) -> int:
    """Generate README support sections."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--section',
        choices=['all', 'table', 'examples'],
        default='all',
        help='README section to generate. Defaults to all.',
    )
    parser.add_argument(
        '--clipboard',
        action='store_true',
        help='Copy generated content to the clipboard instead of stdout only.',
    )
    args = parser.parse_args(argv)

    content = build_content(args.section)
    if args.clipboard:
        import pyperclip

        pyperclip.copy(content)
    else:
        sys.stdout.write(content)
        if content and not content.endswith('\n'):
            sys.stdout.write('\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
