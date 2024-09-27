import inspect
from typing import Callable

from cytoolz.curried import concat, map, pipe  # type:ignore

from typstpy import (
    bibliography,
    cite,
    cmyk,
    color,
    emph,
    figure,
    heading,
    image,
    lorem,
    luma,
    pagebreak,
    par,
    ref,
    rgb,
    strong,
    text,
)


def information(func: Callable) -> tuple[tuple[str, tuple[str, ...], str], ...]:
    _funcs = (func,) + tuple(
        getattr(func, attribute)
        for attribute in dir(func)
        if not attribute.startswith("_")
    )
    return pipe(
        _funcs,
        map(
            lambda x: (
                x.__name__
                if not x.__name__.startswith("_")
                else f"{func.__name__}.{x.__name__.strip('_')}",
                tuple(inspect.signature(x).parameters),
                str(x._implement_type.name),
            )
        ),
        tuple,
    )


def format(name: str, params: tuple[str, ...], implement_type: str) -> str:
    return f"| {name} | {', '.join(params)} | {implement_type} |"


funcs = (
    bibliography,
    cite,
    cmyk,
    color,
    emph,
    figure,
    heading,
    image,
    lorem,
    luma,
    pagebreak,
    par,
    ref,
    rgb,
    strong,
    text,
)

informations = pipe(funcs, map(information), tuple, concat)
for i, j, k in informations:
    print(format(i, j, k))
