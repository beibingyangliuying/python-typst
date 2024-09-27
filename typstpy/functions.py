from typing import Optional, overload

from cytoolz.curried import assoc, memoize, valfilter  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from ._utils import ImplementType, RenderType, attach_func, implement_type, render
from .param_types import (
    Alignment,
    Angle,
    Block,
    Color,
    Content,
    Label,
    Length,
    Ratio,
    Relative,
)


@implement_type(ImplementType.STANDARD)
def text(
    content: Block,
    *,
    font: Optional[str | tuple[str, ...]] = None,
    fallback: Optional[bool] = None,
    style: Optional[str] = None,
    weight: Optional[int | str] = None,
    stretch: Optional[Ratio] = None,
    size: Optional[Length] = None,
    fill: Optional[Color] = None,
) -> Block:
    """Interface of `text` function in typst.

    Args:
        content (Block): Content in which all text is styled according to the other arguments.
        font (Optional[str | tuple[str, ...]], optional): A font family name or priority list of font family names. Defaults to None.
        fallback (Optional[bool], optional): Whether to allow last resort font fallback when the primary font list contains no match. This lets Typst search through all available fonts for the most similar one that has the necessary glyphs. Defaults to None.
        style (Optional[str], optional): The desired font style. Options are "normal", "italic", and "oblique". Defaults to None.
        weight (Optional[int | str], optional): The desired thickness of the font's glyphs. Accepts an integer between 100 and 900 or one of the predefined weight names. When the desired weight is not available, Typst selects the font from the family that is closest in weight. When passing a string, options are "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black", and "extrablack". Defaults to None.
        stretch (Optional[Ratio], optional): The desired width of the glyphs. Accepts a ratio between 50% and 200%. When the desired width is not available, Typst selects the font from the family that is closest in stretch. This will only stretch the text if a condensed or expanded version of the font is available. Defaults to None.
        size (Optional[Length], optional): The size of the glyphs. Defaults to None.
        fill (Optional[Color], optional): The glyph fill paint. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> text("Hello, World!")
        'Hello, World!'
        >>> text("Hello, World!", font="Arial", fallback=True)
        '#text(font: "Arial", fallback: true)[Hello, World!]'
        >>> text("Hello, World!", font=("Arial", "Times New Roman"), fallback=True)
        '#text(font: ("Arial", "Times New Roman"), fallback: true)[Hello, World!]'
        >>> text("Hello, World!", size=Length(12, "pt"))
        '#text(size: 12pt)[Hello, World!]'
        >>> text("Hello, World!", fill=color("red"))
        '#text(fill: rgb("#ff4136"))[Hello, World!]'
        >>> text("Hello, World!", style="italic")
        '#text(style: "italic")[Hello, World!]'
        >>> text("Hello, World!", weight="bold")
        '#text(weight: "bold")[Hello, World!]'
        >>> text("Hello, World!", stretch=Ratio(50))
        '#text(stretch: 50%)[Hello, World!]'
    """
    if style and style not in ("normal", "italic", "oblique"):
        raise ValueError("style must be one of 'normal','italic','oblique'.")
    if isinstance(weight, str) and weight not in (
        "thin",
        "extralight",
        "light",
        "regular",
        "medium",
        "semibold",
        "bold",
        "extrabold",
        "black",
    ):
        raise ValueError(
            "When passing a string, weight must be one of 'thin','extralight','light','regular','medium','semibold','bold','extrabold','black'."
        )
    params = (
        Pipe(
            {
                "font": font,
                "fallback": fallback,
                "style": style,
                "weight": weight,
                "stretch": stretch,
                "size": size,
                "fill": fill,
            }
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return content
    return rf"#text({render(RenderType.DICT)(params)}){Content(content)}"


@implement_type(ImplementType.STANDARD)
def lorem(words: int) -> Block:
    """Interface of `lorem` function in typst.

    Args:
        words (int): The length of the blind text in words.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> lorem(10)
        '#lorem(10)'
    """
    return rf"#lorem({render(RenderType.VALUE)(words)})"


@implement_type(ImplementType.STANDARD)
def emph(content: Block) -> Block:
    """Interface of `emph` function in typst.

    Args:
        content (Block): The content to emphasize.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> emph("Hello, World!")
        '#emph[Hello, World!]'
        >>> emph(text("Hello, World!", font="Arial", fallback=True))
        '#emph[#text(font: "Arial", fallback: true)[Hello, World!]]'
    """
    return rf"#emph{Content(content)}"


@implement_type(ImplementType.STANDARD)
def strong(content: Block, *, delta: Optional[int] = None) -> Block:
    """Interface of `strong` function in typst.

    Args:
        content (Block): The content to strongly emphasize.
        delta (Optional[int], optional): The delta to apply on the font weight. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> strong("Hello, World!")
        '#strong[Hello, World!]'
        >>> strong("Hello, World!", delta=300)
        '#strong(delta: 300)[Hello, World!]'
        >>> strong(text("Hello, World!", font="Arial", fallback=True), delta=300)
        '#strong(delta: 300)[#text(font: "Arial", fallback: true)[Hello, World!]]'
    """
    _content = Content(content)
    params = Pipe({"delta": delta}).map(valfilter(lambda x: x is not None)).flush()
    if not params:
        return rf"#strong{_content}"
    return rf"#strong({render(RenderType.DICT)(params)}){_content}"


@implement_type(ImplementType.STANDARD)
def ref(target: Label) -> Block:
    """Interface of `ref` function in typst.

    Args:
        target (Label): The target label that should be referenced.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> ref(Label("chap:chapter"))
        '#ref(<chap:chapter>)'
    """
    return rf"#ref({target})"


@memoize
def _valid_styles() -> tuple[str, ...]:
    return (
        "annual-reviews",
        "pensoft",
        "annual-reviews-author-date",
        "the-lancet",
        "elsevier-with-titles",
        "gb-7714-2015-author-date",
        "royal-society-of-chemistry",
        "american-anthropological-association",
        "sage-vancouver",
        "british-medical-journal",
        "frontiers",
        "elsevier-harvard",
        "gb-7714-2005-numeric",
        "angewandte-chemie",
        "gb-7714-2015-note",
        "springer-basic-author-date",
        "trends",
        "american-geophysical-union",
        "american-political-science-association",
        "american-psychological-association",
        "cell",
        "spie",
        "harvard-cite-them-right",
        "american-institute-of-aeronautics-and-astronautics",
        "council-of-science-editors-author-date",
        "copernicus",
        "sist02",
        "springer-socpsych-author-date",
        "modern-language-association-8",
        "nature",
        "iso-690-numeric",
        "springer-mathphys",
        "springer-lecture-notes-in-computer-science",
        "future-science",
        "current-opinion",
        "deutsche-gesellschaft-für-psychologie",
        "american-meteorological-society",
        "modern-humanities-research-association",
        "american-society-of-civil-engineers",
        "chicago-notes",
        "institute-of-electrical-and-electronics-engineers",
        "deutsche-sprache",
        "gb-7714-2015-numeric",
        "bristol-university-press",
        "association-for-computing-machinery",
        "associacao-brasileira-de-normas-tecnicas",
        "american-medical-association",
        "elsevier-vancouver",
        "chicago-author-date",
        "vancouver",
        "chicago-fullnotes",
        "turabian-author-date",
        "springer-fachzeitschriften-medizin-psychologie",
        "thieme",
        "taylor-and-francis-national-library-of-medicine",
        "american-chemical-society",
        "american-institute-of-physics",
        "taylor-and-francis-chicago-author-date",
        "gost-r-705-2008-numeric",
        "institute-of-physics-numeric",
        "iso-690-author-date",
        "the-institution-of-engineering-and-technology",
        "american-society-for-microbiology",
        "multidisciplinary-digital-publishing-institute",
        "springer-basic",
        "springer-humanities-author-date",
        "turabian-fullnote-8",
        "karger",
        "springer-vancouver",
        "vancouver-superscript",
        "american-physics-society",
        "mary-ann-liebert-vancouver",
        "american-society-of-mechanical-engineers",
        "council-of-science-editors",
        "american-physiological-society",
        "future-medicine",
        "biomed-central",
        "public-library-of-science",
        "american-sociological-association",
        "modern-language-association",
        "alphanumeric",
    )


@implement_type(ImplementType.STANDARD)
def cite(
    key: Label, *, form: Optional[str] = None, style: Optional[str] = None
) -> Block:
    """Interface of `cite` function in typst.

    Args:
        key (Label): The citation key that identifies the entry in the bibliography that shall be cited, as a label.
        form (Optional[str], optional): The kind of citation to produce. Different forms are useful in different scenarios: A normal citation is useful as a source at the end of a sentence, while a "prose" citation is more suitable for inclusion in the flow of text. Defaults to None.
        style (Optional[str], optional): The citation style. Defaults to None.

    Raises:
        ValueError: If form is not one of "normal","prose","full","author","year" and style is not valid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> cite(Label("Essay1"))
        '#cite(<Essay1>)'
        >>> cite(Label("Essay1"), form="prose")
        '#cite(<Essay1>, form: "prose")'
        >>> cite(Label("Essay1"), style="annual-reviews")
        '#cite(<Essay1>, style: "annual-reviews")'
    """
    if form and form not in ("normal", "prose", "full", "author", "year"):
        raise ValueError("form must be one of 'normal','prose','full','author','year'.")
    if style and style not in _valid_styles():
        raise ValueError(
            "See https://typst.app/docs/reference/model/cite/ for available styles."
        )
    params = (
        Pipe({"form": form, "style": style})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return rf"#cite({key})"
    return rf"#cite({key}, {render(RenderType.DICT)(params)})"


@implement_type(ImplementType.STANDARD)
def bibliography(
    path: str | tuple[str, ...],
    *,
    title: Optional[Content] = None,
    full: Optional[bool] = None,
    style: Optional[str] = None,
) -> Block:
    """Interface of `bibliography` function in typst.

    Args:
        path (str | tuple[str, ...]): Path(s) to Hayagriva .yml and/or BibLaTeX .bib files.
        title (Optional[Content], optional): The title of the bibliography. Defaults to None.
        full (Optional[bool], optional): Whether to include all works from the given bibliography files, even those that weren't cited in the document. Defaults to None.
        style (Optional[str], optional): The bibliography style. Defaults to None.

    Raises:
        ValueError: If style is not valid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> bibliography("bibliography.bib")
        '#bibliography("bibliography.bib")'
        >>> bibliography("bibliography.bib", title="My Bib")
        '#bibliography("bibliography.bib", title: "My Bib")'
        >>> bibliography("bibliography.bib", full=True)
        '#bibliography("bibliography.bib", full: true)'
    """
    if style and style not in _valid_styles():
        raise ValueError(
            "See https://typst.app/docs/reference/model/bibliography/ for available styles."
        )
    params = (
        Pipe({"title": title, "full": full, "style": style})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return rf"#bibliography({render(RenderType.VALUE)(path)})"
    return rf"#bibliography({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"


@implement_type(ImplementType.STANDARD)
def par(
    content: Block,
    *,
    leading: Optional[Length] = None,
    justify: Optional[bool] = None,
    linebreaks: Optional[str] = None,
    first_line_indent: Optional[Length] = None,
    hanging_indent: Optional[Length] = None,
) -> Block:
    """Interface of `par` function in typst.

    Args:
        content (Block): The contents of the paragraph.
        leading (Optional[Length], optional): The spacing between lines. Defaults to None.
        justify (Optional[bool], optional): Whether to justify text in its line. Defaults to None.
        linebreaks (Optional[str], optional): How to determine line breaks. Options are "simple" and "optimized". Defaults to None.
        first_line_indent (Optional[Length], optional): The indent the first line of a paragraph should have. Defaults to None.
        hanging_indent (Optional[Length], optional): The indent all but the first line of a paragraph should have. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> par("Hello, World!", leading=Length(1.5, "em"))
        '#par(leading: 1.5em)[Hello, World!]'
        >>> par("Hello, World!", justify=True)
        '#par(justify: true)[Hello, World!]'
        >>> par("Hello, World!")
        'Hello, World!'
    """
    if linebreaks and linebreaks not in ("simple", "optimized"):
        raise ValueError(f"Invalid value for linebreaks: {linebreaks}.")
    params = (
        Pipe(
            {
                "leading": leading,
                "justify": justify,
                "linebreaks": linebreaks,
                "first_line_indent": first_line_indent,
                "hanging_indent": hanging_indent,
            }
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return content
    return rf"#par({render(RenderType.DICT)(params)}){Content(content)}"


@implement_type(ImplementType.STANDARD)
def pagebreak(*, weak: Optional[bool] = None, to: Optional[str] = None) -> Block:
    """Interface of `pagebreak` function in typst.

    Args:
        weak (Optional[bool], optional): If true, the page break is skipped if the current page is already empty. Defaults to None.
        to (Optional[str], optional): If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary. Defaults to None.

    Raises:
        ValueError: If to is not "even" or "odd".

    Returns:
        Block: Executable typst block.

    Examples:
        >>> pagebreak()
        '#pagebreak()'
        >>> pagebreak(weak=True)
        '#pagebreak(weak: true)'
        >>> pagebreak(to="even")
        '#pagebreak(to: "even")'
        >>> pagebreak(to="odd")
        '#pagebreak(to: "odd")'
        >>> pagebreak(weak=True, to="even")
        '#pagebreak(weak: true, to: "even")'
        >>> pagebreak(weak=True, to="odd")
        '#pagebreak(weak: true, to: "odd")'
    """
    if to and to not in ("even", "odd"):
        raise ValueError(f"Invalid value for to: {to}.")
    params = (
        Pipe({"weak": weak, "to": to}).map(valfilter(lambda x: x is not None)).flush()
    )
    if not params:
        return "#pagebreak()"
    return rf"#pagebreak({render(RenderType.DICT)(params)})"


@implement_type(ImplementType.STANDARD)
def heading(
    content: Block,
    *,
    level: int = 1,
    supplement: Optional[Content] = None,
    numbering: Optional[str] = None,
    label: Optional[Label] = None,
) -> Block:
    """Interface of `heading` function in typst.

    Args:
        content (Block): The heading's title.
        level (int, optional): The absolute nesting depth of the heading, starting from one. Defaults to 1.
        supplement (Optional[Content], optional): A supplement for the heading. Defaults to None.
        numbering (Optional[str], optional): How to number the heading. Defaults to None.
        label (Optional[Label], optional): Cross-reference for the heading. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> heading("Hello, World!", level=2, supplement=Content("Chapter"), label=Label("chap:chapter"))
        '#heading(supplement: [Chapter], level: 2)[Hello, World!] <chap:chapter>'
        >>> heading("Hello, World!", level=2)
        '== Hello, World!'
    """
    params = (
        Pipe({"supplement": supplement, "numbering": numbering})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        result = rf"{"="*level} {content}"
    else:
        result = rf"#heading({render(RenderType.DICT)(assoc(params,'level',level))}){Content(content)}"
    if label:
        result += f" {label}"
    return result


@implement_type(ImplementType.STANDARD)
def image(
    path: str,
    *,
    format: Optional[str] = None,
    width: Optional[Relative] = None,
    height: Optional[Relative] = None,
    alt: Optional[str] = None,
    fit: Optional[str] = None,
) -> Block:
    """Interface of `image` function in typst.

    Args:
        path (str): Path to an image file.
        format (Optional[str], optional): The image's format. Detected automatically by default. Options are "png", "jpg", "gif", and "svg". Defaults to None.
        width (Optional[Relative], optional): The width of the image. Defaults to None.
        height (Optional[Relative], optional): The height of the image. Defaults to None.
        alt (Optional[str], optional): A text describing the image. Defaults to None.
        fit (Optional[str], optional): How the image should adjust itself to a given area (the area is defined by the width and height fields). Note that fit doesn't visually change anything if the area's aspect ratio is the same as the image's one. Options are "cover", "contain", and "stretch". Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> image("image.png")
        '#image("image.png")'
        >>> image("image.png", format="png")
        '#image("image.png", format: "png")'
    """
    if format and format not in ("png", "jpg", "gif", "svg"):
        raise ValueError(f"Invalid value for format: {format}.")
    if fit and fit not in ("cover", "contain", "stretch"):
        raise ValueError(f"Invalid value for fit: {fit}.")
    params = (
        Pipe(
            {"format": format, "width": width, "height": height, "alt": alt, "fit": fit}
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return rf"#image({render(RenderType.VALUE)(path)})"
    return (
        rf"#image({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"
    )


# region figure


@implement_type(ImplementType.STANDARD)
def _caption(
    content: Block,
    *,
    position: Optional[Alignment] = None,
    separator: Optional[Content] = None,
) -> Content:
    """Interface of `figure.caption` function in typst.

    Args:
        content (Block): The caption's body.
        position (Optional[Alignment], optional): The caption's position in the figure. Either top or bottom. Defaults to None.
        separator (Optional[Content], optional): The separator which will appear between the number and body. Defaults to None.

    Returns:
        Content: The caption's content.

    Examples:
        >>> figure.caption("This is a caption.")
        Content(content='This is a caption.')
        >>> figure.caption("This is a caption.", position=Alignment.TOP)
        Content(content='#figure.caption(position: top)[This is a caption.]')
        >>> figure.caption("This is a caption.", position=Alignment.TOP, separator=Content("---"))
        Content(content='#figure.caption(position: top, separator: [---])[This is a caption.]')
    """
    if (
        position and not (Alignment.TOP | Alignment.BOTTOM) & position
    ):  # TODO: Solve problem: Alignment.TOP|Alignment.BOTTOM
        raise ValueError(f"Invalid value for position: {position}.")
    _content = Content(content)
    params = (
        Pipe({"position": position, "separator": separator})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return _content
    return Content(rf"#figure.caption({render(RenderType.DICT)(params)}){_content}")


@attach_func(_caption, _caption.__name__.strip("_"))
@implement_type(ImplementType.STANDARD)
def figure(
    content: Block, *, caption: Optional[Content] = None, label: Optional[Label] = None
) -> Block:
    """Interface of `figure` function in typst.

    Args:
        content (Block): The content of the figure. Often, an image.
        caption (Optional[Content], optional): The figure's caption. Defaults to None.
        label (Optional[Label], optional): Cross-reference for the figure. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> figure(image("image.png"))
        '#figure(image("image.png"))'
        >>> figure(image("image.png"), caption=Content("This is a figure."))
        '#figure(image("image.png"), caption: [This is a figure.])'
        >>> figure(image("image.png"), caption=Content("This is a figure."), label=Label("fig:figure"))
        '#figure(image("image.png"), caption: [This is a figure.]) <fig:figure>'
        >>> figure(image("image.png"), caption=figure.caption("This is a figure.", separator=Content("---")))
        '#figure(image("image.png"), caption: figure.caption(separator: [---])[This is a figure.])'
        >>> figure(image("image.png"), caption=figure.caption("This is a figure.", position=Alignment.TOP, separator=Content("---")))
        '#figure(image("image.png"), caption: figure.caption(position: top, separator: [---])[This is a figure.])'
    """
    _content = Content(content)
    params = Pipe({"caption": caption}).map(valfilter(lambda x: x is not None)).flush()
    if not params:
        result = rf"#figure({render(RenderType.VALUE)(_content)})"
    else:
        result = rf"#figure({render(RenderType.VALUE)(_content)}, {render(RenderType.DICT)(params)})"
    if label:
        result += f" {label}"
    return result


# endregion
# region color


@overload
def rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `rgb` function in typst.

    Args:
        red (int | Ratio): The red component.
        green (int | Ratio): The green component.
        blue (int | Ratio): The blue component.
        alpha (Optional[int | Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in RGB space.

    Examples:
        >>> rgb(255, 255, 255)
        Content(content='#rgb(255, 255, 255)')
        >>> rgb(255, 255, 255, 0.5)
        Content(content='#rgb(255, 255, 255, 0.5)')
    """


@overload
def rgb(hex: str) -> Color:
    """Interface of `rgb` function in typst.

    Args:
        hex (str): The color in hexadecimal notation. Accepts three, four, six or eight hexadecimal digits and optionally a leading hash.

    Returns:
        Color: The color in RGB space.

    Examples:
        >>> rgb("#ffffff")
        Content(content='#rgb("#ffffff")')
    """


@implement_type(ImplementType.STANDARD)
def rgb(*args):
    """
    Examples:
        >>> rgb(255, 255, 255)
        Content(content='#rgb(255, 255, 255)')
        >>> rgb(255, 255, 255, 0.5)
        Content(content='#rgb(255, 255, 255, 0.5)')
        >>> rgb("#ffffff")
        Content(content='#rgb("#ffffff")')
    """
    if len(args) not in (1, 3, 4):
        raise ValueError(f"Invalid number of arguments: {len(args)}.")
    return Color(rf"#rgb{render(RenderType.VALUE)(args)}")


@implement_type(ImplementType.STANDARD)
def luma(lightness: int | Ratio, alpha: Optional[Ratio] = None) -> Color:
    """Interface of `luma` function in typst.

    Args:
        lightness (int | Ratio): The lightness component.
        alpha (Optional[Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in luma space.

    Examples:
        >>> luma(50)
        Content(content='#luma(50)')
        >>> luma(50, 0.5)
        Content(content='#luma(50, 0.5)')
    """
    if alpha:
        return Color(rf"#luma{render(RenderType.VALUE)((lightness, alpha))}")
    return Color(rf"#luma({render(RenderType.VALUE)(lightness)})")


@implement_type(ImplementType.STANDARD)
def cmyk(cyan: Ratio, magenta: Ratio, yellow: Ratio, key: Ratio) -> Color:
    """Interface of `cmyk` function in typst.

    Args:
        cyan (Ratio): The cyan component.
        magenta (Ratio): The magenta component.
        yellow (Ratio): The yellow component.
        key (Ratio): The key component.

    Returns:
        Color: The color in CMYK space.

    Examples:
        >>> cmyk(0, 0, 0, 0)
        Content(content='#cmyk(0, 0, 0, 0)')
        >>> cmyk(0, 0, 0, 0.5)
        Content(content='#cmyk(0, 0, 0, 0.5)')
    """
    return Color(rf"#cmyk{render(RenderType.VALUE)((cyan, magenta, yellow, key))}")


@implement_type(ImplementType.STANDARD)
def _linear_rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `color.linear-rgb` function in typst.

    Args:
        red (int | Ratio): The red component.
        green (int | Ratio): The green component.
        blue (int | Ratio): The blue component.
        alpha (Optional[int  |  Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in linear RGB space.

    Examples:
        >>> color.linear_rgb(255, 255, 255)
        Content(content='#color.linear-rgb(255, 255, 255)')
        >>> color.linear_rgb(255, 255, 255, 0.5)
        Content(content='#color.linear-rgb(255, 255, 255, 0.5)')
    """
    params = (red, green, blue)
    if alpha:
        params += (alpha,)  # type:ignore
    return Color(rf"#color.linear-rgb{render(RenderType.VALUE)(params)}")


@implement_type(ImplementType.STANDARD)
def _hsl(
    hue: Angle,
    saturation: int | Ratio,
    lightness: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `color.hsl` function in typst.

    Args:
        hue (Angle): The hue angle.
        saturation (int | Ratio): The saturation component.
        lightness (int | Ratio): The lightness component.
        alpha (Optional[int  |  Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in HSL space.

    Examples:
        >>> color.hsl(0, 0, 0)
        Content(content='#color.hsl(0, 0, 0)')
        >>> color.hsl(0, 0, 0, 0.5)
        Content(content='#color.hsl(0, 0, 0, 0.5)')
        >>> color.hsl(Ratio(30), Ratio(100), Ratio(50), 0.5)
        Content(content='#color.hsl(30%, 100%, 50%, 0.5)')
    """
    params = (hue, saturation, lightness)
    if alpha:
        params += (alpha,)  # type:ignore
    return Color(rf"#color.hsl{render(RenderType.VALUE)(params)}")


@attach_func(rgb)
@attach_func(luma)
@attach_func(cmyk)
@attach_func(_linear_rgb, _linear_rgb.__name__.strip("_"))
@attach_func(_hsl, _hsl.__name__.strip("_"))
@implement_type(ImplementType.NOTSTANDARD)
def color(name: str) -> Color:
    """Return the corresponding color based on the color name.

    Args:
        name (str): The color name.

    Raises:
        ValueError: Unsupported color name.

    Returns:
        Color: The color in RGB/luma space.

    Examples:
        >>> color("black")
        Content(content='#luma(0)')
        >>> color("gray")
        Content(content='#luma(170)')
        >>> color("silver")
        Content(content='#luma(221)')
        >>> color("white")
        Content(content='#luma(255)')
        >>> color("navy")
        Content(content='#rgb("#001f3f")')
        >>> color("blue")
        Content(content='#rgb("#0074d9")')
        >>> color("aqua")
        Content(content='#rgb("#7fdbff")')
        >>> color("teal")
        Content(content='#rgb("#39cccc")')
        >>> color("eastern")
        Content(content='#rgb("#239dad")')
        >>> color("purple")
        Content(content='#rgb("#b10dc9")')
        >>> color("fuchsia")
        Content(content='#rgb("#f012be")')
        >>> color("maroon")
        Content(content='#rgb("#85144b")')
        >>> color("red")
        Content(content='#rgb("#ff4136")')
        >>> color("orange")
        Content(content='#rgb("#ff851b")')
        >>> color("yellow")
        Content(content='#rgb("#ffdc00")')
        >>> color("olive")
        Content(content='#rgb("#3d9970")')
        >>> color("green")
        Content(content='#rgb("#2ecc40")')
        >>> color("lime")
        Content(content='#rgb("#01ff70")')
    """
    match name:
        case "black":
            return luma(0)
        case "gray":
            return luma(170)
        case "silver":
            return luma(221)
        case "white":
            return luma(255)
        case "navy":
            return rgb("#001f3f")
        case "blue":
            return rgb("#0074d9")
        case "aqua":
            return rgb("#7fdbff")
        case "teal":
            return rgb("#39cccc")
        case "eastern":
            return rgb("#239dad")
        case "purple":
            return rgb("#b10dc9")
        case "fuchsia":
            return rgb("#f012be")
        case "maroon":
            return rgb("#85144b")
        case "red":
            return rgb("#ff4136")
        case "orange":
            return rgb("#ff851b")
        case "yellow":
            return rgb("#ffdc00")
        case "olive":
            return rgb("#3d9970")
        case "green":
            return rgb("#2ecc40")
        case "lime":
            return rgb("#01ff70")
        case _:
            raise ValueError(f"Unsupported color name: {name}.")


# endregion
