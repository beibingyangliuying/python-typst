from __future__ import annotations

import argparse
import sys
from io import StringIO
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from typstpy._docs import (  # noqa: E402
    ExampleBlock,
    ImplementRecord,
    collect_example_blocks,
    collect_implement_records,
    ensure_registry_loaded,
)


def render_implement_table(records: list[ImplementRecord]) -> str:
    """Render implementation metadata as a README Markdown table."""
    with StringIO() as stream:
        print(
            "| Package's function name | Typst's function name | Documentation on typst | Version |",
            '| --- | --- | --- | --- |',
            sep='\n',
            file=stream,
        )
        for record in records:
            print(
                f'| {record.qualname} | {record.original_name} | '
                f'[{record.hyperlink}]({record.hyperlink}) | {record.version} |',
                file=stream,
            )
        return stream.getvalue()


def render_code_examples(blocks: list[ExampleBlock]) -> str:
    """Render extracted Examples sections as README Markdown code blocks."""
    with StringIO() as stream:
        for block in blocks:
            print(
                f'`{block.qualname}`:',
                '\n```python',
                block.source,
                '```\n',
                sep='\n',
                file=stream,
            )
        return stream.getvalue()


def build_content(section: str) -> str:
    """Build generated README support content."""
    ensure_registry_loaded()
    parts = []
    if section in {'all', 'table'}:
        parts.append(render_implement_table(collect_implement_records()))
    if section in {'all', 'examples'}:
        parts.append(render_code_examples(collect_example_blocks()))
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
