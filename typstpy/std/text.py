from typing import Any, Iterable

from cytoolz.curried import map  # type:ignore

from .._utils import attach_func, implement, is_valid, normal, pad, positional
from ..typings import Block
from .visualize import luma, rgb


@implement(
    True,
    original_name='highlight',
    hyperlink='https://typst.app/docs/reference/text/highlight/',
)
def highlight(
    body: str,
    /,
    *,
    fill: str | None = rgb('"#fffd11a1"'),
    stroke: str | dict[str, Any] | None = dict(),
    top_edge: str = '"ascender"',
    bottom_edge: str = '"descender"',
    extent: str = '0pt',
    radius: str | dict[str, Any] = dict(),
) -> Block:
    """Interface of `highlight` in typst. See [the documentation](https://typst.app/docs/reference/text/highlight/) for more information.

    Args:
        body (str): The content that should be highlighted.
        fill (str | None, optional): The color to highlight the text with. Defaults to rgb('"#fffd11a1"').
        stroke (str | dict[str, Any] | None, optional): The highlight's border color. Defaults to dict().
        top_edge (str, optional): The top end of the background rectangle. Defaults to '"ascender"'.
        bottom_edge (str, optional): The bottom end of the background rectangle. Defaults to '"descender"'.
        extent (str, optional): The amount by which to extend the background to the sides beyond (or within if negative) the content. Defaults to '0pt'.
        radius (str | dict[str, Any], optional): How much to round the highlight's corners. Defaults to dict().

    Raises:
        ValueError: If `top_edge` or `bottom_edge` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> highlight('"Hello, world!"', fill=rgb('"#ffffff"'))
        '#highlight("Hello, world!", fill: rgb("#ffffff"))'
        >>> highlight('"Hello, world!"', fill=rgb('"#ffffff"'), stroke=rgb('"#000000"'))
        '#highlight("Hello, world!", fill: rgb("#ffffff"), stroke: rgb("#000000"))'
        >>> highlight(
        ...     '"Hello, world!"',
        ...     fill=rgb('"#ffffff"'),
        ...     stroke=rgb('"#000000"'),
        ...     top_edge='"bounds"',
        ...     bottom_edge='"bounds"',
        ... )
        '#highlight("Hello, world!", fill: rgb("#ffffff"), stroke: rgb("#000000"), top-edge: "bounds", bottom-edge: "bounds")'
    """
    is_valid(
        lambda: top_edge
        in map(pad, ('ascender', 'cap-height', 'x-height', 'baseline', 'bounds')),
        lambda: bottom_edge in map(pad, ('baseline', 'descender', 'bounds')),
    )
    return normal(
        highlight,
        body,
        fill=fill,
        stroke=stroke,
        top_edge=top_edge,
        bottom_edge=bottom_edge,
        extent=extent,
        radius=radius,
    )


@implement(
    True,
    original_name='linebreak',
    hyperlink='https://typst.app/docs/reference/text/linebreak/',
)
def linebreak(*, justify: bool = False) -> Block:
    """Interface of `linebreak` in typst. See [the documentation](https://typst.app/docs/reference/text/linebreak/) for more information.

    Args:
        justify (bool, optional): Whether to justify the line before the break. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> linebreak()
        '#linebreak()'
        >>> linebreak(justify=True)
        '#linebreak(justify: true)'
    """
    return normal(linebreak, justify=justify)


@implement(
    True,
    original_name='lorem',
    hyperlink='https://typst.app/docs/reference/text/lorem/',
)
def lorem(words: int, /) -> Block:
    """Interface of `lorem` in typst. See [the documentation](https://typst.app/docs/reference/text/lorem/) for more information.

    Args:
        words (int): The length of the blind text in words.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> lorem(10)
        '#lorem(10)'
    """
    return normal(lorem, words)


@implement(
    True,
    original_name='lower',
    hyperlink='https://typst.app/docs/reference/text/lower/',
)
def lower(text: str, /) -> Block:
    """Interface of `lower` in typst. See [the documentation](https://typst.app/docs/reference/text/lower/) for more information.

    Args:
        text (str): The text to convert to lowercase.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> lower('"Hello, World!"')
        '#lower("Hello, World!")'
        >>> lower('[Hello, World!]')
        '#lower([Hello, World!])'
        >>> lower(upper('"Hello, World!"'))
        '#lower(upper("Hello, World!"))'
    """
    return normal(lower, text)


@implement(
    True,
    original_name='overline',
    hyperlink='https://typst.app/docs/reference/text/overline/',
)
def overline(
    body: str,
    /,
    *,
    stroke: str | dict[str, Any] = 'auto',
    offset: str = 'auto',
    extent: str = '0pt',
    evade: bool = True,
    background: bool = False,
) -> Block:
    """Interface of `overline` in typst. See [the documentation](https://typst.app/docs/reference/text/overline/) for more information.

    Args:
        body (str): The content to add a line over.
        stroke (str | dict[str, Any], optional): How to stroke the line. Defaults to 'auto'.
        offset (str, optional): The position of the line relative to the baseline. Defaults to 'auto'.
        extent (str, optional): The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        evade (bool, optional): Whether the line skips sections in which it would collide with the glyphs. Defaults to True.
        background (bool, optional): Whether the line is placed behind the content it overlines. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> overline('"Hello, World!"')
        '#overline("Hello, World!")'
        >>> overline('[Hello, World!]')
        '#overline([Hello, World!])'
        >>> overline(
        ...     upper('"Hello, World!"'),
        ...     stroke='red',
        ...     offset='0pt',
        ...     extent='0pt',
        ...     evade=False,
        ...     background=True,
        ... )
        '#overline(upper("Hello, World!"), stroke: red, offset: 0pt, evade: false, background: true)'
    """
    return normal(
        overline,
        body,
        stroke=stroke,
        offset=offset,
        extent=extent,
        evade=evade,
        background=background,
    )


@implement(
    True,
    original_name='raw.line',
    hyperlink='https://typst.app/docs/reference/text/raw/#definitions-line',
)
def _raw_line(number: int, count: int, text: str, body: str, /) -> Block:
    """Interface of `raw.line` in typst. See [the documentation](https://typst.app/docs/reference/text/raw/#definitions-line) for more information.

    Args:
        number (int): The line number of the raw line inside of the raw block, starts at 1.
        count (int): The total number of lines in the raw block.
        text (str): The line of raw text.
        body (str): The highlighted raw text.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> raw.line(1, 1, '"Hello, World!"', '"Hello, World!"')
        '#raw.line(1, 1, "Hello, World!", "Hello, World!")'
    """
    return positional(_raw_line, number, count, text, body)


@attach_func(_raw_line, 'line')
@implement(
    True,
    original_name='raw',
    hyperlink='https://typst.app/docs/reference/text/raw/',
)
def raw(
    text: str,
    /,
    *,
    block: bool = False,
    lang: str | None = None,
    align: str = 'start',
    syntaxes: str | Iterable[str] = tuple(),
    theme: str | None = 'auto',
    tab_size: int = 2,
) -> Block:
    """Interface of `raw` in typst. See [the documentation](https://typst.app/docs/reference/text/raw/) for more information.

    Args:
        text (str): The raw text.
        block (bool, optional): Whether the raw text is displayed as a separate block. Defaults to False.
        lang (str | None, optional): The language to syntax-highlight in. Defaults to None.
        align (str, optional): The horizontal alignment that each line in a raw block should have. Defaults to 'start'.
        syntaxes (str | Iterable[str], optional): One or multiple additional syntax definitions to load. Defaults to tuple().
        theme (str | None, optional): The theme to use for syntax highlighting. Defaults to 'auto'.
        tab_size (int, optional): The size for a tab stop in spaces. Defaults to 2.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> raw('"Hello, World!"')
        '#raw("Hello, World!")'
        >>> raw('"Hello, World!"', block=True, align='center')
        '#raw("Hello, World!", block: true, align: center)'
        >>> raw('"Hello, World!"', lang='"rust"')
        '#raw("Hello, World!", lang: "rust")'
        >>> raw('"Hello, World!"', tab_size=4)
        '#raw("Hello, World!", tab-size: 4)'
    """
    return normal(
        raw,
        text,
        block=block,
        lang=lang,
        align=align,
        syntaxes=syntaxes,
        theme=theme,
        tab_size=tab_size,
    )


@implement(
    True,
    original_name='smallcaps',
    hyperlink='https://typst.app/docs/reference/text/smallcaps/',
)
def smallcaps(body: str, /) -> Block:
    """Interface of `smallcaps` in typst. See [the documentation](https://typst.app/docs/reference/text/smallcaps/) for more information.

    Args:
        body (str): The content to display in small capitals.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> smallcaps('"Hello, World!"')
        '#smallcaps("Hello, World!")'
        >>> smallcaps('[Hello, World!]')
        '#smallcaps([Hello, World!])'
    """
    return normal(smallcaps, body)


@implement(
    True,
    original_name='smartquote',
    hyperlink='https://typst.app/docs/reference/text/smartquote/',
)
def smartquote(
    *,
    double: bool = True,
    enabled: bool = True,
    alternative: bool = False,
    quotes: str | Iterable[str] | dict[str, Any] = 'auto',
) -> Block:
    """Interface of `smartquote` in typst. See [the documentation](https://typst.app/docs/reference/text/smartquote/) for more information.

    Args:
        double (bool, optional): Whether this should be a double quote. Defaults to True.
        enabled (bool, optional): Whether smart quotes are enabled. Defaults to True.
        alternative (bool, optional): Whether to use alternative quotes. Defaults to False.
        quotes (str | Iterable[str] | dict[str, Any], optional): The quotes to use. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> smartquote(double=False, enabled=False, alternative=True, quotes='"()"')
        '#smartquote(double: false, enabled: false, alternative: true, quotes: "()")'
        >>> smartquote(quotes=('"()"', '"{}"'))
        '#smartquote(quotes: ("()", "{}"))'
    """
    return normal(
        smartquote,
        double=double,
        enabled=enabled,
        alternative=alternative,
        quotes=quotes,
    )


@implement(
    True,
    original_name='strike',
    hyperlink='https://typst.app/docs/reference/text/strike/',
)
def strike(
    body: str,
    /,
    *,
    stroke: str | dict[str, Any] = 'auto',
    offset: str = 'auto',
    extent: str = '0pt',
    background: bool = False,
) -> Block:
    """Interface of `strike` in typst. See [the documentation](https://typst.app/docs/reference/text/strike/) for more information.

    Args:
        body (str): The content to strike through.
        stroke (str | dict[str, Any], optional): How to stroke the line. Defaults to 'auto'.
        offset (str, optional): The position of the line relative to the baseline. Defaults to 'auto'.
        extent (str, optional): The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        background (bool, optional): Whether the line is placed behind the content. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> strike('"Hello, World!"')
        '#strike("Hello, World!")'
        >>> strike('[Hello, World!]')
        '#strike([Hello, World!])'
        >>> strike(
        ...     upper('"Hello, World!"'),
        ...     stroke='red',
        ...     offset='0.1em',
        ...     extent='0.2em',
        ...     background=True,
        ... )
        '#strike(upper("Hello, World!"), stroke: red, offset: 0.1em, extent: 0.2em, background: true)'
    """
    return normal(
        strike,
        body,
        stroke=stroke,
        offset=offset,
        extent=extent,
        background=background,
    )


@implement(
    True,
    original_name='sub',
    hyperlink='https://typst.app/docs/reference/text/sub/',
)
def subscript(
    body: str,
    /,
    *,
    typographic: bool = True,
    baseline: str = '0.2em',
    size: str = '0.6em',
) -> Block:
    """Interface of `sub` in typst. See [the documentation](https://typst.app/docs/reference/text/sub/) for more information.

    Args:
        body (str): The text to display in subscript.
        typographic (bool, optional): Whether to prefer the dedicated subscript characters of the font. Defaults to True.
        baseline (str, optional): The baseline shift for synthetic subscripts. Defaults to '0.2em'.
        size (str, optional): The font size for synthetic subscripts. Defaults to '0.6em'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> subscript('"Hello, World!"')
        '#sub("Hello, World!")'
        >>> subscript('[Hello, World!]')
        '#sub([Hello, World!])'
        >>> subscript('[Hello, World!]', typographic=False, baseline='0.3em', size='0.7em')
        '#sub([Hello, World!], typographic: false, baseline: 0.3em, size: 0.7em)'
    """
    return normal(
        subscript,
        body,
        typographic=typographic,
        baseline=baseline,
        size=size,
    )


@implement(
    True,
    original_name='super',
    hyperlink='https://typst.app/docs/reference/text/super/',
)
def superscript(
    body: str,
    /,
    *,
    typographic: bool = True,
    baseline: str = '-0.5em',
    size: str = '0.6em',
) -> Block:
    """Interface of `super` in typst. See [the documentation](https://typst.app/docs/reference/text/super/) for more information.

    Args:
        body (str): The text to display in superscript.
        typographic (bool, optional): Whether to prefer the dedicated superscript characters of the font. Defaults to True.
        baseline (str, optional): The baseline shift for synthetic superscripts. Defaults to '-0.5em'.
        size (str, optional): The font size for synthetic superscripts. Defaults to '0.6em'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> superscript('"Hello, World!"')
        '#super("Hello, World!")'
        >>> superscript('[Hello, World!]')
        '#super([Hello, World!])'
        >>> superscript(
        ...     '[Hello, World!]', typographic=False, baseline='-0.4em', size='0.7em'
        ... )
        '#super([Hello, World!], typographic: false, baseline: -0.4em, size: 0.7em)'
    """
    return normal(
        superscript,
        body,
        typographic=typographic,
        baseline=baseline,
        size=size,
    )


@implement(
    True,
    original_name='text',
    hyperlink='https://typst.app/docs/reference/text/text/',
)
def text(
    body: str,
    /,
    *,
    font: str | Iterable[str] = '"libertinus serif"',
    fallback: bool = True,
    style: str = '"normal"',
    weight: str | int = '"regular"',
    stretch: str = '100%',
    size: str = '11pt',
    fill: str = luma('0%'),
    stroke: str | dict[str, Any] | None = None,
    tracking: str = '0pt',
    spacing: str = '100% + 0pt',
    cjk_latin_spacing: str | None = 'auto',
    overhang: bool = True,
    top_edge: str = '"cap-height"',
    bottom_edge: str = '"baseline"',
    lang: str = '"en"',
    region: str | None = None,
    script: str = 'auto',
    dir: str = 'auto',
    hyphenate: str | bool = 'auto',
    costs: dict[str, Any] = dict(
        hyphenation='100%', runt='100%', widow='100%', orphan='100%'
    ),
    kerning: bool = True,
    alternates: bool = False,
    stylistic_set: int | Iterable[int] | None = tuple(),
    ligatures: bool = True,
    discretionary_ligatures: bool = False,
    historical_ligatures: bool = False,
    number_type: str = 'auto',
    number_width: str = 'auto',
    slashed_zero: bool = False,
    fractions: bool = False,
    features: Iterable[str] | dict[str, Any] = dict(),
) -> Block:
    """Interface of `text` in typst. See [the documentation](https://typst.app/docs/reference/text/text/) for more information.

    Args:
        body (str): Content in which all text is styled according to the other arguments.
        font (str | Iterable[str], optional): A font family name or priority list of font family names. Defaults to '"libertinus serif"'.
        fallback (bool, optional): Whether to allow last resort font fallback when the primary font list contains no match. Defaults to True.
        style (str, optional): The desired font style. Defaults to '"normal"'.
        weight (str | int, optional): The desired thickness of the font's glyphs. Defaults to '"regular"'.
        stretch (str, optional): The desired width of the glyphs. Defaults to '100%'.
        size (str, optional): The size of the glyphs. Defaults to '11pt'.
        fill (str, optional): The glyph fill paint. Defaults to luma('0%').
        stroke (str | dict[str, Any] | None, optional): How to stroke the text. Defaults to None.
        tracking (str, optional): The amount of space that should be added between characters. Defaults to '0pt'.
        spacing (str, optional): The amount of space between words. Defaults to '100% + 0pt'.
        cjk_latin_spacing (str | None, optional): Whether to automatically insert spacing between CJK and Latin characters. Defaults to 'auto'.
        overhang (bool, optional): Whether certain glyphs can hang over into the margin in justified text. Defaults to True.
        top_edge (str, optional): The top end of the conceptual frame around the text used for layout and positioning. Defaults to '"cap-height"'.
        bottom_edge (str, optional): The bottom end of the conceptual frame around the text used for layout and positioning. Defaults to '"baseline"'.
        lang (str, optional): An ISO 639-1/2/3 language code. Defaults to '"en"'.
        region (str | None, optional): An ISO 3166-1 alpha-2 region code. Defaults to None.
        script (str, optional): The OpenType writing script. Defaults to 'auto'.
        dir (str, optional): The dominant direction for text and inline objects. Defaults to 'auto'.
        hyphenate (str | bool, optional): Whether to hyphenate text to improve line breaking. Defaults to 'auto'.
        costs (dict[str, Any], optional): The "cost" of various choices when laying out text. Defaults to dict( hyphenation='100%', runt='100%', widow='100%', orphan='100%' ).
        kerning (bool, optional): Whether to apply kerning. Defaults to True.
        alternates (bool, optional): Whether to apply stylistic alternates. Defaults to False.
        stylistic_set (int | Iterable[int] | None, optional): Which stylistic sets to apply. Defaults to tuple().
        ligatures (bool, optional): Whether standard ligatures are active. Defaults to True.
        discretionary_ligatures (bool, optional): Whether ligatures that should be used sparingly are active. Defaults to False.
        historical_ligatures (bool, optional): Whether historical ligatures are active. Defaults to False.
        number_type (str, optional): Which kind of numbers / figures to select. Defaults to 'auto'.
        number_width (str, optional): The width of numbers / figures. Defaults to 'auto'.
        slashed_zero (bool, optional): Whether to have a slash through the zero glyph. Defaults to False.
        fractions (bool, optional): Whether to turn numbers into fractions. Defaults to False.
        features (Iterable[str] | dict[str, Any], optional): Raw OpenType features to apply. Defaults to dict().

    Raises:
        ValueError: If `style` or `weight` or `top_edge` or `bottom_edge` or `number_type` or `number_width` is invalid.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> text('"Hello, World!"')
        '#text("Hello, World!")'
        >>> text('[Hello, World!]')
        '#text([Hello, World!])'
        >>> text('[Hello, World!]', font='"Times New Roman"')
        '#text([Hello, World!], font: "Times New Roman")'
    """
    is_valid(
        lambda: style in map(pad, ('normal', 'italic', 'oblique')),
        lambda: isinstance(weight, int)
        or weight
        in map(
            pad,
            (
                'thin',
                'extralight',
                'light',
                'regular',
                'medium',
                'semibold',
                'bold',
                'extrabold',
                'black',
            ),
        ),
        lambda: top_edge
        in map(pad, ('ascender', 'cap-height', 'x-height', 'baseline', 'bounds')),
        lambda: bottom_edge in map(pad, ('baseline', 'descender', 'bounds')),
        lambda: number_type == 'auto'
        or number_type in map(pad, ('lining', 'old-style')),
        lambda: number_width == 'auto'
        or number_width in map(pad, ('proportional', 'tabular')),
    )
    return normal(
        text,
        body,
        font=font,
        fallback=fallback,
        style=style,
        weight=weight,
        stretch=stretch,
        size=size,
        fill=fill,
        stroke=stroke,
        tracking=tracking,
        spacing=spacing,
        cjk_latin_spacing=cjk_latin_spacing,
        overhang=overhang,
        top_edge=top_edge,
        bottom_edge=bottom_edge,
        lang=lang,
        region=region,
        script=script,
        dir=dir,
        hyphenate=hyphenate,
        costs=costs,
        kerning=kerning,
        alternates=alternates,
        stylistic_set=stylistic_set,
        ligatures=ligatures,
        discretionary_ligatures=discretionary_ligatures,
        historical_ligatures=historical_ligatures,
        number_type=number_type,
        number_width=number_width,
        slashed_zero=slashed_zero,
        fractions=fractions,
        features=features,
    )


@implement(
    True,
    original_name='underline',
    hyperlink='https://typst.app/docs/reference/text/underline/',
)
def underline(
    body: str,
    /,
    *,
    stroke: str | dict[str, Any] = 'auto',
    offset: str = 'auto',
    extent: str = '0pt',
    evade: bool = True,
    background: bool = False,
) -> Block:
    """Interface of `underline` in typst. See [the documentation](https://typst.app/docs/reference/text/underline/) for more information.

    Args:
        body (str): The content to underline.
        stroke (str | dict[str, Any], optional): How to stroke the line. Defaults to 'auto'.
        offset (str, optional): The position of the line relative to the baseline, read from the font tables if auto. Defaults to 'auto'.
        extent (str, optional): The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        evade (bool, optional): Whether the line skips sections in which it would collide with the glyphs. Defaults to True.
        background (bool, optional): Whether the line is placed behind the content it underlines. Defaults to False.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> underline('"Hello, World!"')
        '#underline("Hello, World!")'
        >>> underline('[Hello, World!]')
        '#underline([Hello, World!])'
        >>> underline(
        ...     '[Hello, World!]',
        ...     stroke='1pt + red',
        ...     offset='0pt',
        ...     extent='1pt',
        ...     evade=False,
        ...     background=True,
        ... )
        '#underline([Hello, World!], stroke: 1pt + red, offset: 0pt, extent: 1pt, evade: false, background: true)'
    """
    return normal(
        underline,
        body,
        stroke=stroke,
        offset=offset,
        extent=extent,
        evade=evade,
        background=background,
    )


@implement(
    True,
    original_name='upper',
    hyperlink='https://typst.app/docs/reference/text/upper/',
)
def upper(text: str, /) -> Block:
    """Interface of `upper` in typst. See [the documentation](https://typst.app/docs/reference/text/upper/) for more information.

    Args:
        text (str): The text to convert to uppercase.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> upper('"Hello, World!"')
        '#upper("Hello, World!")'
        >>> upper('[Hello, World!]')
        '#upper([Hello, World!])'
        >>> upper(lower('"Hello, World!"'))
        '#upper(lower("Hello, World!"))'
    """
    return normal(upper, text)
