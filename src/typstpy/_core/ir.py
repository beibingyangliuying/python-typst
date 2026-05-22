from dataclasses import dataclass
from typing import Protocol


class _TypstExpr(Protocol):
    def render(self) -> str: ...


@dataclass(frozen=True)
class _RawExpr:
    source: str

    def render(self) -> str:
        return self.source


@dataclass(frozen=True)
class _SequenceExpr:
    items: tuple['_TypstExpr', ...]

    def render(self) -> str:
        return f'({", ".join(item.render() for item in self.items)})'


@dataclass(frozen=True)
class _MappingExpr:
    entries: tuple[tuple[str, '_TypstExpr'], ...]

    def render(self) -> str:
        if not self.entries:
            return '(:)'
        return (
            '('
            + ', '.join(f'{key}: {value.render()}' for key, value in self.entries)
            + ')'
        )
