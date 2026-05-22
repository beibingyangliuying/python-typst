from __future__ import annotations

import inspect
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any

from typstpy._core import _Implement

_SECTION_HEADING_RE = re.compile(r'[A-Za-z][A-Za-z0-9 _-]*:')


@dataclass(frozen=True)
class ImplementRecord:
    """Structured metadata for one registered typstpy function."""

    qualname: str
    original_name: str
    hyperlink: str | None
    version: str | None


@dataclass(frozen=True)
class ExampleBlock:
    """Google-style Examples section extracted from one function."""

    qualname: str
    func: Callable[..., Any]
    source: str


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


def collect_implement_records(
    functions: Iterable[Callable[..., Any]] | None = None,
) -> list[ImplementRecord]:
    """Return structured metadata for registered functions."""
    if functions is None:
        functions = iter_registered_functions()

    records: list[ImplementRecord] = []
    for func in functions:
        implement = _Implement.permanent[func]
        records.append(
            ImplementRecord(
                function_qualname(func),
                implement.original_name,
                implement.hyperlink,
                implement.version,
            )
        )
    return records


def _is_top_level_section_heading(line: str) -> bool:
    if not line or line[0].isspace():
        return False
    return _SECTION_HEADING_RE.fullmatch(line.strip()) is not None


def extract_examples(func: Callable[..., Any]) -> str | None:
    """Extract a Google-style Examples section from a function docstring."""
    docstring = inspect.getdoc(func)
    if not docstring:
        return None

    lines = docstring.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == 'Examples:' and _is_top_level_section_heading(line):
            start = index + 1
            break
    if start is None:
        return None

    end = len(lines)
    for index, line in enumerate(lines[start:], start=start):
        if _is_top_level_section_heading(line):
            end = index
            break

    source = inspect.cleandoc('\n'.join(lines[start:end]))
    return source


def collect_example_blocks(
    functions: Iterable[Callable[..., Any]] | None = None,
) -> list[ExampleBlock]:
    """Return Examples sections from registered functions."""
    if functions is None:
        functions = iter_registered_functions()

    blocks: list[ExampleBlock] = []
    for func in functions:
        source = extract_examples(func)
        if source is None:
            continue
        blocks.append(ExampleBlock(function_qualname(func), func, source))
    return blocks


__all__ = [
    'ExampleBlock',
    'ImplementRecord',
    'collect_example_blocks',
    'collect_implement_records',
    'ensure_registry_loaded',
    'extract_examples',
    'function_qualname',
    'iter_registered_functions',
]
