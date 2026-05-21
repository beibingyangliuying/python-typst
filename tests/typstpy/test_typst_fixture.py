from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


def test_generated_typst_fixture_is_up_to_date() -> None:
    """Keep the committed Typst fixture in sync with the collector."""
    root = Path(__file__).parents[2]
    fixture = Path(__file__).parents[1] / 'fixtures' / 'test.typ'
    result = subprocess.run(
        [sys.executable, 'scripts/generate_typst_fixture.py'],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert fixture.read_text(encoding='utf-8') == result.stdout, (
        'Run `python scripts/generate_typst_fixture.py --write '
        'tests/fixtures/test.typ` to update the fixture.'
    )


def test_generated_typst_fixture_compiles(tmp_path: Path) -> None:
    """Compile the generated Typst fixture when the Typst CLI is available."""
    typst = shutil.which('typst')
    if typst is None:
        pytest.skip('typst CLI is not installed')
    assert typst is not None

    fixture = Path(__file__).parents[1] / 'fixtures' / 'test.typ'
    output = tmp_path / 'test.pdf'

    result = subprocess.run(
        [typst, 'compile', fixture.name, str(output)],
        cwd=fixture.parent,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert output.exists()
