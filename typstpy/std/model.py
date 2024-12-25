from typing import Any, Iterable, Optional

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
from .layout import hspace, repeat  # noqa
from .text import lorem  # noqa
from .visualize import image, line  # noqa

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


@implement('bibliography', 'https://typst.app/docs/reference/model/bibliography/')
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


@implement('list.item', 'https://typst.app/docs/reference/model/list/#definitions-item')
def _bullet_list_item(body: str, /) -> Block:
    """Interface of `list.item` in typst. See [the documentation](https://typst.app/docs/reference/model/list/#definitions-item) for more information.

    Args:
        body (str): The item's body.

    Returns:
        Block: Executable typst code.
    """
    return normal(_bullet_list_item, body)


@attach_func(_bullet_list_item, 'item')
@implement('list', 'https://typst.app/docs/reference/model/list/')
def bullet_list(
    *children: str,
    tight: bool = True,
    marker: str | Iterable[str] = ('[•]', '[‣]', '[–]'),
    indent: str = '0pt',
    body_indent: str = '0.5em',
    spacing: str = 'auto',
) -> Block:
    """Interface of `list` in typst. See [the documentation](https://typst.app/docs/reference/model/list/) for more information.

    Args:
        tight (bool, optional): Defines the default spacing of the list. Defaults to True.
        marker (str | Iterable[str], optional): The marker which introduces each item. Defaults to ('[•]', '[‣]', '[–]').
        indent (str, optional): The indent of each item. Defaults to '0pt'.
        body_indent (str, optional): The spacing between the marker and the body of each item. Defaults to '0.5em'.
        spacing (str, optional): The spacing between the items of the list. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> bullet_list(lorem(20), lorem(20), lorem(20))
        '#list(lorem(20), lorem(20), lorem(20))'
        >>> bullet_list(lorem(20), lorem(20), lorem(20), tight=False)
        '#list(tight: false, lorem(20), lorem(20), lorem(20))'
    """
    return post_series(
        bullet_list,
        *children,
        tight=tight,
        marker=marker,
        indent=indent,
        body_indent=body_indent,
        spacing=spacing,
    )


@implement('cite', 'https://typst.app/docs/reference/model/cite/')
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


@implement('document', 'https://typst.app/docs/reference/model/document/')
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


@implement('emph', 'https://typst.app/docs/reference/model/emph/')
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
    'figure.caption',
    'https://typst.app/docs/reference/model/figure/#definitions-caption',
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
@implement('figure', 'https://typst.app/docs/reference/model/figure/')
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
    'footnote.entry',
    'https://typst.app/docs/reference/model/footnote/#definitions-entry',
)
def _footnote_entry(
    note: str,
    /,
    *,
    separator: str = line(length='30% + 0pt', stroke='0.5pt'),
    clearance: str = '1em',
    gap: str = '0.5em',
    indent: str = '1em',
) -> Block:
    """Interface of `footnote.entry` in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/#definitions-entry) for more information.

    Args:
        note (str): The footnote for this entry.
        separator (str, optional): The separator between the document body and the footnote listing. Defaults to line(length='30% + 0pt', stroke='0.5pt').
        clearance (str, optional): The amount of clearance between the document body and the separator. Defaults to '1em'.
        gap (str, optional): The gap between footnote entries. Defaults to '0.5em'.
        indent (str, optional): The indent of each footnote entry. Defaults to '1em'.

    Returns:
        Block: Executable typst code.
    """
    return normal(
        _footnote_entry,
        note,
        separator=separator,
        clearance=clearance,
        gap=gap,
        indent=indent,
    )


@attach_func(_footnote_entry, 'entry')
@implement('footnote', 'https://typst.app/docs/reference/model/footnote/')
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


@implement('heading', 'https://typst.app/docs/reference/model/heading/')
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
    """Interface of `heading` in typst. See [the documentation](https://typst.app/docs/reference/model/heading/) for more information.

    Args:
        body (str): The heading's title.
        level (str | int, optional): The absolute nesting depth of the heading, starting from one. Defaults to 'auto'.
        depth (int, optional): The relative nesting depth of the heading, starting from one. Defaults to 1.
        offset (int, optional): The starting offset of each heading's level, used to turn its relative depth into its absolute level. Defaults to 0.
        numbering (str | None, optional): How to number the heading. Defaults to None.
        supplement (str | None, optional): A supplement for the heading. Defaults to 'auto'.
        outlined (bool, optional): Whether the heading should appear in the outline. Defaults to True.
        bookmarked (str | bool, optional): Whether the heading should appear as a bookmark in the exported PDF's outline. Defaults to 'auto'.
        hanging_indent (str, optional): The indent all but the first line of a heading should have. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> heading('[Hello, World!]')
        '#heading([Hello, World!])'
        >>> heading('[Hello, World!]', level=1)
        '#heading([Hello, World!], level: 1)'
        >>> heading('[Hello, World!]', level=1, depth=2)
        '#heading([Hello, World!], level: 1, depth: 2)'
        >>> heading('[Hello, World!]', level=1, depth=2, offset=10)
        '#heading([Hello, World!], level: 1, depth: 2, offset: 10)'
        >>> heading('[Hello, World!]', level=1, depth=2, offset=10, numbering='"a"')
        '#heading([Hello, World!], level: 1, depth: 2, offset: 10, numbering: "a")'
        >>> heading(
        ...     '[Hello, World!]',
        ...     level=1,
        ...     depth=2,
        ...     offset=10,
        ...     numbering='"a"',
        ...     supplement='"Supplement"',
        ... )
        '#heading([Hello, World!], level: 1, depth: 2, offset: 10, numbering: "a", supplement: "Supplement")'
    """
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


@implement('link', 'https://typst.app/docs/reference/model/link/')
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
    return positional(
        link, *Pipe([dest]).map(lambda x: x + [body] if body else x).flush()
    )


@implement('enum.item', 'https://typst.app/docs/reference/model/enum/#definitions-item')
def _numbered_list_item(body: str, /, *, number: int | None = None) -> Block:
    """Interface of `enum.item` in typst. See [the documentation](https://typst.app/docs/reference/model/enum/#definitions-item) for more information.

    Args:
        body (str): The item's body.
        number (int | None, optional): The item's number. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> numbered_list.item('[Hello, World!]', number=2)
        '#enum.item([Hello, World!], number: 2)'
    """
    return normal(_numbered_list_item, body, number=number)


@attach_func(_numbered_list_item, 'item')
@implement('enum', 'https://typst.app/docs/reference/model/enum/')
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
    """Interface of `enum` in typst. See [the documentation](https://typst.app/docs/reference/model/enum/) for more information.

    Args:
        tight (bool, optional): Defines the default spacing of the enumeration. Defaults to True.
        numbering (str, optional): How to number the enumeration. Defaults to '"1."'.
        start (int, optional): Which number to start the enumeration with. Defaults to 1.
        full (bool, optional): Whether to display the full numbering, including the numbers of all parent enumerations. Defaults to False.
        indent (str, optional): The indentation of each item. Defaults to '0pt'.
        body_indent (str, optional): The space between the numbering and the body of each item. Defaults to '0.5em'.
        spacing (str, optional): The spacing between the items of the enumeration. Defaults to 'auto'.
        number_align (str, optional): The alignment that enum numbers should have. Defaults to 'end + top'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> numbered_list(lorem(20), lorem(20), lorem(20))
        '#enum(lorem(20), lorem(20), lorem(20))'
        >>> numbered_list(lorem(20), lorem(20), lorem(20), tight=False)
        '#enum(tight: false, lorem(20), lorem(20), lorem(20))'
    """
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


@implement('numbering', 'https://typst.app/docs/reference/model/numbering/')
def numbering(numbering_: str, /, *numbers: int) -> Block:
    """Interface of `numbering` in typst. See [the documentation](https://typst.app/docs/reference/model/numbering/) for more information.

    Args:
        numbering_ (str): Defines how the numbering works.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> numbering('"1.1)"', 1, 2)
        '#numbering("1.1)", 1, 2)'
    """
    return normal(numbering, numbering_, *numbers)


@implement(
    'outline.entry', 'https://typst.app/docs/reference/model/outline/#definitions-entry'
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
@implement('outline', 'https://typst.app/docs/reference/model/outline/')
def outline(
    *,
    title: str | None = 'auto',
    target: str = heading.where(outlined=True),  # type: ignore
    depth: int | None = None,
    indent: str | bool | None = None,
    fill: str | None = repeat('[.]'),
) -> Block:
    """Interface of `outline` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/) for more information.

    Args:
        title (str | None, optional): The title of the outline. Defaults to 'auto'.
        target (str, optional): The type of element to include in the outline. Defaults to heading.where(outlined=True).
        depth (int | None, optional): The maximum level up to which elements are included in the outline. Defaults to None.
        indent (str | bool | None, optional): How to indent the outline's entries. Defaults to None.
        fill (str | None, optional): Content to fill the space between the title and the page number. Defaults to repeat('[.]').

    Returns:
        Block: Executable typst code.

    Examples:
        >>> outline()
        '#outline()'
        >>> outline(title='"Hello, World!"', target=heading.where(outlined=False))
        '#outline(title: "Hello, World!", target: heading.where(outlined: false))'
    """
    return normal(
        outline, title=title, target=target, depth=depth, indent=indent, fill=fill
    )


@implement('par.line', 'https://typst.app/docs/reference/model/par/#definitions-line')
def _par_line(
    *,
    numbering: str | None = None,
    number_align: str = 'auto',
    number_margin: str = 'start',
    number_clearance: str = 'auto',
    numbering_scope: str = '"document"',
) -> Block:
    """Interface of `par.line` in typst. See [the documentation](https://typst.app/docs/reference/model/par/#definitions-line) for more information.

    Args:
        numbering (str | None, optional): How to number each line. Defaults to None.
        number_align (str, optional): The alignment of line numbers associated with each line. Defaults to 'auto'.
        number_margin (str, optional): The margin at which line numbers appear. Defaults to 'start'.
        number_clearance (str, optional): The distance between line numbers and text. Defaults to 'auto'.
        numbering_scope (str, optional): Controls when to reset line numbering. Defaults to '"document"'.

    Raises:
        ValueError: If `numbering_scope` is invalid.

    Returns:
        Block: Executable typst code.
    """
    is_valid(lambda: numbering_scope in map(pad, ('"document"', '"page"')))
    return positional(
        _par_line,
        numbering,
        number_align,
        number_margin,
        number_clearance,
        numbering_scope,
    )


@attach_func(_par_line, 'line')
@implement('par', 'https://typst.app/docs/reference/model/par/')
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


@implement('parbreak', 'https://typst.app/docs/reference/model/parbreak/')
def parbreak() -> Block:
    """Interface of `parbreak` in typst. See [the documentation](https://typst.app/docs/reference/model/parbreak/) for more information.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> parbreak()
        '#parbreak()'
    """
    return normal(parbreak)


@implement('quote', 'https://typst.app/docs/reference/model/quote/')
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


@implement('ref', 'https://typst.app/docs/reference/model/ref/')
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


@implement('strong', 'https://typst.app/docs/reference/model/strong/')
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
    'table.cell', 'https://typst.app/docs/reference/model/table/#definitions-cell'
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
    """Interface of `table.cell` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-cell) for more information.

    Args:
        body (str): The cell's body.
        x (str | int, optional): The cell's column (zero-indexed). Defaults to 'auto'.
        y (str | int, optional): The cell's row (zero-indexed). Defaults to 'auto'.
        colspan (int, optional): The amount of columns spanned by this cell. Defaults to 1.
        rowspan (int, optional): The cell's fill override. Defaults to 1.
        fill (str | None, optional): The amount of rows spanned by this cell. Defaults to 'auto'.
        align (str, optional): The cell's alignment override. Defaults to 'auto'.
        inset (str, optional): The cell's inset override. Defaults to 'auto'.
        stroke (str | dict[str, Any] | None, optional): The cell's stroke override. Defaults to dict().
        breakable (str | bool, optional): Whether rows spanned by this cell can be placed in different pages. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.
    """
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
    'table.hline', 'https://typst.app/docs/reference/model/table/#definitions-hline'
)
def _table_hline(
    *,
    y: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'top',
) -> Block:
    """Interface of `table.hline` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-hline) for more information.

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
        _table_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'table.vline', 'https://typst.app/docs/reference/model/table/#definitions-vline'
)
def _table_vline(
    *,
    x: str | int = 'auto',
    start: int = 0,
    end: int | None = None,
    stroke: str | dict[str, Any] | None = '1pt + black',
    position: str = 'start',
) -> Block:
    """Interface of `table.vline` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-vline) for more information.

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
        _table_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


@implement(
    'table.header', 'https://typst.app/docs/reference/model/table/#definitions-header'
)
def _table_header(*children: str, repeat: bool = True) -> Block:
    """Interface of `table.header` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-header) for more information.

    Args:
        repeat (bool, optional): Whether this header should be repeated across pages. Defaults to True.

    Returns:
        Block: Executable typst code.
    """
    return post_series(_table_header, *children, repeat=repeat)


@implement(
    'table.footer', 'https://typst.app/docs/reference/model/table/#definitions-footer'
)
def _table_footer(*children: str, repeat: bool = True) -> Block:
    """Interface of `table.footer` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-footer) for more information.

    Args:
        repeat (bool, optional): Whether this footer should be repeated across pages. Defaults to True.

    Returns:
        Block: Executable typst code.
    """
    return post_series(_table_footer, *children, repeat=repeat)


@attach_func(_table_cell, 'cell')
@attach_func(_table_hline, 'hline')
@attach_func(_table_vline, 'vline')
@attach_func(_table_header, 'header')
@attach_func(_table_footer, 'footer')
@implement('table', 'https://typst.app/docs/reference/model/table/')
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
    """Interface of `table` in typst. See [the documentation](https://typst.app/docs/reference/model/table/) for more information.

    Args:
        columns (str | int | Iterable[str], optional): The column sizes. Defaults to tuple().
        rows (str | int | Iterable[str], optional): The row sizes. Defaults to tuple().
        gutter (str | int | Iterable[str], optional): The gaps between rows and columns. Defaults to tuple().
        column_gutter (str | int | Iterable[str], optional): The gaps between columns. Defaults to tuple().
        row_gutter (str | int | Iterable[str], optional): The gaps between rows. Defaults to tuple().
        fill (str | Iterable[str] | None, optional): How to fill the cells. Defaults to None.
        align (str | Iterable[str], optional): How to align the cells' content. Defaults to 'auto'.
        stroke (str | Iterable[str] | dict[str, Any] | None, optional): How to stroke the cells. Defaults to '1pt + black'.
        inset (str | Iterable[str] | dict[str, Any], optional): How much to pad the cells' content. Defaults to '0% + 5pt'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> table('[1]', '[2]', '[3]')
        '#table([1], [2], [3])'
        >>> table(
        ...     '[1]',
        ...     '[2]',
        ...     '[3]',
        ...     columns=['1fr', '2fr', '3fr'],
        ...     rows=['1fr', '2fr', '3fr'],
        ...     gutter=['1fr', '2fr', '3fr'],
        ...     column_gutter=['1fr', '2fr', '3fr'],
        ...     row_gutter=['1fr', '2fr', '3fr'],
        ...     fill='red',
        ...     align=['center', 'center', 'center'],
        ... )
        '#table(columns: (1fr, 2fr, 3fr), rows: (1fr, 2fr, 3fr), gutter: (1fr, 2fr, 3fr), column-gutter: (1fr, 2fr, 3fr), row-gutter: (1fr, 2fr, 3fr), fill: red, align: (center, center, center), [1], [2], [3])'
    """
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
    'terms.item', 'https://typst.app/docs/reference/model/terms/#definitions-item'
)
def _terms_item(term: str, description: str, /) -> Block:
    """Interface of `terms.item` in typst. See [the documentation](https://typst.app/docs/reference/model/terms/#definitions-item) for more information.

    Args:
        term (str): The term described by the list item.
        description (str): The description of the term.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> terms.item('"term"', '"description"')
        '#terms.item("term", "description")'
    """
    return positional(_terms_item, term, description)


@attach_func(_terms_item, 'item')
@implement('terms', 'https://typst.app/docs/reference/model/terms/')
def terms(
    *children: tuple[str, str] | str,
    tight: bool = True,
    separator: str = hspace('0.6em', weak=True),
    indent: str = '0pt',
    hanging_indent: str = '2em',
    spacing: str = 'auto',
) -> Block:
    """Interface of `terms` in typst. See [the documentation](https://typst.app/docs/reference/model/terms/) for more information.

    Args:
        tight (bool, optional): Defines the default spacing of the term list. Defaults to True.
        separator (str, optional): The separator between the item and the description. Defaults to hspace('0.6em', weak=True).
        indent (str, optional): The indentation of each item. Defaults to '0pt'.
        hanging_indent (str, optional): The hanging indent of the description. Defaults to '2em'.
        spacing (str, optional): The spacing between the items of the term list. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> terms(('[1]', lorem(20)), ('[1]', lorem(20)))
        '#terms(([1], lorem(20)), ([1], lorem(20)))'
        >>> terms(('[1]', lorem(20)), ('[1]', lorem(20)), tight=False)
        '#terms(tight: false, ([1], lorem(20)), ([1], lorem(20)))'
        >>> terms(terms.item('[1]', lorem(20)), terms.item('[1]', lorem(20)))
        '#terms(terms.item([1], lorem(20)), terms.item([1], lorem(20)))'
    """
    return post_series(
        terms,
        *children,
        tight=tight,
        separator=separator,
        indent=indent,
        hanging_indent=hanging_indent,
        spacing=spacing,
    )


__all__ = [
    'bibliography',
    'bullet_list',
    'cite',
    'document',
    'emph',
    'figure',
    'footnote',
    'heading',
    'link',
    'numbered_list',
    'numbering',
    'outline',
    'par',
    'parbreak',
    'quote',
    'ref',
    'strong',
    'table',
    'terms',
]
