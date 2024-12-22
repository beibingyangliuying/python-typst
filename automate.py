import inspect
import warnings
from typing import Callable

from typstpy.std import (
    align,
    arguments,
    bibliography,
    block,
    box,
    bullet_list,
    circle,
    cite,
    cmyk,
    colbreak,
    color,
    columns,
    document,
    ellipse,
    emph,
    figure,
    footnote,
    gradient,
    grid,
    heading,
    hide,
    highlight,
    hspace,
    image,
    layout,
    line,
    linebreak,
    link,
    lorem,
    lower,
    luma,
    measure,
    move,
    numbered_list,
    numbering,
    oklab,
    oklch,
    outline,
    overline,
    pad,
    page,
    pagebreak,
    par,
    parbreak,
    path,
    pattern,
    place,
    polygon,
    quote,
    raw,
    rect,
    ref,
    repeat,
    rgb,
    rotate,
    scale,
    skew,
    smallcaps,
    smartquote,
    square,
    stack,
    strike,
    stroke,
    strong,
    subscript,
    superscript,
    table,
    terms,
    text,
    underline,
    upper,
    vspace,
)

funcs = (
    align,
    arguments,
    bibliography,
    block,
    box,
    bullet_list,
    circle,
    cite,
    cmyk,
    colbreak,
    color,
    columns,
    document,
    ellipse,
    emph,
    figure,
    footnote,
    gradient,
    grid,
    heading,
    hide,
    highlight,
    hspace,
    image,
    layout,
    line,
    linebreak,
    link,
    lorem,
    lower,
    luma,
    measure,
    move,
    numbered_list,
    numbering,
    oklab,
    oklch,
    outline,
    overline,
    pad,
    page,
    pagebreak,
    par,
    parbreak,
    path,
    pattern,
    place,
    polygon,
    quote,
    raw,
    rect,
    ref,
    repeat,
    rgb,
    rotate,
    scale,
    skew,
    smallcaps,
    smartquote,
    square,
    stack,
    strike,
    stroke,
    strong,
    subscript,
    superscript,
    table,
    terms,
    text,
    underline,
    upper,
    vspace,
)

for func in funcs:
    print(func._implement)  # type:ignore


def extract_examples(func: Callable) -> str | None:
    docstring = inspect.getdoc(func)
    if not docstring:
        return None

    sign = 'Examples:'
    if sign not in docstring:
        warnings.warn(f"Function {func} doesn't have examples.")
        return None
    start = docstring.index(sign) + len(sign) + 1

    result = docstring[start:]
    return '\n'.join(i.lstrip() for i in result.splitlines())


with open('test.typ', 'w', encoding='utf-8') as f:
    for func in funcs:
        examples = extract_examples(func)
        if examples is None:
            continue

        print(f'`{func.__name__}`:')
        print('\n```python')
        print(examples)
        print('```\n')

        f.write(
            '\n'.join(
                i.strip("'")
                for i in examples.splitlines()
                if not i.startswith('>>>') and not i.startswith('...')
            )
        )
        f.write('\n')
