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

GENERATED_START = '<!-- typstpy-generated-start -->'
GENERATED_END = '<!-- typstpy-generated-end -->'


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


def build_content(section: str, *, markers: bool = False) -> str:
    """Build generated README support content."""
    ensure_registry_loaded()
    parts = []
    if section in {'all', 'table'}:
        if markers:
            parts.append('## Current Supports')
        parts.append(render_implement_table(collect_implement_records()))
    if section in {'all', 'examples'}:
        if markers:
            parts.append('## Examples')
        parts.append(render_code_examples(collect_example_blocks()))
    content = '\n'.join(parts)
    if markers:
        return f'{GENERATED_START}\n\n{content.rstrip()}\n\n{GENERATED_END}\n'
    return content


def replace_generated_section(readme: str, generated: str) -> str:
    """Replace the generated README section, adding markers if needed."""
    generated = generated.rstrip() + '\n'
    start = readme.find(GENERATED_START)
    end = readme.find(GENERATED_END)
    if start != -1 and end != -1:
        end += len(GENERATED_END)
        return readme[:start] + generated + readme[end:].lstrip('\n')

    heading = readme.find('## Current Supports')
    if heading == -1:
        raise ValueError('README generated section not found')
    return readme[:heading] + generated


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
    parser.add_argument(
        '--markers',
        action='store_true',
        help='Wrap generated content in README marker comments.',
    )
    parser.add_argument(
        '--write-readme',
        type=Path,
        help='Replace the generated section in the given README file.',
    )
    args = parser.parse_args(argv)

    if args.write_readme is not None and args.section != 'all':
        parser.error('--write-readme requires --section all')

    content = build_content(
        args.section, markers=args.markers or args.write_readme is not None
    )
    if args.clipboard:
        import pyperclip

        pyperclip.copy(content)
    elif args.write_readme is not None:
        readme = args.write_readme.read_text(encoding='utf-8')
        args.write_readme.write_text(
            replace_generated_section(readme, content),
            encoding='utf-8',
        )
    else:
        sys.stdout.write(content)
        if content and not content.endswith('\n'):
            sys.stdout.write('\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
