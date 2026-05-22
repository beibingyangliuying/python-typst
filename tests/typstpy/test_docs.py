from __future__ import annotations

from pathlib import Path

from scripts.generate_readme import (
    GENERATED_END,
    GENERATED_START,
    build_content,
    render_code_examples,
    render_implement_table,
    replace_generated_section,
)
from typstpy._docs import ExampleBlock, ImplementRecord, extract_examples


def test_extract_examples_stops_at_next_top_level_section() -> None:
    def sample() -> str:
        """Sample function.

        Examples:
            >>> sample()
            '#sample()'

        Returns:
            Executable typst code.
        """
        return '#sample()'

    assert extract_examples(sample) == ">>> sample()\n'#sample()'"


def test_extract_examples_keeps_indented_heading_like_output() -> None:
    def sample() -> None:
        """Sample function.

        Examples:
            >>> print('Args:')
            Args:
            >>> print('done')
            done
        """

    assert (
        extract_examples(sample) == ">>> print('Args:')\nArgs:\n>>> print('done')\ndone"
    )


def test_extract_examples_reads_to_docstring_end() -> None:
    def sample() -> str:
        """Sample function.

        Examples:
            >>> sample()
            '#sample()'
        """
        return '#sample()'

    assert extract_examples(sample) == ">>> sample()\n'#sample()'"


def test_extract_examples_returns_none_without_examples_section() -> None:
    def sample() -> str:
        """Sample function.

        Returns:
            Executable typst code.
        """
        return '#sample()'

    assert extract_examples(sample) is None


def test_readme_renderers_use_structured_docs_data() -> None:
    table = render_implement_table(
        [ImplementRecord('std.demo', 'demo', 'https://example.test/demo', '0.x')]
    )
    examples = render_code_examples(
        [
            ExampleBlock(
                'std.demo',
                test_readme_renderers_use_structured_docs_data,
                ">>> demo()\n'#demo()'",
            )
        ]
    )

    assert table == (
        "| Package's function name | Typst's function name | Documentation on typst | Version |\n"
        '| --- | --- | --- | --- |\n'
        '| std.demo | demo | [https://example.test/demo](https://example.test/demo) | 0.x |\n'
    )
    assert examples == "`std.demo`:\n\n```python\n>>> demo()\n'#demo()'\n```\n\n"


def test_replace_generated_section_adds_markers_to_existing_readme() -> None:
    readme = '# Demo\n\nIntro.\n\n## Current Supports\n\nold\n'
    generated = f'{GENERATED_START}\n\n## Current Supports\n\nnew\n\n{GENERATED_END}\n'

    assert replace_generated_section(readme, generated) == (
        '# Demo\n\nIntro.\n\n'
        f'{GENERATED_START}\n\n## Current Supports\n\nnew\n\n{GENERATED_END}\n'
    )


def test_readme_generated_section_is_up_to_date() -> None:
    root = Path(__file__).parents[2]
    readme = (root / 'README.md').read_text(encoding='utf-8')
    start = readme.find(GENERATED_START)
    end = readme.find(GENERATED_END)

    assert start != -1 and end != -1
    end += len(GENERATED_END)
    assert readme[start:end] == build_content('all', markers=True).rstrip()
