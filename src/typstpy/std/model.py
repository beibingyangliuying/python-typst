from types import MappingProxyType

from typstpy._core import (
    attach_func,
    call_,
    implement,
    instance,
    normal,
    positional,
    post_series,
    validate_value,
)
from typstpy.std.layout import hspace, repeat
from typstpy.std.text import lorem  # noqa
from typstpy.std.visualize import image, line  # noqa

_DEFAULT_PAR_JUSTIFICATION_LIMITS = MappingProxyType(
    {
        'spacing': MappingProxyType({'min': '66.67% + 0pt', 'max': '150% + 0pt'}),
        'tracking': MappingProxyType({'min': '0pt', 'max': '0pt'}),
    }
)
_DEFAULT_PAR_FIRST_LINE_INDENT = MappingProxyType({'amount': '0pt', 'all': False})


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/bibliography/; parameters match; style validation intentionally relaxed to accept strings and CSL paths.
@implement(
    'bibliography',
    hyperlink='https://typst.app/docs/reference/model/bibliography/',
    version='0.14.2',
)
def bibliography(
    path,
    /,
    *,
    title='auto',
    full=False,
    style='"ieee"',
):
    """Interface of `bibliography` in typst. See [the documentation](https://typst.app/docs/reference/model/bibliography/) for more information.

    Args:
        path: Path(s) to Hayagriva .yml and/or BibLaTeX .bib files.
        title: The title of the bibliography. Defaults to 'auto'.
        full: Whether to include all works from the given bibliography files, even those that weren't cited in the document. Defaults to False.
        style: The bibliography style. Defaults to '"ieee"'.

    Returns:
        Executable typst code.

    Examples:
        >>> bibliography('"bibliography.bib"', style='"cell"')
        '#bibliography("bibliography.bib", style: "cell")'
    """
    return normal(
        bibliography,
        path,
        title=title,
        full=full,
        style=style,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/list/#definitions-item; parameters match.
@implement(
    'list.item',
    hyperlink='https://typst.app/docs/reference/model/list/#definitions-item',
    version='0.14.2',
)
def _bullet_list_item(body, /):
    """Interface of `list.item` in typst. See [the documentation](https://typst.app/docs/reference/model/list/#definitions-item) for more information.

    Args:
        body: The item's body.

    Returns:
        Executable typst code.

    Examples:
        >>> bullet_list.item('[Hello, World!]')
        '#list.item([Hello, World!])'
    """
    return normal(_bullet_list_item, body)


@attach_func(_bullet_list_item, 'item')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/list/; parameters match.
@implement(
    'list',
    hyperlink='https://typst.app/docs/reference/model/list/',
    version='0.14.2',
    spread_single=True,
)
def bullet_list(
    *children,
    tight=True,
    marker=('[•]', '[‣]', '[–]'),
    indent='0pt',
    body_indent='0.5em',
    spacing='auto',
):
    """Interface of `list` in typst. See [the documentation](https://typst.app/docs/reference/model/list/) for more information.

    Args:
        tight: Defines the default spacing of the list. Defaults to True.
        marker: The marker which introduces each item. Defaults to ('[•]', '[‣]', '[–]').
        indent: The indent of each item. Defaults to '0pt'.
        body_indent: The spacing between the marker and the body of each item. Defaults to '0.5em'.
        spacing: The spacing between the items of the list. Defaults to 'auto'.

    Returns:
        Executable typst code.

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


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/cite/; form accepts none per official docs; style validation intentionally relaxed to accept strings and CSL paths.
@implement(
    'cite',
    hyperlink='https://typst.app/docs/reference/model/cite/',
    version='0.14.2',
)
def cite(
    key,
    /,
    *,
    supplement=None,
    form: str | None = '"normal"',
    style='auto',
):  # Support version: 0.13.x
    """Interface of `cite` in typst. See [the documentation](https://typst.app/docs/reference/model/cite/) for more information.

    Args:
        key: The citation key that identifies the entry in the bibliography that shall be cited, as a label.
        supplement: A supplement for the citation such as page or chapter number. Defaults to None.
        form: The kind of citation to produce. Defaults to '"normal"'.
        style: The citation style. Defaults to 'auto'.

    Raises:
        ValueError: If `form` is invalid.

    Returns:
        Executable typst code.

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
    if form is not None:
        validate_value(
            cite,
            'form',
            form,
            {'none', '"normal"', '"prose"', '"full"', '"author"', '"year"'},
        )
    return normal(
        cite,
        key,
        supplement=supplement,
        form=form,
        style=style,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/document/; parameters match.
@implement(
    'document',
    hyperlink='https://typst.app/docs/reference/model/document/',
    version='0.14.2',
)
def document(
    *,
    title=None,
    author=tuple(),
    description=None,
    keywords=tuple(),
    date='auto',
):  # Support version: 0.13.x
    """Interface of `document` in typst. See [the documentation](https://typst.app/docs/reference/model/document/) for more information.

    Args:
        title: The document's title. Defaults to None.
        author: The document's authors. Defaults to tuple().
        description: The document's description. Defaults to None.
        keywords: The document's keywords. Defaults to tuple().
        date: The document's creation date. Defaults to 'auto'.

    Returns:
        Executable typst code.
    """
    return normal(
        document,
        title=title,
        author=author,
        description=description,
        keywords=keywords,
        date=date,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/emph/; parameters match.
@implement(
    'emph',
    hyperlink='https://typst.app/docs/reference/model/emph/',
    version='0.14.2',
)
def emph(body, /):  # Support version: 0.13.x
    """Interface of `emph` in typst. See [the documentation](https://typst.app/docs/reference/model/emph/) for more information.

    Args:
        body: The content to emphasize.

    Returns:
        Executable typst code.

    Examples:
        >>> emph('"Hello, World!"')
        '#emph("Hello, World!")'
        >>> emph('[Hello, World!]')
        '#emph([Hello, World!])'
    """
    return normal(emph, body)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/figure/#definitions-caption; parameters match.
@implement(
    'figure.caption',
    hyperlink='https://typst.app/docs/reference/model/figure/#definitions-caption',
    version='0.14.2',
)
def _figure_caption(
    body,
    /,
    *,
    position='bottom',
    separator='auto',
):  # Support version: 0.13.x
    """Interface of `figure.caption` in typst. See [the documentation](https://typst.app/docs/reference/model/figure/#definitions-caption) for more information.

    Args:
        body: The caption's body.
        position: The caption's position in the figure. Defaults to 'bottom'.
        separator: The separator which will appear between the number and body. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> figure.caption('[Hello, World!]')
        '#figure.caption([Hello, World!])'
        >>> figure.caption('[Hello, World!]', position='top', separator='[---]')
        '#figure.caption([Hello, World!], position: top, separator: [---])'
    """
    return normal(_figure_caption, body, position=position, separator=separator)


@attach_func(_figure_caption, 'caption')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/figure/; parameters match; alt parameter moved to end in normal() call (non-breaking).
@implement(
    'figure',
    hyperlink='https://typst.app/docs/reference/model/figure/',
    version='0.14.2',
)
def figure(
    body,
    /,
    *,
    alt=None,
    placement=None,
    scope='"column"',
    caption=None,
    kind='auto',
    supplement='auto',
    numbering='"1"',
    gap='0.65em',
    outlined=True,
):
    """Interface of `figure` in typst. See [the documentation](https://typst.app/docs/reference/model/figure/) for more information.

    Args:
        body: The content of the figure.
        alt: An alternative description for the figure, used for accessibility. Defaults to None.
        placement: The figure's placement on the page. Defaults to None.
        scope: Relative to which containing scope the figure is placed. Defaults to '"column"'.
        caption: The figure's caption. Defaults to None.
        kind: The kind of figure this is. Defaults to 'auto'.
        supplement: The figure's supplement. Defaults to 'auto'.
        numbering: How to number the figure. Defaults to '"1"'.
        gap: The vertical gap between the body and caption. Defaults to '0.65em'.
        outlined: Whether the figure should appear in an outline of figures. Defaults to True.

    Raises:
        ValueError: If `scope` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> figure(image('"image.png"'))
        '#figure(image("image.png"))'
        >>> figure(image('"image.png"'), caption='[Hello, World!]')
        '#figure(image("image.png"), caption: [Hello, World!])'
    """
    validate_value(figure, 'scope', scope, {'"column"', '"parent"'})

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
        alt=alt,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/footnote/#definitions-entry; parameters match.
@implement(
    'footnote.entry',
    hyperlink='https://typst.app/docs/reference/model/footnote/#definitions-entry',
    version='0.14.2',
)
def _footnote_entry(
    note,
    /,
    *,
    separator=line(length='30% + 0pt', stroke='0.5pt'),
    clearance='1em',
    gap='0.5em',
    indent='1em',
):
    """Interface of `footnote.entry` in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/#definitions-entry) for more information.

    Args:
        note: The footnote for this entry.
        separator: The separator between the document body and the footnote listing. Defaults to line(length='30% + 0pt', stroke='0.5pt').
        clearance: The amount of clearance between the document body and the separator. Defaults to '1em'.
        gap: The gap between footnote entries. Defaults to '0.5em'.
        indent: The indent of each footnote entry. Defaults to '1em'.

    Returns:
        Executable typst code.
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
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/footnote/; parameters match.
@implement(
    'footnote',
    hyperlink='https://typst.app/docs/reference/model/footnote/',
    version='0.14.2',
)
def footnote(body, /, *, numbering='"1"'):
    """Interface of `footnote` in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/) for more information.

    Args:
        body: The content to put into the footnote.
        numbering: How to number footnotes. Defaults to '"1"'.

    Returns:
        Executable typst code.

    Examples:
        >>> footnote('[Hello, World!]')
        '#footnote([Hello, World!])'
        >>> footnote('[Hello, World!]', numbering='"a"')
        '#footnote([Hello, World!], numbering: "a")'
    """
    return normal(footnote, body, numbering=numbering)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/heading/; parameters match.
@implement(
    'heading',
    hyperlink='https://typst.app/docs/reference/model/heading/',
    version='0.14.2',
)
def heading(
    body,
    /,
    *,
    level='auto',
    depth=1,
    offset=0,
    numbering=None,
    supplement='auto',
    outlined=True,
    bookmarked='auto',
    hanging_indent='auto',
):
    """Interface of `heading` in typst. See [the documentation](https://typst.app/docs/reference/model/heading/) for more information.

    Args:
        body: The heading's title.
        level: The absolute nesting depth of the heading, starting from one. Defaults to 'auto'.
        depth: The relative nesting depth of the heading, starting from one. Defaults to 1.
        offset: The starting offset of each heading's level, used to turn its relative depth into its absolute level. Defaults to 0.
        numbering: How to number the heading. Defaults to None.
        supplement: A supplement for the heading. Defaults to 'auto'.
        outlined: Whether the heading should appear in the outline. Defaults to True.
        bookmarked: Whether the heading should appear as a bookmark in the exported PDF's outline. Defaults to 'auto'.
        hanging_indent: The indent all but the first line of a heading should have. Defaults to 'auto'.

    Returns:
        Executable typst code.

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


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/link/; parameters match; body optionality follows Python convention for dest-only URL links.
@implement(
    'link',
    hyperlink='https://typst.app/docs/reference/model/link/',
    version='0.14.2',
)
def link(dest, body=None, /):
    """Interface of `link` in typst. See [the documentation](https://typst.app/docs/reference/model/link/) for more information.

    Args:
        dest: The destination the link points to.
        body: The content that should become a link. Defaults to None.

    Returns:
        Executable typst code.

    Examples:
        >>> link('"https://typst.app"')
        '#link("https://typst.app")'
        >>> link('"https://typst.app"', '"Typst"')
        '#link("https://typst.app", "Typst")'
    """
    return positional(link, *([dest] if body is None else [dest, body]))


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/enum/#definitions-item; parameters match.
@implement(
    'enum.item',
    hyperlink='https://typst.app/docs/reference/model/enum/#definitions-item',
    version='0.14.2',
)
def _numbered_list_item(body, /, *, number='auto'):
    """Interface of `enum.item` in typst. See [the documentation](https://typst.app/docs/reference/model/enum/#definitions-item) for more information.

    Args:
        body: The item's body.
        number: The item's number. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> numbered_list.item('[Hello, World!]', number=2)
        '#enum.item(2, [Hello, World!])'
    """
    if number == 'auto':
        return normal(_numbered_list_item, body)
    return call_(_numbered_list_item, number, body)


@attach_func(_numbered_list_item, 'item')
# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/enum/; parameters match.
@implement(
    'enum',
    hyperlink='https://typst.app/docs/reference/model/enum/',
    version='0.14.2',
    spread_single=True,
)
def numbered_list(
    *children,
    tight=True,
    numbering='"1."',
    start: int | str = 'auto',
    full=False,
    reversed=False,
    indent='0pt',
    body_indent='0.5em',
    spacing='auto',
    number_align='end + top',
):
    """Interface of `enum` in typst. See [the documentation](https://typst.app/docs/reference/model/enum/) for more information.

    Args:
        tight: Defines the default spacing of the enumeration. Defaults to True.
        numbering: How to number the enumeration. Defaults to '"1."'.
        start: Which number to start the enumeration with. Defaults to 'auto'.
        full: Whether to display the full numbering, including the numbers of all parent enumerations. Defaults to False.
        reversed: Whether to reverse the numbering for this enumeration. Defaults to False.
        indent: The indentation of each item. Defaults to '0pt'.
        body_indent: The space between the numbering and the body of each item. Defaults to '0.5em'.
        spacing: The spacing between the items of the enumeration. Defaults to 'auto'.
        number_align: The alignment that enum numbers should have. Defaults to 'end + top'.

    Returns:
        Executable typst code.

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
        reversed=reversed,
        indent=indent,
        body_indent=body_indent,
        spacing=spacing,
        number_align=number_align,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/numbering/; parameters match.
@implement(
    'numbering',
    hyperlink='https://typst.app/docs/reference/model/numbering/',
    version='0.14.2',
)
def numbering(numbering_, /, *numbers):
    """Interface of `numbering` in typst. See [the documentation](https://typst.app/docs/reference/model/numbering/) for more information.

    Args:
        numbering_: Defines how the numbering works.

    Returns:
        Executable typst code.

    Examples:
        >>> numbering('"1.1)"', 1, 2)
        '#numbering("1.1)", 1, 2)'
    """
    return normal(numbering, numbering_, *numbers)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry; parameters match.
@implement(
    'outline.entry',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry',
    version='0.14.2',
)
def _outline_entry(
    level,
    element,
    /,
    *,
    fill=repeat('[.]', gap='0.15em'),
):
    """Interface of `outline.entry` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry) for more information.

    Args:
        level: The nesting level of this outline entry.
        element: The element this entry refers to.
        fill: Content to fill the space between the title and the page number.

    Returns:
        Executable typst code.
    """
    return normal(_outline_entry, '', level, element, fill=fill)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented; parameters match.
@implement(
    'indented',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented',
    version='0.14.2',
)
def _outline_indented(self, prefix, inner, /, *, gap='0.5em'):
    """Interface of `outline.indented` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented) for more information.

    Args:
        self: An outline entry.
        prefix: The prefix is aligned with the inner content of entries that have level one less.
        inner: The formatted inner content of the entry.
        gap: The gap between the prefix and the inner content. Defaults to '0.5em'.

    Returns:
        Executable typst code.
    """
    return instance(_outline_indented, self, prefix, inner, gap=gap)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix; parameters match.
@implement(
    'prefix',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix',
    version='0.14.2',
)
def _outline_prefix(self, /):
    """Interface of `outline.prefix` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix) for more information.

    Args:
        self: An outline entry.

    Returns:
        Executable typst code.
    """
    return instance(_outline_prefix, self)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner; parameters match.
@implement(
    'inner',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner',
    version='0.14.2',
)
def _outline_inner(self, /):
    """Interface of `outline.inner` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner) for more information.

    Args:
        self: An outline entry.

    Returns:
        Executable typst code.
    """
    return instance(_outline_inner, self)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body; parameters match.
@implement(
    'body',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body',
    version='0.14.2',
)
def _outline_body(self, /):
    """Interface of `outline.body` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body) for more information.

    Args:
        self: An outline entry.

    Returns:
        Executable typst code.
    """
    return instance(_outline_body, self)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page; parameters match.
@implement(
    'page',
    hyperlink='https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page',
    version='0.14.2',
)
def _outline_page(self, /):
    """Interface of `outline.page` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page) for more information.

    Args:
        self: An outline entry.

    Returns:
        Executable typst code.
    """
    return instance(_outline_page, self)


@attach_func(_outline_entry, 'entry')
@attach_func(_outline_indented, 'indented')
@attach_func(_outline_prefix, 'prefix')
@attach_func(_outline_inner, 'inner')
@attach_func(_outline_body, 'body')
@attach_func(_outline_page, 'page')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/outline/; parameters match.
@implement(
    'outline',
    hyperlink='https://typst.app/docs/reference/model/outline/',
    version='0.14.2',
)
def outline(
    *,
    title='auto',
    target=heading,
    depth=None,
    indent='auto',
):
    """Interface of `outline` in typst. See [the documentation](https://typst.app/docs/reference/model/outline/) for more information.

    Args:
        title: The title of the outline. Defaults to 'auto'.
        target: The type of element to include in the outline. Defaults to heading.
        depth: The maximum level up to which elements are included in the outline. Defaults to None.
        indent: How to indent the outline's entries. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> outline()
        '#outline()'
        >>> outline(title='"Hello, World!"', target=heading.where(outlined=True))
        '#outline(title: "Hello, World!", target: heading.where(outlined: true))'
    """
    return normal(outline, title=title, target=target, depth=depth, indent=indent)


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/par/#definitions-line; parameters match.
@implement(
    'par.line',
    hyperlink='https://typst.app/docs/reference/model/par/#definitions-line',
    version='0.14.2',
)
def _par_line(
    *,
    numbering=None,
    number_align='auto',
    number_margin='start',
    number_clearance='auto',
    numbering_scope='"document"',
):
    """Interface of `par.line` in typst. See [the documentation](https://typst.app/docs/reference/model/par/#definitions-line) for more information.

    Args:
        numbering: How to number each line. Defaults to None.
        number_align: The alignment of line numbers associated with each line. Defaults to 'auto'.
        number_margin: The margin at which line numbers appear. Defaults to 'start'.
        number_clearance: The distance between line numbers and text. Defaults to 'auto'.
        numbering_scope: Controls when to reset line numbering. Defaults to '"document"'.

    Raises:
        ValueError: If `numbering_scope` is invalid.

    Returns:
        Executable typst code.
    """
    validate_value(
        _par_line, 'numbering_scope', numbering_scope, {'"document"', '"page"'}
    )

    return normal(
        _par_line,
        numbering=numbering,
        number_align=number_align,
        number_margin=number_margin,
        number_clearance=number_clearance,
        numbering_scope=numbering_scope,
    )


@attach_func(_par_line, 'line')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/par/; parameters match.
@implement(
    'par', hyperlink='https://typst.app/docs/reference/model/par/', version='0.14.2'
)
def par(
    body,
    /,
    *,
    leading='0.65em',
    spacing='1.2em',
    justify=False,
    justification_limits=_DEFAULT_PAR_JUSTIFICATION_LIMITS,
    linebreaks='auto',
    first_line_indent=_DEFAULT_PAR_FIRST_LINE_INDENT,
    hanging_indent='0pt',
) -> str:
    """Interface of `par` in typst. See [the documentation](https://typst.app/docs/reference/model/par/) for more information.

    Args:
        body: The contents of the paragraph.
        leading: The spacing between lines. Defaults to '0.65em'.
        spacing: The spacing between paragraphs. Defaults to '1.2em'.
        justify: Whether to justify text in its line. Defaults to False.
        justification_limits: How much the spacing between words and characters may be adjusted during justification. Defaults to Typst's standard spacing and tracking limits.
        linebreaks: How to determine line breaks. Defaults to 'auto'.
        first_line_indent: The indent the first line of a paragraph should have. Defaults to Typst's standard first-line indent mapping.
        hanging_indent: The indent all but the first line of a paragraph should have. Defaults to '0pt'.

    Raises:
        ValueError: If `linebreaks` is invalid.

    Returns:
        Executable typst code.

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
    if linebreaks != 'auto':
        validate_value(par, 'linebreaks', linebreaks, {'"simple"', '"optimized"'})

    return normal(
        par,
        body,
        leading=leading,
        spacing=spacing,
        justify=justify,
        justification_limits=justification_limits,
        linebreaks=linebreaks,
        first_line_indent=first_line_indent,
        hanging_indent=hanging_indent,
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/parbreak/; parameters match.
@implement(
    'parbreak',
    hyperlink='https://typst.app/docs/reference/model/parbreak/',
    version='0.14.2',
)
def parbreak():
    """Interface of `parbreak` in typst. See [the documentation](https://typst.app/docs/reference/model/parbreak/) for more information.

    Returns:
        Executable typst code.

    Examples:
        >>> parbreak()
        '#parbreak()'
    """
    return normal(parbreak)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/quote/; parameters match.
@implement(
    'quote',
    hyperlink='https://typst.app/docs/reference/model/quote/',
    version='0.14.2',
)
def quote(
    body,
    /,
    *,
    block=False,
    quotes='auto',
    attribution=None,
):
    """Interface of `quote` in typst. See [the documentation](https://typst.app/docs/reference/model/quote/) for more information.

    Args:
        body: The quote.
        block: Whether this is a block quote. Defaults to False.
        quotes: Whether double quotes should be added around this quote. Defaults to 'auto'.
        attribution: The attribution of this quote, usually the author or source. Defaults to None.

    Returns:
        Executable typst code.

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


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/ref/; parameters match.
@implement(
    'ref',
    hyperlink='https://typst.app/docs/reference/model/ref/',
    version='0.14.2',
)
def ref(
    target,
    /,
    *,
    supplement='auto',
    form='"normal"',
):
    """Interface of `ref` in typst. See [the documentation](https://typst.app/docs/reference/model/ref/) for more information.

    Args:
        target: The target label that should be referenced.
        supplement: A supplement for the reference. Defaults to 'auto'.
        form: The kind of reference to produce. Defaults to '"normal"'.

    Raises:
        ValueError: If `form` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> ref('<label>')
        '#ref(<label>)'
        >>> ref('<label>', supplement='[Hello, World!]')
        '#ref(<label>, supplement: [Hello, World!])'
    """
    validate_value(ref, 'form', form, {'"normal"', '"page"'})

    return normal(ref, target, supplement=supplement, form=form)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/strong/; parameters match.
@implement(
    'strong',
    hyperlink='https://typst.app/docs/reference/model/strong/',
    version='0.14.2',
)
def strong(body, /, *, delta=300):
    """Interface of `strong` in typst. See [the documentation](https://typst.app/docs/reference/model/strong/) for more information.

    Args:
        body: The content to strongly emphasize.
        delta: The delta to apply on the font weight. Defaults to 300.

    Returns:
        Executable typst code.

    Examples:
        >>> strong('"Hello, World!"')
        '#strong("Hello, World!")'
        >>> strong('[Hello, World!]', delta=400)
        '#strong([Hello, World!], delta: 400)'
    """
    return normal(strong, body, delta=delta)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/table/#definitions-cell; parameters match.
@implement(
    'table.cell',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-cell',
    version='0.14.2',
)
def _table_cell(
    body,
    /,
    *,
    x='auto',
    y='auto',
    colspan=1,
    rowspan=1,
    fill='auto',
    align='auto',
    inset='auto',
    stroke=dict(),
    breakable='auto',
):
    """Interface of `table.cell` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-cell) for more information.

    Args:
        body: The cell's body.
        x: The cell's column (zero-indexed). Defaults to 'auto'.
        y: The cell's row (zero-indexed). Defaults to 'auto'.
        colspan: The amount of columns spanned by this cell. Defaults to 1.
        rowspan: The cell's fill override. Defaults to 1.
        fill: The amount of rows spanned by this cell. Defaults to 'auto'.
        align: The cell's alignment override. Defaults to 'auto'.
        inset: The cell's inset override. Defaults to 'auto'.
        stroke: The cell's stroke override. Defaults to dict().
        breakable: Whether rows spanned by this cell can be placed in different pages. Defaults to 'auto'.

    Returns:
        Executable typst code.
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


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/table/#definitions-hline; parameters match.
@implement(
    'table.hline',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-hline',
    version='0.14.2',
)
def _table_hline(
    *,
    y='auto',
    start=0,
    end=None,
    stroke='1pt + black',
    position='top',
):
    """Interface of `table.hline` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-hline) for more information.

    Args:
        y: The row above which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start: The column at which the horizontal line starts (zero-indexed, inclusive). Defaults to 0.
        end: The column before which the horizontal line ends (zero-indexed, exclusive). Defaults to None.
        stroke: The line's stroke. Defaults to '1pt + black'.
        position: The position at which the line is placed, given its row (y) - either top to draw above it or bottom to draw below it. Defaults to 'top'.

    Raises:
        ValueError: If `position` is invalid.

    Returns:
        Executable typst code.
    """
    validate_value(_table_hline, 'position', position, {'top', 'bottom'})

    return normal(
        _table_hline, y=y, start=start, end=end, stroke=stroke, position=position
    )


# * Typst docs verified on 2026-05-22: https://typst.app/docs/reference/model/table/#definitions-vline; parameters match; position also accepts left/right as discouraged aliases.
@implement(
    'table.vline',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-vline',
    version='0.14.2',
)
def _table_vline(
    *,
    x='auto',
    start=0,
    end=None,
    stroke='1pt + black',
    position='start',
):
    """Interface of `table.vline` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-vline) for more information.

    Args:
        x: The column before which the horizontal line is placed (zero-indexed). Defaults to 'auto'.
        start: The row at which the vertical line starts (zero-indexed, inclusive). Defaults to 0.
        end: The row on top of which the vertical line ends (zero-indexed, exclusive). Defaults to None.
        stroke: The line's stroke. Defaults to '1pt + black'.
        position: The position at which the line is placed, given its column (x) - either start to draw before it or end to draw after it. Defaults to 'start'.

    Raises:
        ValueError: If `position` is invalid.

    Returns:
        Executable typst code.
    """
    validate_value(
        _table_vline, 'position', position, {'start', 'end', 'left', 'right'}
    )

    return normal(
        _table_vline, x=x, start=start, end=end, stroke=stroke, position=position
    )


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/table/#definitions-header; parameters match.
@implement(
    'table.header',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-header',
    version='0.14.2',
)
def _table_header(*children, repeat=True, level=1):
    """Interface of `table.header` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-header) for more information.

    Args:
        repeat: Whether this header should be repeated across pages. Defaults to True.
        level: The level of the header. Must not be zero. Defaults to 1.

    Returns:
        Executable typst code.
    """
    return post_series(_table_header, *children, repeat=repeat, level=level)


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/table/#definitions-footer; parameters match.
@implement(
    'table.footer',
    hyperlink='https://typst.app/docs/reference/model/table/#definitions-footer',
    version='0.14.2',
)
def _table_footer(*children, repeat=True):
    """Interface of `table.footer` in typst. See [the documentation](https://typst.app/docs/reference/model/table/#definitions-footer) for more information.

    Args:
        repeat: Whether this footer should be repeated across pages. Defaults to True.

    Returns:
        Executable typst code.
    """
    return post_series(_table_footer, *children, repeat=repeat)


@attach_func(_table_cell, 'cell')
@attach_func(_table_hline, 'hline')
@attach_func(_table_vline, 'vline')
@attach_func(_table_header, 'header')
@attach_func(_table_footer, 'footer')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/table/; parameters match.
@implement(
    'table',
    hyperlink='https://typst.app/docs/reference/model/table/',
    version='0.14.2',
    spread_single=True,
)
def table(
    *children,
    columns=tuple(),
    rows=tuple(),
    gutter=tuple(),
    column_gutter=tuple(),
    row_gutter=tuple(),
    fill=None,
    align='auto',
    stroke='1pt + black',
    inset='0% + 5pt',
):
    """Interface of `table` in typst. See [the documentation](https://typst.app/docs/reference/model/table/) for more information.

    Args:
        columns: The column sizes. Defaults to tuple().
        rows: The row sizes. Defaults to tuple().
        gutter: The gaps between rows and columns. Defaults to tuple().
        column_gutter: The gaps between columns. Defaults to tuple().
        row_gutter: The gaps between rows. Defaults to tuple().
        fill: How to fill the cells. Defaults to None.
        align: How to align the cells' content. Defaults to 'auto'.
        stroke: How to stroke the cells. Defaults to '1pt + black'.
        inset: How much to pad the cells' content. Defaults to '0% + 5pt'.

    Returns:
        Executable typst code.

    Examples:
        >>> table('[1]')
        '#table([1])'
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


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/title/; parameters match.
@implement(
    'title',
    hyperlink='https://typst.app/docs/reference/model/title/',
    version='0.14.2',
)
def title(body='auto', /):
    """Interface of `title` in typst. See [the documentation](https://typst.app/docs/reference/model/title/) for more information.

    Args:
        body: The content of the title. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> title()
        '#title()'
        >>> title('[My Thesis]')
        '#title([My Thesis])'
    """
    return normal(title, body if body != 'auto' else '')


# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/terms/#definitions-item; parameters match.
@implement(
    'terms.item',
    hyperlink='https://typst.app/docs/reference/model/terms/#definitions-item',
    version='0.14.2',
)
def _terms_item(term, description, /):
    """Interface of `terms.item` in typst. See [the documentation](https://typst.app/docs/reference/model/terms/#definitions-item) for more information.

    Args:
        term: The term described by the list item.
        description: The description of the term.

    Returns:
        Executable typst code.

    Examples:
        >>> terms.item('"term"', '"description"')
        '#terms.item("term", "description")'
    """
    return positional(_terms_item, term, description)


@attach_func(_terms_item, 'item')
# * Typst docs verified on 2026-05-23: https://typst.app/docs/reference/model/terms/; parameters match.
@implement(
    'terms',
    hyperlink='https://typst.app/docs/reference/model/terms/',
    version='0.14.2',
)
def terms(
    *children,
    tight=True,
    separator=hspace('0.6em', weak=True),
    indent='0pt',
    hanging_indent='2em',
    spacing='auto',
):
    """Interface of `terms` in typst. See [the documentation](https://typst.app/docs/reference/model/terms/) for more information.

    Args:
        tight: Defines the default spacing of the term list. Defaults to True.
        separator: The separator between the item and the description. Defaults to hspace('0.6em', weak=True).
        indent: The indentation of each item. Defaults to '0pt'.
        hanging_indent: The hanging indent of the description. Defaults to '2em'.
        spacing: The spacing between the items of the term list. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> terms(('[1]', lorem(20)))
        '#terms(([1], lorem(20)))'
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
    'title',
    'terms',
]
