from typing import Any, Iterable

from cytoolz.curried import map  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from ..typings import Block
from ..utils import (
    attach_func,
    implement,
    is_valid,
    normal,
    pad,
    positional,
    post_series,
)
from .text import lorem  # noqa
from .visualize import rect  # noqa

_VALID_PAPER_SIZES = set(
    map(
        pad,
        (
            'a0',
            'a1',
            'a2',
            'a3',
            'a4',
            'a5',
            'a6',
            'a7',
            'a8',
            'a9',
            'a10',
            'a11',
            'iso-b1',
            'iso-b2',
            'iso-b3',
            'iso-b4',
            'iso-b5',
            'iso-b6',
            'iso-b7',
            'iso-b8',
            'iso-c3',
            'iso-c4',
            'iso-c5',
            'iso-c6',
            'iso-c7',
            'iso-c8',
            'din-d3',
            'din-d4',
            'din-d5',
            'din-d6',
            'din-d7',
            'din-d8',
            'sis-g5',
            'sis-e5',
            'ansi-a',
            'ansi-b',
            'ansi-c',
            'ansi-d',
            'ansi-e',
            'arch-a',
            'arch-b',
            'arch-c',
            'arch-d',
            'arch-e1',
            'arch-e',
            'jis-b0',
            'jis-b1',
            'jis-b2',
            'jis-b3',
            'jis-b4',
            'jis-b5',
            'jis-b6',
            'jis-b7',
            'jis-b8',
            'jis-b9',
            'jis-b10',
            'jis-b11',
            'sac-d0',
            'sac-d1',
            'sac-d2',
            'sac-d3',
            'sac-d4',
            'sac-d5',
            'sac-d6',
            'iso-id-1',
            'iso-id-2',
            'iso-id-3',
            'asia-f4',
            'jp-shiroku-ban-4',
            'jp-shiroku-ban-5',
            'jp-shiroku-ban-6',
            'jp-kiku-4',
            'jp-kiku-5',
            'jp-business-card',
            'cn-business-card',
            'eu-business-card',
            'fr-tellière',
            'fr-couronne-écriture',
            'fr-couronne-édition',
            'fr-raisin',
            'fr-carré',
            'fr-jésus',
            'uk-brief',
            'uk-draft',
            'uk-foolscap',
            'uk-quarto',
            'uk-crown',
            'uk-book-a',
            'uk-book-b',
            'us-letter',
            'us-legal',
            'us-tabloid',
            'us-executive',
            'us-foolscap-folio',
            'us-statement',
            'us-ledger',
            'us-oficio',
            'us-gov-letter',
            'us-gov-legal',
            'us-business-card',
            'us-digest',
            'us-trade',
            'newspaper-compact',
            'newspaper-berliner',
            'newspaper-broadsheet',
            'presentation-16-9',
            'presentation-4-3',
        ),
    )
)


@implement('align', 'https://typst.app/docs/reference/layout/align/')
def align(body: Block, alignment: str = 'start + top', /) -> Block:
    """Interface of `align` in typst. See [the documentation](https://typst.app/docs/reference/layout/align/) for more information.

    Args:
        body (str): The content to align.
        alignment (str, optional): The alignment along both axes. Defaults to 'start + top'.

    Returns:
        Block: Executable typst code.

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
        *Pipe([body])
        .map(lambda x: x + [alignment] if alignment != 'start + top' else x)
        .flush(),
    )


@implement('block', 'https://typst.app/docs/reference/layout/block/')
def block(
    body: str | None = '',
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
    """Interface of `block` in typst. See [the documentation](https://typst.app/docs/reference/layout/block/) for more information.

    Args:
        body (str | None, optional): The contents of the block. Defaults to ''.
        width (str, optional): The block's width. Defaults to 'auto'.
        height (str, optional): The block's height. Defaults to 'auto'.
        breakable (bool, optional): Whether the block can be broken and continue on the next page. Defaults to True.
        fill (str | None, optional): The block's background color. Defaults to None.
        stroke (str | dict[str, Any] | None, optional): The block's border color. Defaults to dict().
        radius (str | dict[str, Any], optional): How much to round the block's corners. Defaults to dict().
        inset (str | dict[str, Any], optional): How much to pad the block's content. Defaults to dict().
        outset (str | dict[str, Any], optional): How much to expand the block's size without affecting the layout. Defaults to dict().
        spacing (str, optional): The spacing around the block. Defaults to '1.2em'.
        above (str, optional): The spacing between this block and its predecessor. Defaults to 'auto'.
        below (str, optional): The spacing between this block and its successor. Defaults to 'auto'.
        clip (bool, optional): Whether to clip the content inside the block. Defaults to False.
        sticky (bool, optional): Whether this block must stick to the following one, with no break in between. Defaults to False.

    Returns:
        Block: Executable typst code.

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
    body: str | None = '',
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
    """Interface of `box` in typst. See [the documentation](https://typst.app/docs/reference/layout/box/) for more information.

    Args:
        body (str | None, optional): The contents of the box. Defaults to ''.
        width (str, optional): The width of the box. Defaults to 'auto'.
        height (str, optional): The height of the box. Defaults to 'auto'.
        baseline (str, optional): An amount to shift the box's baseline by. Defaults to '0% + 0pt'.
        fill (str | None, optional): The box's background color. Defaults to None.
        stroke (str | dict[str, Any] | None, optional): The box's border color. Defaults to dict().
        radius (str | dict[str, Any], optional): How much to round the box's corners. Defaults to dict().
        inset (str | dict[str, Any], optional): How much to pad the box's content. Defaults to dict().
        outset (str | dict[str, Any], optional): How much to expand the box's size without affecting the layout. Defaults to dict().
        clip (bool, optional): Whether to clip the content inside the box. Defaults to False.

    Returns:
        Block: Executable typst code.

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
def colbreak(*, weak: bool = False) -> Block:
    """Interface of `colbreak` in typst. See [the documentation](https://typst.app/docs/reference/layout/colbreak/) for more information.

    Args:
        weak (bool, optional): If true, the column break is skipped if the current column is already empty. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> colbreak()
        '#colbreak()'
        >>> colbreak(weak=True)
        '#colbreak(weak: true)'
    """
    return normal(colbreak, weak=weak)


@implement('columns', 'https://typst.app/docs/reference/layout/columns/')
def columns(body: str, count: int = 2, /, *, gutter: str = '4% + 0pt') -> Block:
    """Interface of `columns` in typst. See [the documentation](https://typst.app/docs/reference/layout/columns/) for more information.

    Args:
        body (str): The content that should be layouted into the columns.
        count (int, optional): The number of columns. Defaults to 2.
        gutter (str, optional): The size of the gutter space between each column. Defaults to '4% + 0pt'.

    Returns:
        Block: Executable typst code.

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
        *Pipe([body]).map(lambda x: x + [count] if count != 2 else x).flush(),
        gutter=gutter,
    )


@implement(
    'grid.cell', 'https://typst.app/docs/reference/layout/grid/#definitions-cell'
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
    """Interface of `grid.cell` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-cell) for more information.

    Args:
        body (str): The cell's body.
        x (str | int, optional): The cell's column (zero-indexed). Defaults to 'auto'.
        y (str | int, optional): The cell's row (zero-indexed). Defaults to 'auto'.
        colspan (int, optional): The amount of columns spanned by this cell. Defaults to 1.
        rowspan (int, optional): The amount of rows spanned by this cell. Defaults to 1.
        fill (str | None, optional): The cell's fill override. Defaults to 'auto'.
        align (str, optional): The cell's alignment override. Defaults to 'auto'.
        inset (str, optional): The cell's inset override. Defaults to 'auto'.
        stroke (str | dict[str, Any] | None, optional): The cell's stroke override. Defaults to dict().
        breakable (str | bool, optional): Whether rows spanned by this cell can be placed in different pages. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.
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
    y: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'top',
) -> Block:
    """Interface of `grid.hline` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-hline) for more information.

    Args:
        y (str | int, optional): The row above which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start (int, optional): The column at which the horizontal line starts (zero-indexed, inclusive). Defaults to 0.
        end (int | None, optional): The column before which the horizontal line ends (zero-indexed, exclusive). Defaults to None.
        stroke (str | dict[str, Any] | None, optional): The line's stroke. Defaults to '1pt + black'.
        position (str, optional): The position at which the line is placed, given its row (y) - either top to draw above it or bottom to draw below it. Defaults to 'top'.

    Returns:
        Block: Executable typst code.
    """
    return normal(
        _grid_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'grid.vline', 'https://typst.app/docs/reference/layout/grid/#definitions-vline'
)
def _grid_vline(
    *,
    x: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'start',
) -> Block:
    """Interface of `grid.vline` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-vline) for more information.

    Args:
        x (str | int, optional): The column before which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start (int, optional): The row at which the vertical line starts (zero-indexed, inclusive). Defaults to 0.
        end (int | None, optional): The row on top of which the vertical line ends (zero-indexed, exclusive). Defaults to None.
        stroke (str | dict[str, Any] | None, optional): The line's stroke. Defaults to '1pt + black'.
        position (str, optional): The position at which the line is placed, given its column (x) - either start to draw before it or end to draw after it. Defaults to 'start'.

    Returns:
        Block: Executable typst code.
    """
    return normal(
        _grid_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'grid.header', 'https://typst.app/docs/reference/layout/grid/#definitions-header'
)
def _grid_header(*children: str, repeat: bool = True) -> Block:
    """Interface of `grid.header` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-header) for more information.

    Args:
        repeat (bool, optional): Whether this header should be repeated across pages. Defaults to True.

    Returns:
        Block: Executable typst code.
    """
    return post_series(_grid_header, *children, repeat=repeat)


@implement(
    'grid.footer', 'https://typst.app/docs/reference/layout/grid/#definitions-footer'
)
def _grid_footer(*children: str, repeat: bool = True) -> Block:
    """Interface of `grid.footer` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/#definitions-footer) for more information.

    Args:
        repeat (bool, optional): Whether this footer should be repeated across pages. Defaults to True.

    Returns:
        Block: Executable typst code.
    """
    return post_series(_grid_footer, *children, repeat=repeat)


@attach_func(_grid_cell, 'cell')
@attach_func(_grid_hline, 'hline')
@attach_func(_grid_vline, 'vline')
@attach_func(_grid_header, 'header')
@attach_func(_grid_footer, 'footer')
@implement('grid', 'https://typst.app/docs/reference/layout/grid/')
def grid(
    *children: Block,
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
    """Interface of `grid` in typst. See [the documentation](https://typst.app/docs/reference/layout/grid/) for more information.

    Args:
        columns (str | int | Iterable[str], optional): The column sizes. Defaults to tuple().
        rows (str | int | Iterable[str], optional): The row sizes. Defaults to tuple().
        gutter (str | int | Iterable[str], optional): The gaps between rows and columns. Defaults to tuple().
        column_gutter (str | int | Iterable[str], optional): The gaps between columns. Defaults to tuple().
        row_gutter (str | int | Iterable[str], optional): The gaps between rows. Defaults to tuple().
        fill (str | Iterable[str] | None, optional): How to fill the cells. Defaults to None.
        align (str | Iterable[str], optional): How to align the cells' content. Defaults to 'auto'.
        stroke (str | Iterable[str] | dict[str, Any] | None, optional): How to stroke the cells. Defaults to None.
        inset (str | Iterable[str] | dict[str, Any], optional): How much to pad the cells' content. Defaults to dict().

    Returns:
        Block: Executable typst code.

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
def hide(body: str, /) -> Block:
    """Interface of `hide` in typst. See [the documentation](https://typst.app/docs/reference/layout/hide/) for more information.

    Args:
        body (str): The content to hide.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> hide(lorem(20))
        '#hide(lorem(20))'
    """
    return normal(hide, body)


@implement('layout', 'https://typst.app/docs/reference/layout/layout/')
def layout(func: str, /) -> Block:
    """Interface of `layout` in typst. See [the documentation](https://typst.app/docs/reference/layout/layout/) for more information.

    Args:
        func (str): A function to call with the outer container's size.

    Returns:
        Block: Executable typst code.
    """
    return normal(layout, func)


@implement('measure', 'https://typst.app/docs/reference/layout/measure/')
def measure(body: str, /, *, width: str = 'auto', height: str = 'auto') -> Block:
    """Interface of `measure` in typst. See [the documentation](https://typst.app/docs/reference/layout/measure/) for more information.

    Args:
        body (str): The content whose size to measure.
        width (str, optional): The width available to layout the content. Defaults to 'auto'.
        height (str, optional): The height available to layout the content. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.
    """
    return normal(measure, body, width=width, height=height)


@implement('move', 'https://typst.app/docs/reference/layout/move/')
def move(body: str, /, *, dx: str = '0% + 0pt', dy: str = '0% + 0pt') -> Block:
    """Interface of `move` in typst. See [the documentation](https://typst.app/docs/reference/layout/move/) for more information.

    Args:
        body (str): The content to move.
        dx (str, optional): The horizontal displacement of the content. Defaults to '0% + 0pt'.
        dy (str, optional): The vertical displacement of the content. Defaults to '0% + 0pt'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> move(lorem(20), dx='50% + 10pt', dy='10% + 5pt')
        '#move(lorem(20), dx: 50% + 10pt, dy: 10% + 5pt)'
    """
    return normal(move, body, dx=dx, dy=dy)


@implement('pad', 'https://typst.app/docs/reference/layout/pad/')
def padding(
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
    """Interface of `pad` in typst. See [the documentation](https://typst.app/docs/reference/layout/pad/) for more information.

    Args:
        body (str): The content to pad at the sides.
        left (str, optional): The padding at the left side. Defaults to '0% + 0pt'.
        top (str, optional): The padding at the top side. Defaults to '0% + 0pt'.
        right (str, optional): The padding at the right side. Defaults to '0% + 0pt'.
        bottom (str, optional): The padding at the bottom side. Defaults to '0% + 0pt'.
        x (str, optional): A shorthand to set left and right to the same value. Defaults to '0% + 0pt'.
        y (str, optional): A shorthand to set top and bottom to the same value. Defaults to '0% + 0pt'.
        rest (str, optional): A shorthand to set all four sides to the same value. Defaults to '0% + 0pt'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> padding(
        ...     lorem(20),
        ...     left='4% + 0pt',
        ...     top='4% + 0pt',
        ...     right='4% + 0pt',
        ...     bottom='4% + 0pt',
        ... )
        '#pad(lorem(20), left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'
    """
    return normal(
        padding,
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
    number_align: str = 'center + bottom',
    header: str | None = 'auto',
    header_ascent: str = '30% + 0pt',
    footer: str | None = 'auto',
    footer_ascent: str = '30% + 0pt',
    background: str | None = None,
    foreground: str | None = None,
) -> Block:
    """Interface of `page` in typst. See [the documentation](https://typst.app/docs/reference/layout/page/) for more information.

    Args:
        body (str): The contents of the page(s).
        paper (str, optional): A standard paper size to set width and height. Defaults to '"a4"'.
        width (str, optional): The width of the page. Defaults to '595.28pt'.
        height (str, optional): The height of the page. Defaults to '841.89pt'.
        flipped (bool, optional): Whether the page is flipped into landscape orientation. Defaults to False.
        margin (str | dict[str, Any], optional): The page's margins. Defaults to 'auto'.
        binding (str, optional): On which side the pages will be bound. Defaults to 'auto'.
        columns (int, optional): How many columns the page has. Defaults to 1.
        fill (str | None, optional): The page's background fill. Defaults to 'auto'.
        numbering (str | None, optional): How to number the pages. Defaults to None.
        number_align (str, optional): The alignment of the page numbering. Defaults to 'center + bottom'.
        header (str | None, optional): The page's header. Defaults to 'auto'.
        header_ascent (str, optional): The amount the header is raised into the top margin. Defaults to '30% + 0pt'.
        footer (str | None, optional): The page's footer. Defaults to 'auto'.
        footer_ascent (str, optional): The amount the footer is lowered into the bottom margin. Defaults to '30% + 0pt'.
        background (str | None, optional): Content in the page's background. Defaults to None.
        foreground (str | None, optional): Content in the page's foreground. Defaults to None.

    Raises:
        ValueError: If `paper` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> page(lorem(20))
        '#page(lorem(20))'
        >>> page(lorem(20), paper='"a0"', width='8.5in', height='11in')
        '#page(lorem(20), paper: "a0", width: 8.5in, height: 11in)'
    """
    is_valid(lambda: paper in _VALID_PAPER_SIZES)
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
def pagebreak(*, weak: bool = False, to: str | None = None) -> Block:
    """Interface of `pagebreak` in typst. See [the documentation](https://typst.app/docs/reference/layout/pagebreak/) for more information.

    Args:
        weak (bool, optional): If true, the page break is skipped if the current page is already empty. Defaults to False.
        to (str | None, optional): If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary. Defaults to None.

    Returns:
        Block: Executable typst code.

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
def _place_flush() -> Block:
    """Interface of `place.flush` in typst. See [the documentation](https://typst.app/docs/reference/layout/place/#definitions-flush) for more information.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> place.flush()
        '#place.flush()'
    """
    return normal(_place_flush)


@attach_func(_place_flush, 'flush')
@implement('place', 'https://typst.app/docs/reference/layout/place/')
def place(
    body: str,
    alignment: str = 'start',
    /,
    *,
    scope: str = '"column"',
    float: bool = False,
    clearance: str = '1.5em',
    dx: str = '0% + 0pt',
    dy: str = '0% + 0pt',
) -> Block:
    """Interface of `place` in typst. See [the documentation](https://typst.app/docs/reference/layout/place/) for more information.

    Args:
        body (str): The content to place.
        alignment (str, optional): Relative to which position in the parent container to place the content. Defaults to 'start'.
        scope (str, optional): Relative to which containing scope something is placed. Defaults to '"column"'.
        float (bool, optional): Whether the placed element has floating layout. Defaults to False.
        clearance (str, optional): The spacing between the placed element and other elements in a floating layout. Defaults to '1.5em'.
        dx (str, optional): The horizontal displacement of the placed content. Defaults to '0% + 0pt'.
        dy (str, optional): The vertical displacement of the placed content. Defaults to '0% + 0pt'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> place(lorem(20))
        '#place(lorem(20))'
        >>> place(lorem(20), 'top')
        '#place(lorem(20), top)'
    """
    return normal(
        place,
        *Pipe([body])
        .map(lambda x: x + [alignment] if alignment != 'start' else x)
        .flush(),
        scope=scope,
        float=float,
        clearance=clearance,
        dx=dx,
        dy=dy,
    )


@implement('repeat', 'https://typst.app/docs/reference/layout/repeat/')
def repeat(body: str, /, *, gap: str = '0pt', justify: bool = True) -> Block:
    """Interface of `repeat` in typst. See [the documentation](https://typst.app/docs/reference/layout/repeat/) for more information.

    Args:
        body (str): The content to repeat.
        gap (str, optional): The gap between each instance of the body. Defaults to '0pt'.
        justify (bool, optional): Whether to increase the gap between instances to completely fill the available space. Defaults to True.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> repeat(lorem(20), gap='0.5em')
        '#repeat(lorem(20), gap: 0.5em)'
        >>> repeat(lorem(20), gap='0.5em', justify=False)
        '#repeat(lorem(20), gap: 0.5em, justify: false)'
    """
    return normal(repeat, body, gap=gap, justify=justify)


@implement('rotate', 'https://typst.app/docs/reference/layout/rotate/')
def rotate(
    body: str,
    angle: str = '0deg',
    /,
    *,
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

    Examples:
        >>> rotate(lorem(20), '20deg')
        '#rotate(lorem(20), 20deg)'
        >>> rotate(lorem(20), '20deg', origin='left + horizon')
        '#rotate(lorem(20), 20deg, origin: left + horizon)'
    """
    return normal(
        rotate,
        *Pipe([body]).map(lambda x: x + [angle] if angle != '0deg' else x).flush(),
        origin=origin,
        reflow=reflow,
    )


@implement('scale', 'https://typst.app/docs/reference/layout/scale/')
def scale(
    body: str,
    factor: str = '100%',
    /,
    *,
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
        *Pipe([body]).map(lambda x: x + [factor] if factor != '100%' else x).flush(),
        x=x,
        y=y,
        origin=origin,
        reflow=reflow,
    )


@implement('skew', 'https://typst.app/docs/reference/layout/skew/')
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

    Examples:
        >>> skew(lorem(20), ax='10deg', ay='20deg')
        '#skew(lorem(20), ax: 10deg, ay: 20deg)'
    """
    return normal(skew, body, ax=ax, ay=ay, origin=origin, reflow=reflow)


@implement('h', 'https://typst.app/docs/reference/layout/h/')
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


@implement('v', 'https://typst.app/docs/reference/layout/v/')
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


@implement('stack', 'https://typst.app/docs/reference/layout/stack/')
def stack(*children: str, dir: str = 'ttb', spacing: str | None = None) -> Block:
    """Interface of `stack` in typst. See [the documentation](https://typst.app/docs/reference/layout/stack/) for more information.

    Args:
        dir (str, optional): The direction along which the items are stacked. Defaults to 'ttb'.
        spacing (str | None, optional): Spacing to insert between items where no explicit spacing was provided. Defaults to None.

    Returns:
        Block: Executable typst code.

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
    'padding',
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
