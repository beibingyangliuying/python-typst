from typing import Protocol

import attrs


class TypstExpr(Protocol):
    def render(self) -> str: ...


@attrs.frozen
class RawExpr:
    source: str

    def render(self) -> str:
        return self.source


@attrs.frozen
class SequenceExpr:
    items: tuple['TypstExpr', ...]

    def render(self) -> str:
        return f'({", ".join(item.render() for item in self.items)})'


@attrs.frozen
class MappingExpr:
    entries: tuple[tuple[str, 'TypstExpr'], ...]

    def render(self) -> str:
        if not self.entries:
            return '(:)'
        return (
            '('
            + ', '.join(f'{key}: {value.render()}' for key, value in self.entries)
            + ')'
        )
