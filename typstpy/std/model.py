from typing import Any, Iterable, Optional

from cytoolz.curried import map  # type:ignore

from .._utils import (
    attach_func,
    implement,
    is_valid,
    normal,
    pad,
    positional,
    post_series,
)
from ..typings import Block
from .visualize import image  # noqa

_VALID_STYLES = set(
    map(
        pad,
        (
            'annual-reviews',
            'pensoft',
            'annual-reviews-author-date',
            'the-lancet',
            'elsevier-with-titles',
            'gb-7714-2015-author-date',
            'royal-society-of-chemistry',
            'american-anthropological-association',
            'sage-vancouver',
            'british-medical-journal',
            'frontiers',
            'elsevier-harvard',
            'gb-7714-2005-numeric',
            'angewandte-chemie',
            'gb-7714-2015-note',
            'springer-basic-author-date',
            'trends',
            'american-geophysical-union',
            'american-political-science-association',
            'american-psychological-association',
            'cell',
            'spie',
            'harvard-cite-them-right',
            'american-institute-of-aeronautics-and-astronautics',
            'council-of-science-editors-author-date',
            'copernicus',
            'sist02',
            'springer-socpsych-author-date',
            'modern-language-association-8',
            'nature',
            'iso-690-numeric',
            'springer-mathphys',
            'springer-lecture-notes-in-computer-science',
            'future-science',
            'current-opinion',
            'deutsche-gesellschaft-für-psychologie',
            'american-meteorological-society',
            'modern-humanities-research-association',
            'american-society-of-civil-engineers',
            'chicago-notes',
            'institute-of-electrical-and-electronics-engineers',
            'deutsche-sprache',
            'gb-7714-2015-numeric',
            'bristol-university-press',
            'association-for-computing-machinery',
            'associacao-brasileira-de-normas-tecnicas',
            'american-medical-association',
            'elsevier-vancouver',
            'chicago-author-date',
            'vancouver',
            'chicago-fullnotes',
            'turabian-author-date',
            'springer-fachzeitschriften-medizin-psychologie',
            'thieme',
            'taylor-and-francis-national-library-of-medicine',
            'american-chemical-society',
            'american-institute-of-physics',
            'taylor-and-francis-chicago-author-date',
            'gost-r-705-2008-numeric',
            'institute-of-physics-numeric',
            'iso-690-author-date',
            'the-institution-of-engineering-and-technology',
            'american-society-for-microbiology',
            'multidisciplinary-digital-publishing-institute',
            'springer-basic',
            'springer-humanities-author-date',
            'turabian-fullnote-8',
            'karger',
            'springer-vancouver',
            'vancouver-superscript',
            'american-physics-society',
            'mary-ann-liebert-vancouver',
            'american-society-of-mechanical-engineers',
            'council-of-science-editors',
            'american-physiological-society',
            'future-medicine',
            'biomed-central',
            'public-library-of-science',
            'american-sociological-association',
            'modern-language-association',
            'alphanumeric',
            'ieee',
        ),
    )
)


@implement(
    True,
    original_name='bibliography',
    hyperlink='https://typst.app/docs/reference/model/bibliography/',
)
def bibliography(
    path: str | Iterable[str],
    /,
    *,
    title: str | None = 'auto',
    full: bool = False,
    style: str = '"ieee"',
) -> Block:
    """Interface of `bibliography` in typst. See [the documentation](https://typst.app/docs/reference/model/bibliography/) for more information.

    Args:
        path (str | Iterable[str]): Path(s) to Hayagriva .yml and/or BibLaTeX .bib files.
        title (str | None, optional): The title of the bibliography. Defaults to 'auto'.
        full (bool, optional): Whether to include all works from the given bibliography files, even those that weren't cited in the document. Defaults to False.
        style (str, optional): The bibliography style. Defaults to '"ieee"'.

    Raises:
        ValueError: If `style` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> bibliography('"bibliography.bib"', style='"cell"')
        '#bibliography("bibliography.bib", style: "cell")'
    """
    is_valid(lambda: style in _VALID_STYLES)
    return normal(
        bibliography,
        path,
        title=title,
        full=full,
        style=style,
    )


@implement(
    True,
    original_name='list.item',
    hyperlink='https://typst.app/docs/reference/model/list/#definitions-item',
)
def _bullet_list_item(body: str, /) -> Block:
    return normal(_bullet_list_item, body)


@attach_func(_bullet_list_item, 'item')
@implement(
    True, original_name='list', hyperlink='https://typst.app/docs/reference/model/list/'
)
def bullet_list(
    *children: str,
    tight: bool = True,
    marker: str | Iterable[str] = ('[•]', '[‣]', '[–]'),
    indent: str = '0pt',
    body_indent: str = '0.5em',
    spacing: str = 'auto',
) -> Block:
    return post_series(
        bullet_list,
        *children,
        tight=tight,
        marker=marker,
        indent=indent,
        body_indent=body_indent,
        spacing=spacing,
    )


@implement(
    True, original_name='cite', hyperlink='https://typst.app/docs/reference/model/cite/'
)
def cite(
    key: str,
    /,
    *,
    supplement: str | None = None,
    form: str | None = '"normal"',
    style: str = 'auto',
) -> Block:
    """Interface of `cite` in typst. See [the documentation](https://typst.app/docs/reference/model/cite/) for more information.

    Args:
        key (str): The citation key that identifies the entry in the bibliography that shall be cited, as a label.
        supplement (str | None, optional): A supplement for the citation such as page or chapter number. Defaults to None.
        form (str | None, optional): The kind of citation to produce. Defaults to '"normal"'.
        style (str, optional): The citation style. Defaults to 'auto'.

    Raises:
        ValueError: If `form` or `style` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> cite('<label>')
        '#cite(<label>)'
        >>> cite('<label>', supplement='[Hello, World!]')
        '#cite(<label>, supplement: [Hello, World!])'
        >>> cite('<label>', form='"prose"')
        '#cite(<label>, form: "prose")'
        >>> cite('<label>', style='"annual-reviews"')
        '#cite(<label>, style: "annual-reviews")'
    """
    is_valid(
        lambda: form is None
        or form in map(pad, ('normal', 'prose', 'full', 'author', 'year')),
        lambda: style == 'auto' or style in _VALID_STYLES,
    )
    return normal(
        cite,
        key,
        supplement=supplement,
        form=form,
        style=style,
    )


@implement(
    True,
    original_name='document',
    hyperlink='https://typst.app/docs/reference/model/document/',
)
def document(
    *,
    title: str | None = None,
    author: str | Iterable[str] = tuple(),
    keywords: str | Iterable[str] = tuple(),
    date: str | None = 'auto',
) -> Block:
    """Interface of `document` in typst. See [the documentation](https://typst.app/docs/reference/model/document/) for more information.

    Args:
        title (str | None, optional): The document's title. Defaults to None.
        author (str | Iterable[str], optional): The document's authors. Defaults to tuple().
        keywords (str | Iterable[str], optional): The document's keywords. Defaults to tuple().
        date (str | None, optional): The document's creation date. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.
    """
    return normal(document, title=title, author=author, keywords=keywords, date=date)


@implement(
    True, original_name='emph', hyperlink='https://typst.app/docs/reference/model/emph/'
)
def emph(body: str, /) -> Block:
    """Interface of `emph` in typst. See [the documentation](https://typst.app/docs/reference/model/emph/) for more information.

    Args:
        body (str): The content to emphasize.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> emph('"Hello, World!"')
        '#emph("Hello, World!")'
        >>> emph('[Hello, World!]')
        '#emph([Hello, World!])'
    """
    return normal(emph, body)


@implement(
    True,
    original_name='figure.caption',
    hyperlink='https://typst.app/docs/reference/model/figure/#definitions-caption',
)
def _figure_caption(
    body: str, /, *, position: str = 'bottom', separator: str = 'auto'
) -> Block:
    """Interface of `figure.caption` in typst. See [the documentation](https://typst.app/docs/reference/model/figure/#definitions-caption) for more information.

    Args:
        body (str): The caption's body.
        position (str, optional): The caption's position in the figure. Defaults to 'bottom'.
        separator (str, optional): The separator which will appear between the number and body. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> figure.caption('[Hello, World!]')
        '#figure.caption([Hello, World!])'
        >>> figure.caption('[Hello, World!]', position='top', separator='[---]')
        '#figure.caption([Hello, World!], position: top, separator: [---])'
    """
    return normal(_figure_caption, body, position=position, separator=separator)


@attach_func(_figure_caption, 'caption')
@implement(
    True,
    original_name='figure',
    hyperlink='https://typst.app/docs/reference/model/figure/',
)
def figure(
    body: str,
    /,
    *,
    placement: str | None = None,
    scope: str = '"column"',
    caption: str | None = None,
    kind: str = 'auto',
    supplement: str | None = 'auto',
    numbering: str | None = '"1"',
    gap: str = '0.65em',
    outlined: bool = True,
) -> Block:
    """Interface of `figure` in typst. See [the documentation](https://typst.app/docs/reference/model/figure/) for more information.

    Args:
        body (str): The content of the figure.
        placement (str | None, optional): The figure's placement on the page. Defaults to None.
        scope (str, optional): Relative to which containing scope the figure is placed. Defaults to '"column"'.
        caption (str | None, optional): The figure's caption. Defaults to None.
        kind (str, optional): The kind of figure this is. Defaults to 'auto'.
        supplement (str | None, optional): The figure's supplement. Defaults to 'auto'.
        numbering (str | None, optional): How to number the figure. Defaults to '"1"'.
        gap (str, optional): The vertical gap between the body and caption. Defaults to '0.65em'.
        outlined (bool, optional): Whether the figure should appear in an outline of figures. Defaults to True.

    Raises:
        ValueError: If `scope` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> figure(image('"image.png"'))
        '#figure(image("image.png"))'
        >>> figure(image('"image.png"'), caption='[Hello, World!]')
        '#figure(image("image.png"), caption: [Hello, World!])'
    """
    is_valid(lambda: scope in map(pad, ('column', 'parent')))
    return normal(
        figure,
        body,
        placement=placement,
        scope=scope,
        caption=caption,
        kind=kind,
        supplement=supplement,
        numbering=numbering,
        gap=gap,
        outlined=outlined,
    )


@implement(
    True,
    original_name='footnote.entry',
    hyperlink='https://typst.app/docs/reference/model/footnote/#definitions-entry',
)
def _footnote_entry(
    note: str,
    /,
    *,
    separator: str = 'line(length: 30% + 0pt, stroke: 0.5pt)',
    clearance: str = '1em',
    gap: str = '0.5em',
    indent: str = '1em',
) -> Block:  # TODO: Implement default value of `separator`.
    return normal(
        _footnote_entry,
        note,
        separator=separator,
        clearance=clearance,
        gap=gap,
        indent=indent,
    )


@attach_func(_footnote_entry, 'entry')
@implement(
    True,
    original_name='footnote',
    hyperlink='https://typst.app/docs/reference/model/footnote/',
)
def footnote(body: str, /, *, numbering: str = '"1"') -> Block:
    """Interface of `footnote` in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/) for more information.

    Args:
        body (str): The content to put into the footnote.
        numbering (str, optional): How to number footnotes. Defaults to '"1"'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> footnote('[Hello, World!]')
        '#footnote([Hello, World!])'
        >>> footnote('[Hello, World!]', numbering='"a"')
        '#footnote([Hello, World!], numbering: "a")'
    """
    return normal(footnote, body, numbering=numbering)


@implement(
    True,
    original_name='heading',
    hyperlink='https://typst.app/docs/reference/model/heading/',
)
def heading(
    body: str,
    /,
    *,
    level: str | int = 'auto',
    depth: int = 1,
    offset: int = 0,
    numbering: str | None = None,
    supplement: str | None = 'auto',
    outlined: bool = True,
    bookmarked: str | bool = 'auto',
    hanging_indent: str = 'auto',
) -> Block:
    return normal(
        heading,
        body,
        level=level,
        depth=depth,
        offset=offset,
        numbering=numbering,
        supplement=supplement,
        outlined=outlined,
        bookmarked=bookmarked,
        hanging_indent=hanging_indent,
    )


@implement(
    True,
    original_name='link',
    hyperlink='https://typst.app/docs/reference/model/link/',
)
def link(dest: str | dict[str, Any], body: Optional[str] = None, /) -> Block:
    """Interface of `link` in typst. See [the documentation](https://typst.app/docs/reference/model/link/) for more information.

    Args:
        dest (str | dict[str, Any]): The destination the link points to.
        body (Optional[str], optional): The content that should become a link. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> link('"https://typst.app"')
        '#link("https://typst.app")'
        >>> link('"https://typst.app"', '"Typst"')
        '#link("https://typst.app", "Typst")'
    """
    args = [dest]
    if body is not None:
        args.append(body)
    return positional(link, *args)


@implement(
    True,
    original_name='list.item',
    hyperlink='https://typst.app/docs/reference/model/list/#definitions-item',
)
def _numbered_list_item(body: str, /, *, number: int | None = None) -> Block:
    return normal(_numbered_list_item, body, number=number)


@attach_func(_numbered_list_item, 'item')
@implement(
    True,
    original_name='enum',
    hyperlink='https://typst.app/docs/reference/model/enum/',
)
def numbered_list(
    *children: str,
    tight: bool = True,
    numbering: str = '"1."',
    start: int = 1,
    full: bool = False,
    indent: str = '0pt',
    body_indent: str = '0.5em',
    spacing: str = 'auto',
    number_align: str = 'end + top',
) -> Block:
    return post_series(
        numbered_list,
        *children,
        tight=tight,
        numbering=numbering,
        start=start,
        full=full,
        indent=indent,
        body_indent=body_indent,
        spacing=spacing,
        number_align=number_align,
    )


@implement(
    True,
    original_name='numbering',
    hyperlink='https://typst.app/docs/reference/model/numbering/',
)
def numbering(numbering_: str, /, *numbers: int) -> Block:
    return normal(numbering, numbering_, *numbers)


@implement(
    True,
    original_name='outline.entry',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry',
)
def _outline_entry(
    level: int, element: str, body: str, fill: str | None, page: str, /
) -> Block:
    """Interface of `outline.entry` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry) for more information.

    Args:
        level (int): The nesting level of this outline entry.
        element (str): The element this entry refers to.
        body (str): The content which is displayed in place of the referred element at its entry in the outline.
        fill (str | None): The content used to fill the space between the element's outline and its page number, as defined by the outline element this entry is located in.
        page (str): The page number of the element this entry links to, formatted with the numbering set for the referenced page.

    Returns:
        Block: Executable typst code.
    """
    return positional(_outline_entry, level, element, body, fill, page)


@attach_func(_outline_entry, 'entry')
@implement(
    True,
    original_name='outline',
    hyperlink='https://typst.app/docs/reference/model/outline/',
)
def outline(
    *,
    title: str | None = 'auto',
    target: str = 'heading.where(outlined: true)',
    depth: int | None = None,
    indent: str | bool | None = None,
    fill: str | None = 'repeat(body: [.])',
) -> Block:  # TODO: Implement default value of `target` and `fill`.
    return normal(
        outline, title=title, target=target, depth=depth, indent=indent, fill=fill
    )


@implement(
    True,
    original_name='par.line',
    hyperlink='https://typst.app/docs/reference/model/par/#definitions-line',
)
def _par_line(
    *,
    numbering: str | None = None,
    number_align: str = 'auto',
    number_margin: str = 'start',
    number_clearance: str = 'auto',
    numbering_scope: str = '"document"',
) -> Block:
    return positional(
        _par_line,
        numbering,
        number_align,
        number_margin,
        number_clearance,
        numbering_scope,
    )


@attach_func(_par_line, 'line')
@implement(
    True,
    original_name='par',
    hyperlink='https://typst.app/docs/reference/model/par/',
)
def par(
    body: str,
    /,
    *,
    leading: str = '0.65em',
    spacing: str = '1.2em',
    justify: bool = False,
    linebreaks: str = 'auto',
    first_line_indent: str = '0pt',
    hanging_indent: str = '0pt',
) -> Block:
    """Interface of `par` in typst. See [the documentation](https://typst.app/docs/reference/model/par/) for more information.

    Args:
        body (str): The contents of the paragraph.
        leading (str, optional): The spacing between lines. Defaults to '0.65em'.
        spacing (str, optional): The spacing between paragraphs. Defaults to '1.2em'.
        justify (bool, optional): Whether to justify text in its line. Defaults to False.
        linebreaks (str, optional): How to determine line breaks. Defaults to 'auto'.
        first_line_indent (str, optional): The indent the first line of a paragraph should have. Defaults to '0pt'.
        hanging_indent (str, optional): The indent all but the first line of a paragraph should have. Defaults to '0pt'.

    Raises:
        ValueError: If `linebreaks` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> par('"Hello, World!"')
        '#par("Hello, World!")'
        >>> par('[Hello, World!]')
        '#par([Hello, World!])'
        >>> par(
        ...     '[Hello, World!]',
        ...     leading='0.1em',
        ...     spacing='0.5em',
        ...     justify=True,
        ...     linebreaks='"simple"',
        ...     first_line_indent='0.2em',
        ...     hanging_indent='0.3em',
        ... )
        '#par([Hello, World!], leading: 0.1em, spacing: 0.5em, justify: true, linebreaks: "simple", first-line-indent: 0.2em, hanging-indent: 0.3em)'
    """
    is_valid(
        lambda: linebreaks == 'auto' or linebreaks in map(pad, ['simple', 'optimized'])
    )
    return normal(
        par,
        body,
        leading=leading,
        spacing=spacing,
        justify=justify,
        linebreaks=linebreaks,
        first_line_indent=first_line_indent,
        hanging_indent=hanging_indent,
    )


@implement(
    True,
    original_name='parbreak',
    hyperlink='https://typst.app/docs/reference/model/parbreak/',
)
def parbreak() -> Block:
    """Interface of `parbreak` in typst. See [the documentation](https://typst.app/docs/reference/model/parbreak/) for more information.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> parbreak()
        '#parbreak()'
    """
    return normal(parbreak)


@implement(
    True,
    original_name='quote',
    hyperlink='https://typst.app/docs/reference/model/quote/',
)
def quote(
    body: str,
    /,
    *,
    block: bool = False,
    quotes: str | bool = 'auto',
    attribution: str | None = None,
) -> Block:
    """Interface of `quote` in typst. See [the documentation](https://typst.app/docs/reference/model/quote/) for more information.

    Args:
        body (str): The quote.
        block (bool, optional): Whether this is a block quote. Defaults to False.
        quotes (str | bool, optional): Whether double quotes should be added around this quote. Defaults to 'auto'.
        attribution (str | None, optional): The attribution of this quote, usually the author or source. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> quote('"Hello, World!"')
        '#quote("Hello, World!")'
        >>> quote('"Hello, World!"', block=True)
        '#quote("Hello, World!", block: true)'
        >>> quote('"Hello, World!"', quotes=False)
        '#quote("Hello, World!", quotes: false)'
        >>> quote('"Hello, World!"', attribution='"John Doe"')
        '#quote("Hello, World!", attribution: "John Doe")'
    """
    return normal(quote, body, block=block, quotes=quotes, attribution=attribution)


@implement(
    True,
    original_name='ref',
    hyperlink='https://typst.app/docs/reference/model/ref/',
)
def ref(target: str, /, *, supplement: str | None = 'auto') -> Block:
    """Interface of `ref` in typst. See [the documentation](https://typst.app/docs/reference/model/ref/) for more information.

    Args:
        target (str): The target label that should be referenced.
        supplement (str | None, optional): A supplement for the reference. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> ref('<label>')
        '#ref(<label>)'
        >>> ref('<label>', supplement='[Hello, World!]')
        '#ref(<label>, supplement: [Hello, World!])'
    """
    return normal(ref, target, supplement=supplement)


@implement(
    True,
    original_name='strong',
    hyperlink='https://typst.app/docs/reference/model/strong/',
)
def strong(body: str, /, *, delta: int = 300) -> Block:
    """Interface of `strong` in typst. See [the documentation](https://typst.app/docs/reference/model/strong/) for more information.

    Args:
        body (str): The content to strongly emphasize.
        delta (int, optional): The delta to apply on the font weight. Defaults to 300.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> strong('"Hello, World!"')
        '#strong("Hello, World!")'
        >>> strong('[Hello, World!]', delta=400)
        '#strong([Hello, World!], delta: 400)'
    """
    return normal(strong, body, delta=delta)


@implement(
    True,
    original_name='table.cell',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-cell',
)
def _table_cell(
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
        _table_cell,
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
    original_name='table.hline',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-hline',
)
def _table_hline(
    *,
    y: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'top',
) -> Block:
    return normal(
        _table_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    True,
    original_name='table.vline',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-vline',
)
def _table_vline(
    *,
    x: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'start',
) -> Block:
    return normal(
        _table_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    True,
    original_name='table.header',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-header',
)
def _table_header(*children: str, repeat: bool = True) -> Block:
    return post_series(_table_header, *children, repeat=repeat)


@implement(
    True,
    original_name='table.footer',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-footer',
)
def _table_footer(*children: str, repeat: bool = True) -> Block:
    return post_series(_table_footer, *children, repeat=repeat)


@attach_func(_table_cell, 'cell')
@attach_func(_table_hline, 'hline')
@attach_func(_table_vline, 'vline')
@attach_func(_table_header, 'header')
@attach_func(_table_footer, 'footer')
@implement(
    True,
    original_name='table',
    hyperlink='https://typst.app/docs/reference/model/table/',
)
def table(
    *children: str,
    columns: str | int | Iterable[str] = tuple(),
    rows: str | int | Iterable[str] = tuple(),
    gutter: str | int | Iterable[str] = tuple(),
    column_gutter: str | int | Iterable[str] = tuple(),
    row_gutter: str | int | Iterable[str] = tuple(),
    fill: str | Iterable[str] | None = None,
    align: str | Iterable[str] = 'auto',
    stroke: str | Iterable[str] | dict[str, Any] | None = '1pt + black',
    inset: str | Iterable[str] | dict[str, Any] = '0% + 5pt',
) -> Block:
    return post_series(
        table,
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
    original_name='terms.item',
    hyperlink='https://typst.app/docs/reference/model/terms/#definitions-item',
)
def _terms_item(term: str, description: str, /) -> Block:
    return positional(_terms_item, term, description)


@attach_func(_terms_item, 'item')
@implement(
    True,
    original_name='terms',
    hyperlink='https://typst.app/docs/reference/model/terms/',
)
def terms(
    *children: str,
    tight: bool = True,
    separator: str = 'h(amount: 0.6em, weak: true)',
    indent: str = '0pt',
    hanging_indent: str = '2em',
    spacing: str = 'auto',
) -> Block:  # TODO: Implement default value of `separator`.
    return post_series(
        terms,
        *children,
        tight=tight,
        separator=separator,
        indent=indent,
        hanging_indent=hanging_indent,
        spacing=spacing,
    )
