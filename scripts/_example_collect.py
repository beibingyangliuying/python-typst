from __future__ import annotations

import ast
import contextlib
import doctest
import importlib
import io
import sys
import warnings
from collections.abc import Callable
from pathlib import Path
from typing import Any

import attrs

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from typstpy._docs import collect_example_blocks  # noqa: E402


@attrs.frozen
class TypstExample:
    """A Typst snippet collected from one Python doctest example."""

    qualname: str
    index: int
    source: str
    typst: str


@attrs.frozen
class SkippedExample:
    """A doctest example or result intentionally excluded from the fixture."""

    qualname: str
    index: int
    source: str
    reason: str


@attrs.frozen
class FailedExample:
    """A doctest example that failed while being executed."""

    qualname: str
    index: int
    source: str
    error: str


def _module_namespace(func: Callable[..., Any]) -> dict[str, Any]:
    module = importlib.import_module(func.__module__)
    return dict(module.__dict__)


def _run_source(source: str, namespace: dict[str, Any]) -> Any:
    try:
        expression = ast.parse(source, mode='eval')
    except SyntaxError:
        exec(compile(source, '<doctest>', 'exec'), namespace)
        return None
    return eval(compile(expression, '<doctest>', 'eval'), namespace)


def collect_typst_examples() -> tuple[
    list[TypstExample], list[SkippedExample], list[FailedExample]
]:
    """Execute registered doctests and collect Typst code string results."""
    parser = doctest.DocTestParser()
    collected: list[TypstExample] = []
    skipped: list[SkippedExample] = []
    failed: list[FailedExample] = []

    for block in collect_example_blocks():
        namespace = _module_namespace(block.func)
        for index, example in enumerate(parser.get_examples(block.source), start=1):
            source = example.source.strip()
            try:
                with (
                    warnings.catch_warnings(),
                    contextlib.redirect_stdout(io.StringIO()),
                ):
                    warnings.simplefilter('ignore', DeprecationWarning)
                    result = _run_source(example.source, namespace)
            # Intentionally broad: doctests may raise any exception type;
            # we report them as failures without crashing the collector.
            # Infrastructure errors (ImportError, SystemExit) are unlikely
            # in normal operation since all modules are already imported.
            except Exception as exc:  # noqa: BLE001 - report doctest failures.
                failed.append(FailedExample(block.qualname, index, source, repr(exc)))
                continue

            if result is None:
                continue
            if not isinstance(result, str):
                skipped.append(
                    SkippedExample(block.qualname, index, source, 'result is not str')
                )
                continue
            if not result.startswith('#'):
                skipped.append(
                    SkippedExample(
                        block.qualname, index, source, 'result is not Typst code'
                    )
                )
                continue
            collected.append(TypstExample(block.qualname, index, source, result))

    return collected, skipped, failed
