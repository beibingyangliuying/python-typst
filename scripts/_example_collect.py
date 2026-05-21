from __future__ import annotations

import ast
import contextlib
import doctest
import importlib
import inspect
import io
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from typstpy._core import _Implement  # noqa: E402


@dataclass(frozen=True)
class ExampleBlock:
    """Doctest examples extracted from one registered typstpy function."""

    qualname: str
    func: Callable[..., Any]
    source: str


@dataclass(frozen=True)
class TypstExample:
    """A Typst snippet collected from one Python doctest example."""

    qualname: str
    index: int
    source: str
    typst: str


@dataclass(frozen=True)
class SkippedExample:
    """A doctest example or result intentionally excluded from the fixture."""

    qualname: str
    index: int
    source: str
    reason: str


def ensure_registry_loaded() -> None:
    """Import modules whose decorators populate the implementation registry."""
    import typstpy.std  # noqa: F401
    import typstpy.subpar  # noqa: F401


def iter_registered_functions() -> list[Callable[..., Any]]:
    """Return registered functions in deterministic order."""
    ensure_registry_loaded()
    return sorted(
        _Implement.permanent,
        key=lambda func: (func.__module__, func.__name__),
    )


def function_qualname(func: Callable[..., Any]) -> str:
    """Return a project-relative qualified name for a registered function."""
    module = func.__module__
    if module.startswith('typstpy.'):
        module = module[len('typstpy.') :]
    return f'{module}.{func.__name__}'


def extract_examples(func: Callable[..., Any]) -> str | None:
    """Extract the Google-style Examples section from a function docstring."""
    docstring = inspect.getdoc(func)
    if not docstring:
        return None

    sign_start = 'Examples:'
    if sign_start not in docstring:
        return None
    index_start = docstring.index(sign_start) + len(sign_start) + 1

    sign_end = 'See also:'
    index_end = docstring.index(sign_end) if sign_end in docstring else None

    examples = (
        docstring[index_start:index_end] if index_end else docstring[index_start:]
    )
    return '\n'.join(line.lstrip() for line in examples.splitlines())


def iter_example_blocks() -> list[ExampleBlock]:
    """Return doctest example blocks from all registered functions."""
    blocks: list[ExampleBlock] = []
    for func in iter_registered_functions():
        source = extract_examples(func)
        if source is None:
            continue
        blocks.append(ExampleBlock(function_qualname(func), func, source))
    return blocks


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


def collect_typst_examples() -> tuple[list[TypstExample], list[SkippedExample]]:
    """Execute registered doctests and collect Typst code string results."""
    parser = doctest.DocTestParser()
    collected: list[TypstExample] = []
    skipped: list[SkippedExample] = []

    for block in iter_example_blocks():
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
            except Exception as exc:  # noqa: BLE001 - report and skip broken examples.
                skipped.append(
                    SkippedExample(block.qualname, index, source, f'raised {exc!r}')
                )
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

    return collected, skipped
