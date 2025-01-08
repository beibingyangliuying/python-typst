import inspect
from typing import Callable

from typstpy.std import (
    align,
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
    padding,
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
    padding,
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
    print(func._implement)  # type: ignore


def extract_examples(func: Callable) -> str | None:
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
    return '\n'.join(i.lstrip() for i in examples.splitlines())


with open('test.typ', 'w', encoding='utf-8') as f:
    for func in funcs:
        examples = extract_examples(func)
        if examples is None:
            continue

        print(f'`{func.__name__}`:', '\n```python', examples, '```\n', sep='\n')
        f.write(
            '\n'.join(
                i.strip("'")
                for i in examples.splitlines()
                if not i.startswith('>>>') and not i.startswith('...')
            )
        )
        f.write('\n')
