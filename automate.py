import inspect
from typing import Callable

from typstpy.functions import (
    _color_hsl,
    _color_linear_rgb,
    _figure_caption,
    bibliography,
    cite,
    cmyk,
    color,
    emph,
    figure,
    footnote,
    heading,
    image,
    link,
    lorem,
    lower,
    luma,
    pagebreak,
    par,
    ref,
    rgb,
    smallcaps,
    strong,
    sub,
    sup,
    text,
)

funcs = (
    _color_hsl,
    _color_linear_rgb,
    _figure_caption,
    bibliography,
    cite,
    cmyk,
    color,
    emph,
    figure,
    footnote,
    heading,
    image,
    link,
    lorem,
    lower,
    luma,
    pagebreak,
    par,
    ref,
    rgb,
    smallcaps,
    strong,
    sub,
    sup,
    text,
)

for func in funcs:
    print(func._implement.to_markdown())  # type:ignore


def extract_examples(func: Callable) -> str | None:
    docstring = inspect.getdoc(func)
    if not docstring:
        return None

    sign = "Examples:"
    start = docstring.index(sign) + len(sign) + 1
    end = len(docstring)

    result = docstring[start:end]
    return "\n".join(i.lstrip() for i in result.splitlines())


for func in funcs:
    print(func.__name__)
    print("\n```python")
    print(extract_examples(func))
    print("```\n")
