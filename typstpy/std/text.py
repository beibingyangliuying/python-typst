from typing import Any, Iterable, Literal

from typstpy._utils import attach_func, implement, normal, positional
from typstpy.std.visualize import luma, rgb
from typstpy.typings import (
    Alignment,
    Auto,
    Color,
    Content,
    Direction,
    Gradient,
    Length,
    Pattern,
    Ratio,
    RectangleRadius,
    RectangleStroke,
    Relative,
    SmartquoteQuotes,
    Stroke,
    TextCosts,
)


@implement('highlight', 'https://typst.app/docs/reference/text/highlight/')
def highlight(
    body: Content,
    /,
    *,
    fill: None | Color | Gradient | Pattern = rgb('"#fffd11a1"'),
    stroke: None | Length | Color | Gradient | Stroke | Pattern | RectangleStroke = {},
    top_edge: Length
    | Literal[
        '"ascender"', '"cap-height"', '"x-height"', '"baseline"', '"bounds"'
    ] = '"ascender"',
    bottom_edge: Length
    | Literal['"baseline"', '"descender"', '"bounds"'] = '"descender"',
    extent: Length = '0pt',
    radius: Relative | RectangleRadius = {},
) -> Content:
    """Interface of `highlight` in typst. See [the documentation](https://typst.app/docs/reference/text/highlight/) for more information.

    Args:
        body: The content that should be highlighted.
        fill: The color to highlight the text with. Defaults to rgb('"#fffd11a1"').
        stroke: The highlight's border color. Defaults to {}.
        top_edge: The top end of the background rectangle. Defaults to '"ascender"'.
        bottom_edge: The bottom end of the background rectangle. Defaults to '"descender"'.
        extent: The amount by which to extend the background to the sides beyond (or within if negative) the content. Defaults to '0pt'.
        radius: How much to round the highlight's corners. Defaults to {}.

    Raises:
        AssertionError: If `top_edge` or `bottom_edge` is invalid.

    Returns:
        Executable typst code.

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
    assert top_edge in {
        '"ascender"',
        '"cap-height"',
        '"x-height"',
        '"baseline"',
        '"bounds"',
    }
    assert bottom_edge in {'"baseline"', '"descender"', '"bounds"'}

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


@implement('linebreak', 'https://typst.app/docs/reference/text/linebreak/')
def linebreak(*, justify: bool = False) -> Content:
    """Interface of `linebreak` in typst. See [the documentation](https://typst.app/docs/reference/text/linebreak/) for more information.

    Args:
        justify: Whether to justify the line before the break. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> linebreak()
        '#linebreak()'
        >>> linebreak(justify=True)
        '#linebreak(justify: true)'
    """
    return normal(linebreak, justify=justify)


@implement('lorem', 'https://typst.app/docs/reference/text/lorem/')
def lorem(words: int, /) -> Content:
    """Interface of `lorem` in typst. See [the documentation](https://typst.app/docs/reference/text/lorem/) for more information.

    Args:
        words: The length of the blind text in words.

    Returns:
        Executable typst code.

    Examples:
        >>> lorem(10)
        '#lorem(10)'
    """
    return normal(lorem, words)


@implement('lower', 'https://typst.app/docs/reference/text/lower/')
def lower(text: str | Content, /) -> str | Content:
    """Interface of `lower` in typst. See [the documentation](https://typst.app/docs/reference/text/lower/) for more information.

    Args:
        text: The text to convert to lowercase.

    Returns:
        Executable typst code.

    Examples:
        >>> lower('"Hello, World!"')
        '#lower("Hello, World!")'
        >>> lower('[Hello, World!]')
        '#lower([Hello, World!])'
        >>> lower(upper('"Hello, World!"'))
        '#lower(upper("Hello, World!"))'
    """
    return normal(lower, text)


@implement('overline', 'https://typst.app/docs/reference/text/overline/')
def overline(
    body: Content,
    /,
    *,
    stroke: Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Pattern
    | RectangleStroke = 'auto',
    offset: Auto | Length = 'auto',
    extent: Length = '0pt',
    evade: bool = True,
    background: bool = False,
) -> Content:
    """Interface of `overline` in typst. See [the documentation](https://typst.app/docs/reference/text/overline/) for more information.

    Args:
        body: The content to add a line over.
        stroke: How to stroke the line. Defaults to 'auto'.
        offset: The position of the line relative to the baseline. Defaults to 'auto'.
        extent: The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        evade: Whether the line skips sections in which it would collide with the glyphs. Defaults to True.
        background: Whether the line is placed behind the content it overlines. Defaults to False.

    Returns:
        Executable typst code.

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


@implement('raw.line', 'https://typst.app/docs/reference/text/raw/#definitions-line')
def _raw_line(number: int, count: int, text: str, body: Content, /) -> Content:
    """Interface of `raw.line` in typst. See [the documentation](https://typst.app/docs/reference/text/raw/#definitions-line) for more information.

    Args:
        number: The line number of the raw line inside of the raw block, starts at 1.
        count: The total number of lines in the raw block.
        text: The line of raw text.
        body: The highlighted raw text.

    Returns:
        Executable typst code.

    Examples:
        >>> raw.line(1, 1, '"Hello, World!"', '"Hello, World!"')
        '#raw.line(1, 1, "Hello, World!", "Hello, World!")'
    """
    return positional(_raw_line, number, count, text, body)


@attach_func(_raw_line, 'line')
@implement('raw', 'https://typst.app/docs/reference/text/raw/')
def raw(
    text: str,
    /,
    *,
    block: bool = False,
    lang: None | str = None,
    align: Alignment = 'start',
    syntaxes: str | Iterable[str] = tuple(),
    theme: None | Auto | str = 'auto',
    tab_size: int = 2,
) -> Content:
    """Interface of `raw` in typst. See [the documentation](https://typst.app/docs/reference/text/raw/) for more information.

    Args:
        text: The raw text.
        block: Whether the raw text is displayed as a separate block. Defaults to False.
        lang: The language to syntax-highlight in. Defaults to None.
        align: The horizontal alignment that each line in a raw block should have. Defaults to 'start'.
        syntaxes: One or multiple additional syntax definitions to load. Defaults to tuple().
        theme: The theme to use for syntax highlighting. Defaults to 'auto'.
        tab_size: The size for a tab stop in spaces. Defaults to 2.

    Returns:
        Executable typst code.

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


@implement('smallcaps', 'https://typst.app/docs/reference/text/smallcaps/')
def smallcaps(body: Content, /) -> Content:
    """Interface of `smallcaps` in typst. See [the documentation](https://typst.app/docs/reference/text/smallcaps/) for more information.

    Args:
        body: The content to display in small capitals.

    Returns:
        Executable typst code.

    Examples:
        >>> smallcaps('"Hello, World!"')
        '#smallcaps("Hello, World!")'
        >>> smallcaps('[Hello, World!]')
        '#smallcaps([Hello, World!])'
    """
    return normal(smallcaps, body)


@implement('smartquote', 'https://typst.app/docs/reference/text/smartquote/')
def smartquote(
    *,
    double: bool = True,
    enabled: bool = True,
    alternative: bool = False,
    quotes: Auto | str | Iterable[str] | SmartquoteQuotes = 'auto',
) -> Content:
    """Interface of `smartquote` in typst. See [the documentation](https://typst.app/docs/reference/text/smartquote/) for more information.

    Args:
        double: Whether this should be a double quote. Defaults to True.
        enabled: Whether smart quotes are enabled. Defaults to True.
        alternative: Whether to use alternative quotes. Defaults to False.
        quotes: The quotes to use. Defaults to 'auto'.

    Returns:
        Executable typst code.

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


@implement('strike', 'https://typst.app/docs/reference/text/strike/')
def strike(
    body: Content,
    /,
    *,
    stroke: Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Pattern
    | RectangleStroke = 'auto',
    offset: Auto | Length = 'auto',
    extent: Length = '0pt',
    background: bool = False,
) -> Content:
    """Interface of `strike` in typst. See [the documentation](https://typst.app/docs/reference/text/strike/) for more information.

    Args:
        body: The content to strike through.
        stroke: How to stroke the line. Defaults to 'auto'.
        offset: The position of the line relative to the baseline. Defaults to 'auto'.
        extent: The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        background: Whether the line is placed behind the content. Defaults to False.

    Returns:
        Executable typst code.

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


@implement('sub', 'https://typst.app/docs/reference/text/sub/')
def subscript(
    body: Content,
    /,
    *,
    typographic: bool = True,
    baseline: Length = '0.2em',
    size: Length = '0.6em',
) -> Content:
    """Interface of `sub` in typst. See [the documentation](https://typst.app/docs/reference/text/sub/) for more information.

    Args:
        body: The text to display in subscript.
        typographic: Whether to prefer the dedicated subscript characters of the font. Defaults to True.
        baseline: The baseline shift for synthetic subscripts. Defaults to '0.2em'.
        size: The font size for synthetic subscripts. Defaults to '0.6em'.

    Returns:
        Executable typst code.

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


@implement('super', 'https://typst.app/docs/reference/text/super/')
def superscript(
    body: Content,
    /,
    *,
    typographic: bool = True,
    baseline: Length = '-0.5em',
    size: Length = '0.6em',
) -> Content:
    """Interface of `super` in typst. See [the documentation](https://typst.app/docs/reference/text/super/) for more information.

    Args:
        body: The text to display in superscript.
        typographic: Whether to prefer the dedicated superscript characters of the font. Defaults to True.
        baseline: The baseline shift for synthetic superscripts. Defaults to '-0.5em'.
        size: The font size for synthetic superscripts. Defaults to '0.6em'.

    Returns:
        Executable typst code.

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


@implement('text', 'https://typst.app/docs/reference/text/text/')
def text(
    body: str | Content,
    /,
    *,
    font: str | Iterable[str] = '"libertinus serif"',
    fallback: bool = True,
    style: Literal['"normal"', '"italic"', '"oblique"'] = '"normal"',
    weight: int
    | Literal[
        '"thin"',
        '"extralight"',
        '"light"',
        '"regular"',
        '"medium"',
        '"semibold"',
        '"bold"',
        '"extrabold"',
        '"black"',
    ] = '"regular"',
    stretch: Ratio = '100%',
    size: Length = '11pt',
    fill: Color | Gradient | Pattern = luma('0%'),
    stroke: None
    | Length
    | Color
    | Gradient
    | Stroke
    | Pattern
    | RectangleStroke = None,
    tracking: Length = '0pt',
    spacing: Relative = '100% + 0pt',
    cjk_latin_spacing: None | Auto = 'auto',
    overhang: bool = True,
    top_edge: Literal[
        '"ascender"', '"cap-height"', '"x-height"', '"baseline"', '"bounds"'
    ] = '"cap-height"',
    bottom_edge: Literal['"baseline"', '"descender"', '"bounds"'] = '"baseline"',
    lang: str = '"en"',
    region: None | str = None,
    script: Auto | str = 'auto',
    dir: Auto | Direction = 'auto',
    hyphenate: Auto | bool = 'auto',
    costs: TextCosts = {
        'hyphenation': '100%',
        'runt': '100%',
        'widow': '100%',
        'orphan': '100%',
    },
    kerning: bool = True,
    alternates: bool = False,
    stylistic_set: None | int | Iterable[int] = tuple(),
    ligatures: bool = True,
    discretionary_ligatures: bool = False,
    historical_ligatures: bool = False,
    number_type: Auto | Literal['"lining"', '"old-style"'] = 'auto',
    number_width: Auto | Literal['"proportional"', '"tabular"'] = 'auto',
    slashed_zero: bool = False,
    fractions: bool = False,
    features: Iterable[str] | dict[str, Any] = {},
) -> Content:
    """Interface of `text` in typst. See [the documentation](https://typst.app/docs/reference/text/text/) for more information.

    Args:
        body: Content in which all text is styled according to the other arguments.
        font: A font family name or priority list of font family names. Defaults to '"libertinus serif"'.
        fallback: Whether to allow last resort font fallback when the primary font list contains no match. Defaults to True.
        style: The desired font style. Defaults to '"normal"'.
        weight: The desired thickness of the font's glyphs. Defaults to '"regular"'.
        stretch: The desired width of the glyphs. Defaults to '100%'.
        size: The size of the glyphs. Defaults to '11pt'.
        fill: The glyph fill paint. Defaults to luma('0%').
        stroke: How to stroke the text. Defaults to None.
        tracking: The amount of space that should be added between characters. Defaults to '0pt'.
        spacing: The amount of space between words. Defaults to '100% + 0pt'.
        cjk_latin_spacing: Whether to automatically insert spacing between CJK and Latin characters. Defaults to 'auto'.
        overhang: Whether certain glyphs can hang over into the margin in justified text. Defaults to True.
        top_edge: The top end of the conceptual frame around the text used for layout and positioning. Defaults to '"cap-height"'.
        bottom_edge: The bottom end of the conceptual frame around the text used for layout and positioning. Defaults to '"baseline"'.
        lang: An ISO 639-1/2/3 language code. Defaults to '"en"'.
        region: An ISO 3166-1 alpha-2 region code. Defaults to None.
        script: The OpenType writing script. Defaults to 'auto'.
        dir: The dominant direction for text and inline objects. Defaults to 'auto'.
        hyphenate: Whether to hyphenate text to improve line breaking. Defaults to 'auto'.
        costs: The "cost" of various choices when laying out text. Defaults to dict( hyphenation='100%', runt='100%', widow='100%', orphan='100%' ).
        kerning: Whether to apply kerning. Defaults to True.
        alternates: Whether to apply stylistic alternates. Defaults to False.
        stylistic_set: Which stylistic sets to apply. Defaults to tuple().
        ligatures: Whether standard ligatures are active. Defaults to True.
        discretionary_ligatures: Whether ligatures that should be used sparingly are active. Defaults to False.
        historical_ligatures: Whether historical ligatures are active. Defaults to False.
        number_type: Which kind of numbers / figures to select. Defaults to 'auto'.
        number_width: The width of numbers / figures. Defaults to 'auto'.
        slashed_zero: Whether to have a slash through the zero glyph. Defaults to False.
        fractions: Whether to turn numbers into fractions. Defaults to False.
        features: Raw OpenType features to apply. Defaults to {}.

    Raises:
        AssertionError: If `style` or `weight` or `top_edge` or `bottom_edge` or `number_type` or `number_width` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> text('"Hello, World!"')
        '#text("Hello, World!")'
        >>> text('[Hello, World!]')
        '#text([Hello, World!])'
        >>> text('[Hello, World!]', font='"Times New Roman"')
        '#text([Hello, World!], font: "Times New Roman")'
    """
    assert style in {'"normal"', '"italic"', '"oblique"'}
    assert isinstance(weight, int) or weight in {
        '"thin"',
        '"extralight"',
        '"light"',
        '"regular"',
        '"medium"',
        '"semibold"',
        '"bold"',
        '"extrabold"',
        '"black"',
    }
    assert top_edge in {
        '"ascender"',
        '"cap-height"',
        '"x-height"',
        '"baseline"',
        '"bounds"',
    }
    assert bottom_edge in {'"baseline"', '"descender"', '"bounds"'}
    assert number_type == 'auto' or number_type in {'"lining"', '"old-style"'}
    assert number_width == 'auto' or number_width in {'"proportional"', '"tabular"'}

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


@implement('underline', 'https://typst.app/docs/reference/text/underline/')
def underline(
    body: Content,
    /,
    *,
    stroke: Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Pattern
    | RectangleStroke = 'auto',
    offset: Auto | Length = 'auto',
    extent: Length = '0pt',
    evade: bool = True,
    background: bool = False,
) -> Content:
    """Interface of `underline` in typst. See [the documentation](https://typst.app/docs/reference/text/underline/) for more information.

    Args:
        body: The content to underline.
        stroke: How to stroke the line. Defaults to 'auto'.
        offset: The position of the line relative to the baseline, read from the font tables if auto. Defaults to 'auto'.
        extent: The amount by which to extend the line beyond (or within if negative) the content. Defaults to '0pt'.
        evade: Whether the line skips sections in which it would collide with the glyphs. Defaults to True.
        background: Whether the line is placed behind the content it underlines. Defaults to False.

    Returns:
        Executable typst code.

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


@implement('upper', 'https://typst.app/docs/reference/text/upper/')
def upper(text: str | Content, /) -> str | Content:
    """Interface of `upper` in typst. See [the documentation](https://typst.app/docs/reference/text/upper/) for more information.

    Args:
        text: The text to convert to uppercase.

    Returns:
        Executable typst code.

    Examples:
        >>> upper('"Hello, World!"')
        '#upper("Hello, World!")'
        >>> upper('[Hello, World!]')
        '#upper([Hello, World!])'
        >>> upper(lower('"Hello, World!"'))
        '#upper(lower("Hello, World!"))'
    """
    return normal(upper, text)


__all__ = [
    'highlight',
    'linebreak',
    'lorem',
    'lower',
    'overline',
    'raw',
    'smallcaps',
    'smartquote',
    'strike',
    'subscript',
    'superscript',
    'text',
    'underline',
    'upper',
]
