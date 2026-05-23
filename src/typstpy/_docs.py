from __future__ import annotations

import importlib
import inspect
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any

from typstpy._core import Implement

_SECTION_HEADING_RE = re.compile(r'[A-Za-z][A-Za-z0-9 _-]*:')


def _is_documented_module(module: str) -> bool:
    return module == 'typstpy.subpar' or module.startswith('typstpy.std.')


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


def _iter_public_function_paths() -> Iterable[tuple[Callable[..., Any], str]]:
    for module_name, prefix in (('typstpy.std', 'std'), ('typstpy.subpar', 'subpar')):
        module = importlib.import_module(module_name)
        for name in getattr(
            module, '__all__', ()
        ):  # pragma: no branch - modules define it.
            obj = getattr(module, name, None)
            if callable(obj) and obj in Implement.permanent:
                yield obj, f'{prefix}.{name}'
            for attr_name, attr in getattr(obj, '__dict__', {}).items():
                if attr_name in {'where', 'with_'} or attr_name.startswith('_'):
                    continue
                if callable(attr) and attr in Implement.permanent:
                    yield attr, f'{prefix}.{name}.{attr_name}'


def iter_registered_functions() -> list[Callable[..., Any]]:
    """Return registered functions in deterministic order."""
    ensure_registry_loaded()
    return sorted(
        [
            func
            for func in Implement.permanent
            if _is_documented_module(func.__module__)
        ],
        key=lambda func: (func.__module__, func.__name__),
    )


def function_qualname(func: Callable[..., Any]) -> str:
    """Return a project-relative qualified name for a registered function."""
    ensure_registry_loaded()
    paths = [
        path for candidate, path in _iter_public_function_paths() if candidate is func
    ]
    if paths:
        return sorted(paths, key=lambda path: (path.count('.'), path))[0]

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
        implement = Implement.permanent[func]
        records.append(
            ImplementRecord(
                function_qualname(func),
                implement.original_name,
                implement.hyperlink,
                implement.version,
            )
        )
    return sorted(records, key=lambda record: record.qualname)


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
    return sorted(blocks, key=lambda block: block.qualname)


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
