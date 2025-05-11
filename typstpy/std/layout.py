from typing import Iterable

from typstpy._constants import VALID_PAPER_SIZES
from typstpy._core import attach_func, implement, normal, positional, post_series
from typstpy.std.text import lorem  # noqa
from typstpy.std.visualize import rect  # noqa
from typstpy.typings import (
    Alignment,
    Angle,
    Auto,
    BoxInset,
    BoxOutset,
    Color,
    Content,
    Direction,
    Fraction,
    Function,
    Gradient,
    Length,
    PageMargin,
    PaperSizes,
    Ratio,
    RectangleRadius,
    RectangleStroke,
    Relative,
    Stroke,
    Tiling,
)


@implement('align', 'https://typst.app/docs/reference/layout/align/')
def align(body: Content, alignment: Alignment = 'start + top', /):
    """Interface of `align` in typst. See [the documentation](https://typst.app/docs/reference/layout/align/) for more information.

    Args:
        body: The content to align.
        alignment: The alignment along both axes. Defaults to 'start + top'.

    Returns:
        Executable typst code.

    Examples:
        >>> align('"Hello, World!"', 'center')
        '#align("Hello, World!", center)'
        >>> align('[Hello, World!]', 'center')
        '#align([Hello, World!], center)'
        >>> align(lorem(20), 'center')
        '#align(lorem(20), center)'
    """
    return positional(
        align,
        *([body] if alignment == 'start + top' else [body, alignment]),
    )


@implement('block', 'https://typst.app/docs/reference/layout/block/')
def block(
    body: None | Content = '',
    /,
    *,
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    breakable: bool = True,
    fill: None | Color | Gradient | Tiling = None,
    stroke: None | Length | Color | Gradient | Stroke | Tiling | RectangleStroke = {},
    radius: Relative | RectangleRadius = {},
    inset: Relative | BoxInset = {},
    outset: Relative | BoxOutset = {},
    spacing: Relative | Fraction = '1.2em',
    above: Auto | Relative | Fraction = 'auto',
    below: Auto | Relative | Fraction = 'auto',
    clip: bool = False,
    sticky: bool = False,
):
    """Interface of `block` in typst. See [the documentation](https://typst.app/docs/reference/layout/block/) for more information.

    Args:
        body: The contents of the block. Defaults to ''.
        width: The block's width. Defaults to 'auto'.
        height: The block's height. Defaults to 'auto'.
        breakable: Whether the block can be broken and continue on the next page. Defaults to True.
        fill: The block's background color. Defaults to None.
        stroke: The block's border color. Defaults to {}.
        radius: How much to round the block's corners. Defaults to {}.
        inset: How much to round the block's corners. Defaults to {}.
        outset: How much to round the block's corners. Defaults to {}.
        spacing: The spacing around the block. Defaults to '1.2em'.
        above: The spacing between this block and its predecessor. Defaults to 'auto'.
        below: The spacing between this block and its successor. Defaults to 'auto'.
        clip: Whether to clip the content inside the block. Defaults to False.
        sticky: Whether this block must stick to the following one, with no break in between. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> block('"Hello, World!"')
        '#block("Hello, World!")'
        >>> block('[Hello, World!]')
        '#block([Hello, World!])'
        >>> block(lorem(20))
        '#block(lorem(20))'
        >>> block(lorem(20), width='100%')
        '#block(lorem(20), width: 100%)'
    """
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


@implement('box', 'https://typst.app/docs/reference/layout/box/')
def box(
    body: None | Content = '',
    /,
    *,
    width: Auto | Relative | Fraction = 'auto',
    height: Auto | Relative = 'auto',
    baseline: Relative = '0% + 0pt',
    fill: None | Color | Gradient | Tiling = None,
    stroke: None | Length | Color | Gradient | Stroke | Tiling | RectangleStroke = {},
    radius: Relative | RectangleRadius = {},
    inset: Relative | BoxInset = {},
    outset: Relative | BoxOutset = {},
    clip: bool = False,
):
    """Interface of `box` in typst. See [the documentation](https://typst.app/docs/reference/layout/box/) for more information.

    Args:
        body: The contents of the box. Defaults to ''.
        width: The width of the box. Defaults to 'auto'.
        height: The height of the box. Defaults to 'auto'.
        baseline: An amount to shift the box's baseline by. Defaults to '0% + 0pt'.
        fill: The box's background color. Defaults to None.
        stroke: The box's border color. Defaults to {}.
        radius: How much to round the box's corners. Defaults to {}.
        inset: How much to pad the box's content. Defaults to {}.
        outset: How much to expand the box's size without affecting the layout. Defaults to {}.
        clip: Whether to clip the content inside the box. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> box('"Hello, World!"')
        '#box("Hello, World!")'
        >>> box('[Hello, World!]')
        '#box([Hello, World!])'
        >>> box(lorem(20))
        '#box(lorem(20))'
        >>> box(lorem(20), width='100%')
        '#box(lorem(20), width: 100%)'
    """
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


@implement('colbreak', 'https://typst.app/docs/reference/layout/colbreak/')
def colbreak(*, weak: bool = False):
    """Interface of `colbreak` in typst. See [the documentation](https://typst.app/docs/reference/layout/colbreak/) for more information.

    Args:
        weak: If true, the column break is skipped if the current column is already empty. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> colbreak()
        '#colbreak()'
        >>> colbreak(weak=True)
        '#colbreak(weak: true)'
    """
    return normal(colbreak, weak=weak)


@implement('columns', 'https://typst.app/docs/reference/layout/columns/')
def columns(body: Content, count: int = 2, /, *, gutter: Relative = '4% + 0pt'):
    """Interface of `columns` in typst. See [the documentation](https://typst.app/docs/reference/layout/columns/) for more information.

    Args:
        body: The content that should be layouted into the columns.
        count: The number of columns. Defaults to 2.
        gutter: The size of the gutter space between each column. Defaults to '4% + 0pt'.

    Returns:
        Executable typst code.

    Examples:
        >>> columns(lorem(20))
        '#columns(lorem(20))'
        >>> columns(lorem(20), 3)
        '#columns(lorem(20), 3)'
        >>> columns(lorem(20), 3, gutter='8% + 0pt')
        '#columns(lorem(20), 3, gutter: 8% + 0pt)'
    """
    return normal(
        columns,
        *([body] if count == 2 else [body, count]),  # type: ignore
        gutter=gutter,
    )


@implement(
    'grid.cell', 'https://typst.app/docs/reference/layout/grid/#definitions-cell'
)
def _grid_cell(
    body: Content,
    /,
    *,
    x: Auto | int = 'auto',
    y: Auto | int = 'auto',
    colspan: int = 1,
    rowspan: int = 1,
    fill: None | Auto | Color | Gradient | Tiling = 'auto',
    align: Auto | Alignment = 'auto',
    inset: Auto | Relative | BoxInset = 'auto',
    stroke: None | Length | Color | Gradient | Stroke | Tiling | RectangleStroke = {},
    breakable: Auto | bool = 'auto',
):
    """Interface of `grid.cell` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-cell) for more information.

    Args:
        body: The cell's body.
        x: The cell's column (zero-indexed). Defaults to 'auto'.
        y: The cell's row (zero-indexed). Defaults to 'auto'.
        colspan: The amount of columns spanned by this cell. Defaults to 1.
        rowspan: The amount of rows spanned by this cell. Defaults to 1.
        fill: The cell's fill override. Defaults to 'auto'.
        align: The cell's alignment override. Defaults to 'auto'.
        inset: The cell's inset override. Defaults to 'auto'.
        stroke: The cell's stroke override. Defaults to {}.
        breakable: Whether rows spanned by this cell can be placed in different pages. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> grid.cell(lorem(20), x=3, y=3)
        '#grid.cell(lorem(20), x: 3, y: 3)'
    """
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
    'grid.hline', 'https://typst.app/docs/reference/layout/grid/#definitions-hline'
)
def _grid_hline(
    *,
    y: Auto | int = 'auto',
    start: int = 0,
    end: None | int = None,
    stroke: None
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = '1pt + black',
    position: Alignment = 'top',
):
    """Interface of `grid.hline` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-hline) for more information.

    Args:
        y: The row above which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start: The column at which the horizontal line starts (zero-indexed, inclusive). Defaults to 0.
        end: The column before which the horizontal line ends (zero-indexed, exclusive). Defaults to None.
        stroke: The line's stroke. Defaults to '1pt + black'.
        position: The position at which the line is placed, given its row (y) - either top to draw above it or bottom to draw below it. Defaults to 'top'.

    Returns:
        Executable typst code.
    """
    return normal(
        _grid_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'grid.vline', 'https://typst.app/docs/reference/layout/grid/#definitions-vline'
)
def _grid_vline(
    *,
    x: Auto | int = 'auto',
    start: int = 0,
    end: None | int = None,
    stroke: None | Length | Color | Gradient | Stroke | Tiling = '1pt + black',
    position: Alignment = 'start',
):
    """Interface of `grid.vline` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-vline) for more information.

    Args:
        x: The column before which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start: The row at which the vertical line starts (zero-indexed, inclusive). Defaults to 0.
        end: The row on top of which the vertical line ends (zero-indexed, exclusive). Defaults to None.
        stroke: The line's stroke. Defaults to '1pt + black'.
        position: The position at which the line is placed, given its column (x) - either start to draw before it or end to draw after it. Defaults to 'start'.

    Returns:
        Executable typst code.
    """
    return normal(
        _grid_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'grid.header', 'https://typst.app/docs/reference/layout/grid/#definitions-header'
)
def _grid_header(*children: Content, repeat: bool = True):
    """Interface of `grid.header` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-header) for more information.

    Args:
        repeat: Whether this header should be repeated across pages. Defaults to True.

    Returns:
        Executable typst code.
    """
    return post_series(_grid_header, *children, repeat=repeat)


@implement(
    'grid.footer', 'https://typst.app/docs/reference/layout/grid/#definitions-footer'
)
def _grid_footer(*children: Content, repeat: bool = True):
    """Interface of `grid.footer` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-footer) for more information.

    Args:
        repeat: Whether this footer should be repeated across pages. Defaults to True.

    Returns:
        Executable typst code.
    """
    return post_series(_grid_footer, *children, repeat=repeat)


@attach_func(_grid_cell, 'cell')
@attach_func(_grid_hline, 'hline')
@attach_func(_grid_vline, 'vline')
@attach_func(_grid_header, 'header')
@attach_func(_grid_footer, 'footer')
@implement('grid', 'https://typst.app/docs/reference/layout/grid/')
def grid(
    *children: Content,
    columns: Auto | int | Relative | Fraction | Iterable[Relative | Fraction] = tuple(),
    rows: Auto | int | Relative | Fraction | Iterable[Relative | Fraction] = tuple(),
    gutter: Auto | int | Relative | Fraction | Iterable[Relative | Fraction] = tuple(),
    column_gutter: Auto
    | int
    | Relative
    | Fraction
    | Iterable[Relative | Fraction] = tuple(),
    row_gutter: Auto
    | int
    | Relative
    | Fraction
    | Iterable[Relative | Fraction] = tuple(),
    fill: None | Color | Gradient | Iterable[Color] | Tiling | Function = None,
    align: Auto | Iterable[Alignment] | Alignment | Function = 'auto',
    stroke: None
    | Length
    | Color
    | Gradient
    | Iterable[Stroke]
    | Stroke
    | Tiling
    | RectangleStroke
    | Function = None,
    inset: Relative | Iterable[Relative] | BoxInset | Function = {},
):
    """Interface of `grid` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/) for more information.

    Args:
        columns: The column sizes. Defaults to tuple().
        rows: The row sizes. Defaults to tuple().
        gutter: The gaps between rows and columns. Defaults to tuple().
        column_gutter: The gaps between columns. Defaults to tuple().
        row_gutter: The gaps between rows. Defaults to tuple().
        fill: How to fill the cells. Defaults to None.
        align: How to align the cells' content. Defaults to 'auto'.
        stroke: How to stroke the cells. Defaults to None.
        inset: How much to pad the cells' content. Defaults to {}.

    Returns:
        Executable typst code.

    Examples:
        >>> grid(lorem(20), lorem(20), lorem(20), align=('center',) * 3)
        '#grid(align: (center, center, center), lorem(20), lorem(20), lorem(20))'
    """
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


@implement('hide', 'https://typst.app/docs/reference/layout/hide/')
def hide(body: Content, /):
    """Interface of `hide` in typst. See [the documentation](https://typst.app/docs/reference/layout/hide/) for more information.

    Args:
        body: The content to hide.

    Returns:
        Executable typst code.

    Examples:
        >>> hide(lorem(20))
        '#hide(lorem(20))'
    """
    return normal(hide, body)


@implement('layout', 'https://typst.app/docs/reference/layout/layout/')
def layout(func: Function, /):
    """Interface of `layout` in typst. See [the documentation](https://typst.app/docs/reference/layout/layout/) for more information.

    Args:
        func: A function to call with the outer container's size.

    Returns:
        Executable typst code.
    """
    return normal(layout, func)


@implement('measure', 'https://typst.app/docs/reference/layout/measure/')
def measure(
    body: Content, /, *, width: Auto | Length = 'auto', height: Auto | Length = 'auto'
):
    """Interface of `measure` in typst. See [the documentation](https://typst.app/docs/reference/layout/measure/) for more information.

    Args:
        body: The content whose size to measure.
        width: The width available to layout the content. Defaults to 'auto'.
        height: The height available to layout the content. Defaults to 'auto'.

    Returns:
        Executable typst code.
    """
    return normal(measure, body, width=width, height=height)


@implement('move', 'https://typst.app/docs/reference/layout/move/')
def move(body: Content, /, *, dx: Relative = '0% + 0pt', dy: Relative = '0% + 0pt'):
    """Interface of `move` in typst. See [the documentation](https://typst.app/docs/reference/layout/move/) for more information.

    Args:
        body: The content to move.
        dx: The horizontal displacement of the content. Defaults to '0% + 0pt'.
        dy: The vertical displacement of the content. Defaults to '0% + 0pt'.

    Returns:
        Executable typst code.

    Examples:
        >>> move(lorem(20), dx='50% + 10pt', dy='10% + 5pt')
        '#move(lorem(20), dx: 50% + 10pt, dy: 10% + 5pt)'
    """
    return normal(move, body, dx=dx, dy=dy)


@implement('pad', 'https://typst.app/docs/reference/layout/pad/')
def pad(
    body: Content,
    /,
    *,
    left: Relative = '0% + 0pt',
    top: Relative = '0% + 0pt',
    right: Relative = '0% + 0pt',
    bottom: Relative = '0% + 0pt',
    x: Relative = '0% + 0pt',
    y: Relative = '0% + 0pt',
    rest: Relative = '0% + 0pt',
):
    """Interface of `pad` in typst. See [the documentation](https://typst.app/docs/reference/layout/pad/) for more information.

    Args:
        body: The content to pad at the sides.
        left: The padding at the left side. Defaults to '0% + 0pt'.
        top: The padding at the top side. Defaults to '0% + 0pt'.
        right: The padding at the right side. Defaults to '0% + 0pt'.
        bottom: The padding at the bottom side. Defaults to '0% + 0pt'.
        x: A shorthand to set left and right to the same value. Defaults to '0% + 0pt'.
        y: A shorthand to set top and bottom to the same value. Defaults to '0% + 0pt'.
        rest: A shorthand to set all four sides to the same value. Defaults to '0% + 0pt'.

    Returns:
        Executable typst code.

    Examples:
        >>> pad(
        ...     lorem(20),
        ...     left='4% + 0pt',
        ...     top='4% + 0pt',
        ...     right='4% + 0pt',
        ...     bottom='4% + 0pt',
        ... )
        '#pad(lorem(20), left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'
    """
    return normal(
        pad,
        body,
        left=left,
        top=top,
        right=right,
        bottom=bottom,
        x=x,
        y=y,
        rest=rest,
    )


@implement('page', 'https://typst.app/docs/reference/layout/page/')
def page(
    body: Content,
    /,
    *,
    paper: PaperSizes = '"a4"',
    width: Auto | Length = '595.28pt',
    height: Auto | Length = '841.89pt',
    flipped: bool = False,
    margin: Auto | Relative | PageMargin = 'auto',
    binding: Auto | Alignment = 'auto',
    columns: int = 1,
    fill: None | Auto | Color | Gradient | Tiling = 'auto',
    numbering: None | str | Function = None,
    number_align: Alignment = 'center + bottom',
    header: None | Auto | Content = 'auto',
    header_ascent: Relative = '30% + 0pt',
    footer: None | Auto | Content = 'auto',
    footer_ascent: Relative = '30% + 0pt',
    background: None | Content = None,
    foreground: None | Content = None,
):
    """Interface of `page` in typst. See [the documentation](https://typst.app/docs/reference/layout/page/) for more information.

    Args:
        body: The contents of the page(s).
        paper: A standard paper size to set width and height. Defaults to '"a4"'.
        width: The width of the page. Defaults to '595.28pt'.
        height: The height of the page. Defaults to '841.89pt'.
        flipped: Whether the page is flipped into landscape orientation. Defaults to False.
        margin: The page's margins. Defaults to 'auto'.
        binding: On which side the pages will be bound. Defaults to 'auto'.
        columns: How many columns the page has. Defaults to 1.
        fill: The page's background fill. Defaults to 'auto'.
        numbering: How to number the pages. Defaults to None.
        number_align: The alignment of the page numbering. Defaults to 'center + bottom'.
        header: The page's header. Defaults to 'auto'.
        header_ascent: The amount the header is raised into the top margin. Defaults to '30% + 0pt'.
        footer: The page's footer. Defaults to 'auto'.
        footer_ascent: The amount the footer is lowered into the bottom margin. Defaults to '30% + 0pt'.
        background: Content in the page's background. Defaults to None.
        foreground: Content in the page's foreground. Defaults to None.

    Raises:
        AssertionError: If `paper` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> page(lorem(20))
        '#page(lorem(20))'
        >>> page(lorem(20), paper='"a0"', width='8.5in', height='11in')
        '#page(lorem(20), paper: "a0", width: 8.5in, height: 11in)'
    """
    assert paper in VALID_PAPER_SIZES

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


@implement('pagebreak', 'https://typst.app/docs/reference/layout/pagebreak/')
def pagebreak(*, weak: bool = False, to: None | str = None):
    """Interface of `pagebreak` in typst. See [the documentation](https://typst.app/docs/reference/layout/pagebreak/) for more information.

    Args:
        weak: If true, the page break is skipped if the current page is already empty. Defaults to False.
        to: If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary. Defaults to None.

    Returns:
        Executable typst code.

    Examples:
        >>> pagebreak()
        '#pagebreak()'
        >>> pagebreak(weak=True)
        '#pagebreak(weak: true)'
        >>> pagebreak(to='"even"')
        '#pagebreak(to: "even")'
    """
    return normal(pagebreak, weak=weak, to=to)


@implement(
    'place.flush', 'https://typst.app/docs/reference/layout/place/#definitions-flush'
)
def _place_flush():
    """Interface of `place.flush` in typst. See [the documentation](https://typst.app/docs/reference/layout/place/#definitions-flush) for more information.

    Returns:
        Executable typst code.

    Examples:
        >>> place.flush()
        '#place.flush()'
    """
    return normal(_place_flush)


@attach_func(_place_flush, 'flush')
@implement('place', 'https://typst.app/docs/reference/layout/place/')
def place(
    body: Content,
    alignment: Auto | Alignment = 'start',
    /,
    *,
    scope: str = '"column"',
    float: bool = False,
    clearance: Length = '1.5em',
    dx: Relative = '0% + 0pt',
    dy: Relative = '0% + 0pt',
):
    """Interface of `place` in typst. See [the documentation](https://typst.app/docs/reference/layout/place/) for more information.

    Args:
        body: The content to place.
        alignment: Relative to which position in the parent container to place the content. Defaults to 'start'.
        scope: Relative to which containing scope something is placed. Defaults to '"column"'.
        float: Whether the placed element has floating layout. Defaults to False.
        clearance: The spacing between the placed element and other elements in a floating layout. Defaults to '1.5em'.
        dx: The horizontal displacement of the placed content. Defaults to '0% + 0pt'.
        dy: The vertical displacement of the placed content. Defaults to '0% + 0pt'.

    Returns:
        Executable typst code.

    Examples:
        >>> place(lorem(20))
        '#place(lorem(20))'
        >>> place(lorem(20), 'top')
        '#place(lorem(20), top)'
    """
    return normal(
        place,
        *([body] if alignment == 'start' else [body, alignment]),
        scope=scope,
        float=float,
        clearance=clearance,
        dx=dx,
        dy=dy,
    )


@implement('repeat', 'https://typst.app/docs/reference/layout/repeat/')
def repeat(body: Content, /, *, gap: Length = '0pt', justify: bool = True):
    """Interface of `repeat` in typst. See [the documentation](https://typst.app/docs/reference/layout/repeat/) for more information.

    Args:
        body: The content to repeat.
        gap: The gap between each instance of the body. Defaults to '0pt'.
        justify: Whether to increase the gap between instances to completely fill the available space. Defaults to True.

    Returns:
        Executable typst code.

    Examples:
        >>> repeat(lorem(20), gap='0.5em')
        '#repeat(lorem(20), gap: 0.5em)'
        >>> repeat(lorem(20), gap='0.5em', justify=False)
        '#repeat(lorem(20), gap: 0.5em, justify: false)'
    """
    return normal(repeat, body, gap=gap, justify=justify)


@implement('rotate', 'https://typst.app/docs/reference/layout/rotate/')
def rotate(
    body: Content,
    angle: Angle = '0deg',
    /,
    *,
    origin: Alignment = 'center + horizon',
    reflow: bool = False,
):
    """Interface of `rotate` in typst. See [the documentation](https://typst.app/docs/reference/layout/rotate/) for more information.

    Args:
        body: The content to rotate.
        angle: The amount of rotation. Defaults to '0deg'.
        origin: The origin of the rotation. Defaults to 'center + horizon'.
        reflow: Whether the rotation impacts the layout. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> rotate(lorem(20), '20deg')
        '#rotate(lorem(20), 20deg)'
        >>> rotate(lorem(20), '20deg', origin='left + horizon')
        '#rotate(lorem(20), 20deg, origin: left + horizon)'
    """
    return normal(
        rotate,
        *([body] if angle == '0deg' else [body, angle]),
        origin=origin,
        reflow=reflow,
    )


@implement('scale', 'https://typst.app/docs/reference/layout/scale/')
def scale(
    body: Content,
    factor: Auto | Length | Ratio = '100%',
    /,
    *,
    x: Auto | Length | Ratio = '100%',
    y: Auto | Length | Ratio = '100%',
    origin: Alignment = 'center + horizon',
    reflow: bool = False,
):
    """Interface of `scale` in typst. See [the documentation](https://typst.app/docs/reference/layout/scale/) for more information.

    Args:
        body: The content to scale.
        factor: The scaling factor for both axes, as a positional argument. Defaults to '100%'.
        x: The horizontal scaling factor. Defaults to '100%'.
        y: The vertical scaling factor. Defaults to '100%'.
        origin: The origin of the transformation. Defaults to 'center + horizon'.
        reflow: Whether the scaling impacts the layout. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> scale(lorem(20), '50%')
        '#scale(lorem(20), 50%)'
        >>> scale(lorem(20), x='50%', y='50%')
        '#scale(lorem(20), x: 50%, y: 50%)'
        >>> scale(lorem(20), '50%', x='50%', y='50%')
        '#scale(lorem(20), 50%, x: 50%, y: 50%)'
    """
    return normal(
        scale,
        *([body] if factor == '100%' else [body, factor]),
        x=x,
        y=y,
        origin=origin,
        reflow=reflow,
    )


@implement('skew', 'https://typst.app/docs/reference/layout/skew/')
def skew(
    body: Content,
    /,
    *,
    ax: Angle = '0deg',
    ay: Angle = '0deg',
    origin: Alignment = 'center + horizon',
    reflow: bool = False,
):
    """Interface of `skew` in typst. See [the documentation](https://typst.app/docs/reference/layout/skew/) for more information.

    Args:
        body: The content to skew.
        ax: The horizontal skewing angle. Defaults to '0deg'.
        ay: The vertical skewing angle. Defaults to '0deg'.
        origin: The origin of the skew transformation. Defaults to 'center + horizon'.
        reflow: Whether the skew transformation impacts the layout. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> skew(lorem(20), ax='10deg', ay='20deg')
        '#skew(lorem(20), ax: 10deg, ay: 20deg)'
    """
    return normal(skew, body, ax=ax, ay=ay, origin=origin, reflow=reflow)


@implement('h', 'https://typst.app/docs/reference/layout/h/')
def hspace(amount: Relative | Fraction, /, *, weak: bool = False):
    """Interface of `h` in typst. See [the documentation](https://typst.app/docs/reference/layout/h/) for more information.

    Args:
        amount: How much spacing to insert.
        weak: If true, the spacing collapses at the start or end of a paragraph. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> hspace('1em')
        '#h(1em)'
        >>> hspace('1em', weak=True)
        '#h(1em, weak: true)'
    """
    return normal(hspace, amount, weak=weak)


@implement('v', 'https://typst.app/docs/reference/layout/v/')
def vspace(amount: Relative | Fraction, /, *, weak: bool = False):
    """Interface of `v` in typst. See [the documentation](https://typst.app/docs/reference/layout/v/) for more information.

    Args:
        amount: How much spacing to insert.
        weak: If true, the spacing collapses at the start or end of a flow. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> vspace('1em')
        '#v(1em)'
        >>> vspace('1em', weak=True)
        '#v(1em, weak: true)'
    """
    return normal(vspace, amount, weak=weak)


@implement('stack', 'https://typst.app/docs/reference/layout/stack/')
def stack(
    *children: Relative | Fraction | Content,
    dir: Direction = 'ttb',
    spacing: None | Relative | Fraction = None,
):
    """Interface of `stack` in typst. See [the documentation](https://typst.app/docs/reference/layout/stack/) for more information.

    Args:
        dir: The direction along which the items are stacked. Defaults to 'ttb'.
        spacing: Spacing to insert between items where no explicit spacing was provided. Defaults to None.

    Returns:
        Executable typst code.

    Examples:
        >>> stack(rect(width='40pt'), rect(width='120pt'), rect(width='90pt'), dir='btt')
        '#stack(dir: btt, rect(width: 40pt), rect(width: 120pt), rect(width: 90pt))'
        >>> stack((rect(width='40pt'), rect(width='120pt'), rect(width='90pt')), dir='btt')
        '#stack(dir: btt, ..(rect(width: 40pt), rect(width: 120pt), rect(width: 90pt)))'
    """
    return post_series(stack, *children, dir=dir, spacing=spacing)


__all__ = [
    'align',
    'block',
    'box',
    'colbreak',
    'columns',
    'grid',
    'hide',
    'layout',
    'measure',
    'move',
    'pad',
    'page',
    'pagebreak',
    'place',
    'repeat',
    'rotate',
    'scale',
    'skew',
    'hspace',
    'vspace',
    'stack',
]
