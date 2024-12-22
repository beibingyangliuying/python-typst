from typing import Any, Iterable

from .._utils import attach_func, implement, normal, post_series
from ..typings import Block


@implement(
    True,
    original_name='align',
    hyperlink='https://typst.app/docs/reference/layout/align/',
)
def align(body: str, /, *, alignment: str = 'start + top') -> Block:
    return normal(align, body, alignment=alignment)


@implement(
    True,
    original_name='block',
    hyperlink='https://typst.app/docs/reference/layout/block/',
)
def block(
    body: str | None = None,
    /,
    *,
    width: str = 'auto',
    height: str = 'auto',
    breakable: bool = True,
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = dict(),
    radius: str | dict[str, Any] = dict(),
    inset: str | dict[str, Any] = dict(),
    outset: str | dict[str, Any] = dict(),
    spacing: str = '1.2em',
    above: str = 'auto',
    below: str = 'auto',
    clip: bool = False,
    sticky: bool = False,
) -> Block:
    return normal(
        block,
        body,
        width=width,
        height=height,
        breakable=breakable,
        fill=fill,
        stroke=stroke,
        radius=radius,
        inset=inset,
        outset=outset,
        spacing=spacing,
        above=above,
        below=below,
        clip=clip,
        sticky=sticky,
    )


@implement(
    True,
    original_name='box',
    hyperlink='https://typst.app/docs/reference/layout/box/',
)
def box(
    body: str | None = None,
    /,
    *,
    width: str = 'auto',
    height: str = 'auto',
    baseline: str = '0% + 0pt',
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = dict(),
    radius: str | dict[str, Any] = dict(),
    inset: str | dict[str, Any] = dict(),
    outset: str | dict[str, Any] = dict(),
    clip: bool = False,
) -> Block:
    return normal(
        box,
        body,
        width=width,
        height=height,
        baseline=baseline,
        fill=fill,
        stroke=stroke,
        radius=radius,
        inset=inset,
        outset=outset,
        clip=clip,
    )


@implement(
    True,
    original_name='colbreak',
    hyperlink='https://typst.app/docs/reference/layout/colbreak/',
)
def colbreak(*, weak: bool = False) -> Block:
    return normal(colbreak, weak=weak)


@implement(
    True,
    original_name='columns',
    hyperlink='https://typst.app/docs/reference/layout/columns/',
)
def columns(body: str, /, *, count: int = 2, gutter: str = '4% + 0pt') -> Block:
    return normal(columns, body, count=count, gutter=gutter)


@implement(
    True,
    original_name='grid.cell',
    hyperlink='https://typst.app/docs/reference/layout/grid/#definitions-cell',
)
def _grid_cell(
    body: str,
    /,
    *,
    x: str | int = 'auto',
    y: str | int = 'auto',
    colspan: int = 1,
    rowspan: int = 1,
    fill: str | None = 'auto',
    align: str = 'auto',
    inset: str = 'auto',
    stroke: str | dict[str, Any] | None = dict(),
    breakable: str | bool = 'auto',
) -> Block:
    return normal(
        _grid_cell,
        body,
        x=x,
        y=y,
        colspan=colspan,
        rowspan=rowspan,
        fill=fill,
        align=align,
        inset=inset,
        stroke=stroke,
        breakable=breakable,
    )


@implement(
    True,
    original_name='grid.hline',
    hyperlink='https://typst.app/docs/reference/layout/grid/#definitions-hline',
)
def _grid_hline(
    *,
    y: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'top',
) -> Block:
    return normal(
        _grid_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    True,
    original_name='grid.vline',
    hyperlink='https://typst.app/docs/reference/layout/grid/#definitions-vline',
)
def _grid_vline(
    *,
    x: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'start',
) -> Block:
    return normal(
        _grid_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    True,
    original_name='grid.header',
    hyperlink='https://typst.app/docs/reference/layout/grid/#definitions-header',
)
def _grid_header(*children: str, repeat: bool = True) -> Block:
    return post_series(_grid_header, *children, repeat=repeat)


@implement(
    True,
    original_name='grid.footer',
    hyperlink='https://typst.app/docs/reference/layout/grid/#definitions-footer',
)
def _grid_footer(*children: str, repeat: bool = True) -> Block:
    return post_series(_grid_footer, *children, repeat=repeat)


@attach_func(_grid_cell, 'cell')
@attach_func(_grid_hline, 'hline')
@attach_func(_grid_vline, 'vline')
@attach_func(_grid_header, 'header')
@attach_func(_grid_footer, 'footer')
@implement(
    True,
    original_name='grid',
    hyperlink='https://typst.app/docs/reference/layout/grid/',
)
def grid(
    *children,
    columns: str | int | Iterable[str] = tuple(),
    rows: str | int | Iterable[str] = tuple(),
    gutter: str | int | Iterable[str] = tuple(),
    column_gutter: str | int | Iterable[str] = tuple(),
    row_gutter: str | int | Iterable[str] = tuple(),
    fill: str | Iterable[str] | None = None,
    align: str | Iterable[str] = 'auto',
    stroke: str | Iterable[str] | dict[str, Any] | None = None,
    inset: str | Iterable[str] | dict[str, Any] = dict(),
) -> Block:
    return post_series(
        grid,
        *children,
        columns=columns,
        rows=rows,
        gutter=gutter,
        column_gutter=column_gutter,
        row_gutter=row_gutter,
        fill=fill,
        align=align,
        stroke=stroke,
        inset=inset,
    )


@implement(
    True,
    original_name='hide',
    hyperlink='https://typst.app/docs/reference/layout/hide/',
)
def hide(body: str, /) -> Block:
    return normal(hide, body)


@implement(
    True,
    original_name='layout',
    hyperlink='https://typst.app/docs/reference/layout/layout/',
)
def layout(func: str, /) -> Block:
    return normal(layout, func)


@implement(
    True,
    original_name='measure',
    hyperlink='https://typst.app/docs/reference/layout/measure/',
)
def measure(body: str, /, *, width: str = 'auto', height: str = 'auto') -> Block:
    return normal(measure, body, width=width, height=height)


@implement(
    True,
    original_name='move',
    hyperlink='https://typst.app/docs/reference/layout/move/',
)
def move(body: str, /, *, dx: str = '0% + 0pt', dy: str = '0% + 0pt') -> Block:
    return normal(move, body, dx=dx, dy=dy)


@implement(
    True,
    original_name='pad',
    hyperlink='https://typst.app/docs/reference/layout/pad/',
)
def pad(
    body: str,
    /,
    *,
    left: str = '0% + 0pt',
    top: str = '0% + 0pt',
    right: str = '0% + 0pt',
    bottom: str = '0% + 0pt',
    x: str = '0% + 0pt',
    y: str = '0% + 0pt',
    rest: str = '0% + 0pt',
) -> Block:
    return normal(
        pad, body, left=left, top=top, right=right, bottom=bottom, x=x, y=y, rest=rest
    )


@implement(
    True,
    original_name='page',
    hyperlink='https://typst.app/docs/reference/layout/page/',
)
def page(
    body: str,
    /,
    *,
    paper: str = '"a4"',
    width: str = '595.28pt',
    height: str = '841.89pt',
    flipped: bool = False,
    margin: str | dict[str, Any] = 'auto',
    binding: str = 'auto',
    columns: int = 1,
    fill: str | None = 'auto',
    numbering: str | None = None,
    number_align='center + bottom',
    header: str | None = 'auto',
    header_ascent: str = '30% + 0pt',
    footer: str | None = 'auto',
    footer_ascent: str = '30% + 0pt',
    background: str | None = None,
    foreground: str | None = None,
) -> Block:
    return normal(
        page,
        body,
        paper=paper,
        width=width,
        height=height,
        flipped=flipped,
        margin=margin,
        binding=binding,
        columns=columns,
        fill=fill,
        numbering=numbering,
        number_align=number_align,
        header=header,
        header_ascent=header_ascent,
        footer=footer,
        footer_ascent=footer_ascent,
        background=background,
        foreground=foreground,
    )


@implement(
    True,
    original_name='pagebreak',
    hyperlink='https://typst.app/docs/reference/layout/pagebreak/',
)
def pagebreak(*, weak: bool = False, to: str | None = None) -> Block:
    return normal(pagebreak, weak=weak, to=to)


@implement(
    True,
    original_name='place.flush',
    hyperlink='https://typst.app/docs/reference/layout/place/#definitions-flush',
)
def _place_flush() -> Block:
    return normal(_place_flush)


@attach_func(_place_flush, 'flush')
@implement(
    True,
    original_name='place',
    hyperlink='https://typst.app/docs/reference/layout/place/',
)
def place(
    body: str,
    /,
    *,
    alignment: str = 'start',
    scope: str = '"column"',
    float: bool = False,
    clearance: str = '1.5em',
    dx: str = '0% + 0pt',
    dy: str = '0% + 0pt',
) -> Block:
    return normal(
        place,
        body,
        alignment=alignment,
        scope=scope,
        float=float,
        clearance=clearance,
        dx=dx,
        dy=dy,
    )


@implement(
    True,
    original_name='repeat',
    hyperlink='https://typst.app/docs/reference/layout/repeat/',
)
def repeat(body: str, /, *, gap: str = '0pt', justify: bool = True) -> Block:
    """Interface of `repeat` in typst. See [the documentation](https://typst.app/docs/reference/layout/repeat/) for more information.

    Args:
        body (str): The content to repeat.
        gap (str, optional): The gap between each instance of the body. Defaults to '0pt'.
        justify (bool, optional): Whether to increase the gap between instances to completely fill the available space. Defaults to True.

    Returns:
        Block: Executable typst code.
    """
    return normal(repeat, body, gap=gap, justify=justify)


@implement(
    True,
    original_name='rotate',
    hyperlink='https://typst.app/docs/reference/layout/rotate/',
)
def rotate(
    body: str,
    /,
    *,
    angle: str = '0deg',
    origin: str = 'center + horizon',
    reflow: bool = False,
) -> Block:
    """Interface of `rotate` in typst. See [the documentation](https://typst.app/docs/reference/layout/rotate/) for more information.

    Args:
        body (str): The content to rotate.
        angle (str, optional): The amount of rotation. Defaults to '0deg'.
        origin (str, optional): The origin of the rotation. Defaults to 'center + horizon'.
        reflow (bool, optional): Whether the rotation impacts the layout. Defaults to False.

    Returns:
        Block: Executable typst code.
    """
    return normal(rotate, body, angle=angle, origin=origin, reflow=reflow)


@implement(
    True,
    original_name='scale',
    hyperlink='https://typst.app/docs/reference/layout/scale/',
)
def scale(
    body: str,
    /,
    *,
    factor: str = '100%',
    x: str = '100%',
    y: str = '100%',
    origin: str = 'center + horizon',
    reflow: bool = False,
) -> Block:
    """Interface of `scale` in typst. See [the documentation](https://typst.app/docs/reference/layout/scale/) for more information.

    Args:
        body (str): The content to scale.
        factor (str, optional): The scaling factor for both axes, as a positional argument. Defaults to '100%'.
        x (str, optional): The horizontal scaling factor. Defaults to '100%'.
        y (str, optional): The vertical scaling factor. Defaults to '100%'.
        origin (str, optional): The origin of the transformation. Defaults to 'center + horizon'.
        reflow (bool, optional): Whether the scaling impacts the layout. Defaults to False.

    Returns:
        Block: Executable typst code.
    """
    return normal(scale, body, factor=factor, x=x, y=y, origin=origin, reflow=reflow)


@implement(
    True,
    original_name='skew',
    hyperlink='https://typst.app/docs/reference/layout/skew/',
)
def skew(
    body: str,
    /,
    *,
    ax: str = '0deg',
    ay: str = '0deg',
    origin: str = 'center + horizon',
    reflow: bool = False,
) -> Block:
    """Interface of `skew` in typst. See [the documentation](https://typst.app/docs/reference/layout/skew/) for more information.

    Args:
        body (str): The content to skew.
        ax (str, optional): The horizontal skewing angle. Defaults to '0deg'.
        ay (str, optional): The vertical skewing angle. Defaults to '0deg'.
        origin (str, optional): The origin of the skew transformation. Defaults to 'center + horizon'.
        reflow (bool, optional): Whether the skew transformation impacts the layout. Defaults to False.

    Returns:
        Block: Executable typst code.
    """
    return normal(skew, body, ax=ax, ay=ay, origin=origin, reflow=reflow)


@implement(
    True,
    original_name='h',
    hyperlink='https://typst.app/docs/reference/layout/h/',
)
def hspace(amount: str, /, *, weak: bool = False) -> Block:
    """Interface of `h` in typst. See [the documentation](https://typst.app/docs/reference/layout/h/) for more information.

    Args:
        amount (str): How much spacing to insert.
        weak (bool, optional): If true, the spacing collapses at the start or end of a paragraph. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> hspace('1em')
        '#h(1em)'
        >>> hspace('1em', weak=True)
        '#h(1em, weak: true)'
    """
    return normal(hspace, amount, weak=weak)


@implement(
    True,
    original_name='v',
    hyperlink='https://typst.app/docs/reference/layout/v/',
)
def vspace(amount: str, /, *, weak: bool = False) -> Block:
    """Interface of `v` in typst. See [the documentation](https://typst.app/docs/reference/layout/v/) for more information.

    Args:
        amount (str): How much spacing to insert.
        weak (bool, optional): If true, the spacing collapses at the start or end of a flow. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> vspace('1em')
        '#v(1em)'
        >>> vspace('1em', weak=True)
        '#v(1em, weak: true)'
    """
    return normal(vspace, amount, weak=weak)


@implement(
    True,
    original_name='stack',
    hyperlink='https://typst.app/docs/reference/layout/stack/',
)
def stack(*children: str, dir: str = 'ttb', spacing: str | None = None) -> Block:
    return post_series(stack, *children, dir=dir, spacing=spacing)
