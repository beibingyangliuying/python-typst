from typing import Any, Callable, Protocol

Block = str
"""Executable typst code."""
TypstFunc = Callable[..., Block]
"""Functions that generate executable typst code."""
Predicate = Callable[[], bool]

# region concepts


class Normal(Protocol):
    def __call__(
        self, core: Any, /, *positional: Any, **keyword_only: Any
    ) -> Block: ...


class Positional(Protocol):
    def __call__(self, *positional: Any) -> Block: ...


class Instance(Protocol):
    def __call__(
        self, instance: Block, /, *positional: Any, **keyword_only: Any
    ) -> Block: ...


class Series(Protocol):
    def __call__(self, *elements: Any, **keyword_only: Any) -> Block: ...


# endregion

__all__ = [
    'Block',
    'TypstFunc',
    'Predicate',
    'Normal',
    'Positional',
    'Instance',
    'Series',
]
