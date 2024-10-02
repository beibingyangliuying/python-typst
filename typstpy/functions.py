from typing import Iterable, Optional, overload

from cytoolz.curried import assoc, valfilter  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from ._utils import (
    RenderType,
    attach_func,
    implement,
    original_name,
    render,
    valid_styles,
)
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

# region model


@implement(
    True,
    original_name="bibliography",
    hyperlink="https://typst.app/docs/reference/model/bibliography/",
)
def bibliography(
    path: str | Iterable[str],
    *,
    title: Optional[Content] = None,
    full: Optional[bool] = None,
    style: Optional[str] = None,
) -> Block:
    """Interface of `bibliography` function in typst. See [the documentation](https://typst.app/docs/reference/model/bibliography/) for more information.

    Args:
        path (str | Iterable[str]): Path(s) to Hayagriva .yml and/or BibLaTeX .bib files.
        title (Optional[Content], optional): The title of the bibliography. Defaults to None.
        full (Optional[bool], optional): Whether to include all works from the given bibliography files, even those that weren't cited in the document. Defaults to None.
        style (Optional[str], optional): The bibliography style. Defaults to None.

    Raises:
        ValueError: If parameter `style` is not valid.

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
    _func_name = original_name(bibliography)
    if style and style not in valid_styles():
        raise ValueError(
            f"Style {style} is not valid. See https://typst.app/docs/reference/model/bibliography/ for available styles."
        )
    params = (
        Pipe({"title": title, "full": full, "style": style})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(path)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"


@implement(
    True, original_name="cite", hyperlink="https://typst.app/docs/reference/model/cite/"
)
def cite(
    key: Label, *, form: Optional[str] = None, style: Optional[str] = None
) -> Block:  # TODO: Implement parameter `supplement`.
    """Interface of `cite` function in typst. See [the documentation](https://typst.app/docs/reference/model/cite/) for more information.

    Args:
        key (Label): The citation key that identifies the entry in the bibliography that shall be cited, as a label.
        form (Optional[str], optional): The kind of citation to produce. Different forms are useful in different scenarios: A normal citation is useful as a source at the end of a sentence, while a "prose" citation is more suitable for inclusion in the flow of text. Defaults to None.
        style (Optional[str], optional): The citation style. Defaults to None.

    Raises:
        ValueError: If parameter `form` or `style` is not valid.

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
    _func_name = original_name(cite)
    if form and form not in ("normal", "prose", "full", "author", "year"):
        raise ValueError("form must be one of 'normal','prose','full','author','year'.")
    if style and style not in valid_styles():
        raise ValueError(
            "See https://typst.app/docs/reference/model/cite/ for available styles."
        )
    params = (
        Pipe({"form": form, "style": style})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(key)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(key)}, {render(RenderType.DICT)(params)})"


@implement(
    True, original_name="emph", hyperlink="https://typst.app/docs/reference/model/emph/"
)
def emph(body: Block) -> Block:
    """Interface of `emph` function in typst. See [the documentation](https://typst.app/docs/reference/model/emph/) for more information.

    Args:
        body (Block): The content to emphasize.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> emph("Hello, World!")
        '#emph[Hello, World!]'
        >>> emph(text("Hello, World!", font="Arial", fallback=True))
        '#emph[#text(font: "Arial", fallback: true)[Hello, World!]]'
    """
    _func_name = original_name(emph)
    return rf"#{_func_name}{Content(body)}"


@implement(
    True,
    original_name="figure.caption",
    hyperlink="https://typst.app/docs/reference/model/figure/#definitions-caption",
)
def _figure_caption(
    body: Block,
    *,
    position: Optional[Alignment] = None,
    separator: Optional[Content] = None,
) -> Content:
    """Interface of `figure.caption` function in typst. See [the documentation](https://typst.app/docs/reference/model/figure/#definitions-caption) for more information.

    Args:
        body (Block): The caption's body.
        position (Optional[Alignment], optional): The caption's position in the figure. Either top or bottom. Defaults to None.
        separator (Optional[Content], optional): The separator which will appear between the number and body. Defaults to None.

    Returns:
        Content: The caption's content.

    Raises:
        ValueError: If parameter `position` is not valid.

    Examples:
        >>> figure.caption("This is a caption.")
        Content(content='This is a caption.')
        >>> figure.caption("This is a caption.", position=Alignment.TOP)
        Content(content='#figure.caption(position: top)[This is a caption.]')
        >>> figure.caption("This is a caption.", position=Alignment.TOP, separator=Content("---"))
        Content(content='#figure.caption(position: top, separator: [---])[This is a caption.]')
    """
    _func_name = original_name(_figure_caption)
    if (
        position and not (Alignment.TOP | Alignment.BOTTOM) & position
    ):  # TODO: Solve problem: Alignment.TOP|Alignment.BOTTOM
        raise ValueError(f"Invalid value for position: {position}.")
    _content = Content(body)
    params = (
        Pipe({"position": position, "separator": separator})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return _content
    return Content(rf"#{_func_name}({render(RenderType.DICT)(params)}){_content}")


@attach_func(_figure_caption, "caption")
@implement(
    True,
    original_name="figure",
    hyperlink="https://typst.app/docs/reference/model/figure/",
)
def figure(
    body: Block,
    label: Optional[Label] = None,
    *,
    placement: Optional[Alignment] = None,  # TODO: Solve problem: `Auto`.
    caption: Optional[Content] = None,
    kind: Optional[str] = None,
    supplement: Optional[Content] = None,
    numbering: Optional[str] = None,
    gap: Optional[Length] = None,
    outlined: Optional[bool] = None,
) -> Block:
    """Interface of `figure` function in typst. See [the documentation](https://typst.app/docs/reference/model/figure/) for more information.

    Args:
        body (Block): The content of the figure. Often, an image.
        label (Optional[Label], optional): Cross-reference for the figure. Defaults to None.
        placement (Optional[Alignment], optional): The figure's placement on the page. Defaults to None.
        caption (Optional[Content], optional): The figure's caption. Defaults to None.
        kind (Optional[str], optional): The kind of figure this is. All figures of the same kind share a common counter. If set to auto, the figure will try to automatically determine its kind based on the type of its body. Automatically detected kinds are tables and code. In other cases, the inferred kind is that of an image. Defaults to None.
        supplement (Optional[Content], optional): The figure's supplement. If set to auto, the figure will try to automatically determine the correct supplement based on the kind and the active text language. If you are using a custom figure type, you will need to manually specify the supplement. Defaults to None.
        numbering (Optional[str], optional): How to number the figure. Accepts a numbering pattern or function. Defaults to None.
        gap (Optional[Length], optional): The vertical gap between the body and caption. Defaults to None.
        outlined (Optional[bool], optional): Whether the figure should appear in an outline of figures. Defaults to None.

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
    _func_name = original_name(figure)
    _content = Content(body)
    params = (
        Pipe(
            {
                "placement": placement,
                "caption": caption,
                "kind": kind,
                "supplement": supplement,
                "numbering": numbering,
                "gap": gap,
                "outlined": outlined,
            }
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        result = rf"#{_func_name}({render(RenderType.VALUE)(_content)})"
    else:
        result = rf"#{_func_name}({render(RenderType.VALUE)(_content)}, {render(RenderType.DICT)(params)})"
    if label:
        result += f" {label}"
    return result


@implement(
    True,
    original_name="footnote",
    hyperlink="https://typst.app/docs/reference/model/footnote/",
)
def footnote(body: Label | Content, *, numbering: Optional[str] = None) -> Block:
    """Interface of `footnote` function in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/) for more information.

    Args:
        body (Label | Content): The content to put into the footnote. Can also be the label of another footnote this one should point to.
        numbering (Optional[str], optional): How to number footnotes. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> footnote(Content("Hello, World!"))
        '#footnote([Hello, World!])'
        >>> footnote(Content(text("Hello, World!", font="Arial", fallback=True)))
        '#footnote(text(font: "Arial", fallback: true)[Hello, World!])'
    """
    _func_name = original_name(footnote)
    params = (
        Pipe({"numbering": numbering}).map(valfilter(lambda x: x is not None)).flush()
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(body)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(body)}, {render(RenderType.DICT)(params)})"


@implement(
    True,
    original_name="heading",
    hyperlink="https://typst.app/docs/reference/model/heading/",
)
def heading(
    body: Block,
    label: Optional[Label] = None,
    *,
    level: int = 1,
    depth: Optional[int] = None,
    offset: Optional[int] = None,
    numbering: Optional[str] = None,
    supplement: Optional[Content] = None,
    outlined: Optional[bool] = None,
    bookmarked: Optional[bool] = None,
) -> Block:
    """Interface of `heading` function in typst. See [the documentation](https://typst.app/docs/reference/model/heading/) for more information.

    Args:
        body (Block): The heading's title.
        label (Optional[Label], optional): Cross-reference for the heading. Defaults to None.
        level (int, optional): The absolute nesting depth of the heading, starting from one. If set to auto, it is computed from offset + depth. Defaults to 1.
        depth (Optional[int], optional): The relative nesting depth of the heading, starting from one. This is combined with offset to compute the actual level. Defaults to None.
        offset (Optional[int], optional): The starting offset of each heading's level, used to turn its relative depth into its absolute level. Defaults to None.
        numbering (Optional[str], optional): How to number the heading. Accepts a numbering pattern or function. Defaults to None.
        supplement (Optional[Content], optional): A supplement for the heading. For references to headings, this is added before the referenced number. If a function is specified, it is passed the referenced heading and should return content. Defaults to None.
        outlined (Optional[bool], optional): Whether the heading should appear in the outline. Defaults to None.
        bookmarked (Optional[bool], optional): Whether the heading should appear as a bookmark in the exported PDF's outline. Doesn't affect other export formats, such as PNG. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> heading("Hello, World!", level=2, supplement=Content("Chapter"), label=Label("chap:chapter"))
        '#heading(supplement: [Chapter], level: 2)[Hello, World!] <chap:chapter>'
        >>> heading("Hello, World!", level=2)
        '== Hello, World!'
    """
    _func_name = original_name(heading)
    params = (
        Pipe(
            {
                "depth": depth,
                "offset": offset,
                "numbering": numbering,
                "supplement": supplement,
                "outlined": outlined,
                "bookmarked": bookmarked,
            }
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        result = rf"{"="*level} {body}"
    else:
        result = rf"#{_func_name}({render(RenderType.DICT)(assoc(params,'level',level))}){Content(body)}"
    if label:
        result += f" {label}"
    return result


@implement(
    True, original_name="link", hyperlink="https://typst.app/docs/reference/model/link/"
)
def link(dest: str | Label) -> Block:
    """Interface of `link` function in typst. See [the documentation](https://typst.app/docs/reference/model/link/) for more information.

    Args:
        dest (str | Label): The destination the link points to.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> link("https://typst.app/docs/")
        '#link("https://typst.app/docs/")'
        >>> link(Label("chap:chapter"))
        '#link(<chap:chapter>)'
    """
    _func_name = original_name(link)
    return rf"#{_func_name}({render(RenderType.VALUE)(dest)})"


@implement(
    True, original_name="par", hyperlink="https://typst.app/docs/reference/model/par/"
)
def par(
    body: Block,
    *,
    leading: Optional[Length] = None,
    justify: Optional[bool] = None,
    linebreaks: Optional[str] = None,
    first_line_indent: Optional[Length] = None,
    hanging_indent: Optional[Length] = None,
) -> Block:
    """Interface of `par` function in typst. See [the documentation](https://typst.app/docs/reference/model/par/) for more information.

    Args:
        body (Block): The contents of the paragraph.
        leading (Optional[Length], optional): The spacing between lines. Defaults to None.
        justify (Optional[bool], optional): Whether to justify text in its line. Hyphenation will be enabled for justified paragraphs if the text function's hyphenate property is set to auto and the current language is known. Note that the current alignment still has an effect on the placement of the last line except if it ends with a justified line break. Defaults to None.
        linebreaks (Optional[str], optional): How to determine line breaks. Options are "simple" and "optimized". Defaults to None.
        first_line_indent (Optional[Length], optional): The indent the first line of a paragraph should have. Only the first line of a consecutive paragraph will be indented (not the first one in a block or on the page). Defaults to None.
        hanging_indent (Optional[Length], optional): The indent all but the first line of a paragraph should have. Defaults to None.

    Raises:
        ValueError: If parameter `linebreaks` is invalid.

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
    _func_name = original_name(par)
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
        return body
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){Content(body)}"


@implement(
    True, original_name="ref", hyperlink="https://typst.app/docs/reference/model/ref/"
)
def ref(target: Label, *, supplement: Optional[Content] = None) -> Block:
    """Interface of `ref` function in typst. See [the documentation](https://typst.app/docs/reference/model/ref/) for more information.

    Args:
        target (Label): The target label that should be referenced. Can be a label that is defined in the document or an entry from the bibliography.
        supplement (Optional[Content], optional): A supplement for the reference. For references to headings or figures, this is added before the referenced number. For citations, this can be used to add a page number. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> ref(Label("chap:chapter"))
        '#ref(<chap:chapter>)'
        >>> ref(Label("chap:chapter"), supplement=Content("Hello, World!"))
        '#ref(<chap:chapter>, supplement: [Hello, World!])'
    """
    _func_name = original_name(ref)
    params = (
        Pipe({"supplement": supplement}).map(valfilter(lambda x: x is not None)).flush()
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(target)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(target)}, {render(RenderType.DICT)(params)})"


@implement(
    True,
    original_name="strong",
    hyperlink="https://typst.app/docs/reference/model/strong/",
)
def strong(body: Block, *, delta: Optional[int] = None) -> Block:
    """Interface of `strong` function in typst. See [the documentation](https://typst.app/docs/reference/model/strong/) for more information.

    Args:
        body (Block): The content to strongly emphasize.
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
    _content = Content(body)
    _func_name = original_name(strong)
    params = Pipe({"delta": delta}).map(valfilter(lambda x: x is not None)).flush()
    if not params:
        return rf"#{_func_name}{_content}"
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){_content}"


# endregion
# region text


@implement(
    True,
    original_name="lorem",
    hyperlink="https://typst.app/docs/reference/text/lorem/",
)
def lorem(words: int) -> Block:
    """Interface of `lorem` function in typst. See [the documentation](https://typst.app/docs/reference/text/lorem/) for more information.

    Args:
        words (int): The length of the blind text in words.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> lorem(10)
        '#lorem(10)'
    """
    _func_name = original_name(lorem)
    return rf"#{_func_name}({render(RenderType.VALUE)(words)})"


@implement(
    True,
    original_name="text",
    hyperlink="https://typst.app/docs/reference/text/text/",
)
def text(
    body: Block,
    *,
    font: Optional[str | Iterable[str]] = None,
    fallback: Optional[bool] = None,
    style: Optional[str] = None,
    weight: Optional[int | str] = None,
    stretch: Optional[Ratio] = None,
    size: Optional[Length] = None,
    fill: Optional[Color] = None,
) -> Block:
    """Interface of `text` function in typst. See [the documentation](https://typst.app/docs/reference/text/text/) for more information.

    Args:
        body (Block): Content in which all text is styled according to the other arguments or the text.
        font (Optional[str | Iterable[str]], optional): A font family name or priority list of font family names. Defaults to None.
        fallback (Optional[bool], optional): Whether to allow last resort font fallback when the primary font list contains no match. This lets Typst search through all available fonts for the most similar one that has the necessary glyphs. Defaults to None.
        style (Optional[str], optional): The desired font style. Options are "normal", "italic", and "oblique". Defaults to None.
        weight (Optional[int | str], optional): The desired thickness of the font's glyphs. Accepts an integer between 100 and 900 or one of the predefined weight names. When the desired weight is not available, Typst selects the font from the family that is closest in weight. When passing a string, options are "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black", and "extrablack". Defaults to None.
        stretch (Optional[Ratio], optional): The desired width of the glyphs. Accepts a ratio between 50% and 200%. When the desired width is not available, Typst selects the font from the family that is closest in stretch. This will only stretch the text if a condensed or expanded version of the font is available. Defaults to None.
        size (Optional[Length], optional): The size of the glyphs. Defaults to None.
        fill (Optional[Color], optional): The glyph fill paint. Defaults to None.

    Raises:
        ValueError: If parameter `style` or `weight` are not valid.

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
    _func_name = original_name(text)
    if style and style not in {"normal", "italic", "oblique"}:
        raise ValueError(
            "Parameter `style` must be one of 'normal', 'italic', and 'oblique'."
        )
    if isinstance(weight, str) and weight not in {
        "thin",
        "extralight",
        "light",
        "regular",
        "medium",
        "semibold",
        "bold",
        "extrabold",
        "black",
    }:
        raise ValueError(
            "When passing a string, weight must be one of 'thin', 'extralight', 'light', 'regular', 'medium', 'semibold', 'bold', 'extrabold', and 'black'."
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
        return body
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){Content(body)}"


# endregion
# region layout


@implement(
    True,
    original_name="pagebreak",
    hyperlink="https://typst.app/docs/reference/layout/pagebreak/",
)
def pagebreak(*, weak: Optional[bool] = None, to: Optional[str] = None) -> Block:
    """Interface of `pagebreak` function in typst. See [the documentation](https://typst.app/docs/reference/layout/pagebreak/) for more information.

    Args:
        weak (Optional[bool], optional): If true, the page break is skipped if the current page is already empty. Defaults to None.
        to (Optional[str], optional): If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary. Defaults to None.

    Raises:
        ValueError: If parameter `to` is not valid.

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
    _func_name = original_name(pagebreak)
    if to and to not in ("even", "odd"):
        raise ValueError(f"Invalid value for to: {to}.")
    params = (
        Pipe({"weak": weak, "to": to}).map(valfilter(lambda x: x is not None)).flush()
    )
    if not params:
        return rf"#{_func_name}()"
    return rf"#{_func_name}({render(RenderType.DICT)(params)})"


# endregion
# region visualize


@overload
def rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `rgb` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

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
    """Interface of `rgb` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Args:
        hex (str): The color in hexadecimal notation. Accepts three, four, six or eight hexadecimal digits and optionally a leading hash.

    Returns:
        Color: The color in RGB space.

    Examples:
        >>> rgb("#ffffff")
        Content(content='#rgb("#ffffff")')
    """


@implement(
    True,
    original_name="rgb",
    hyperlink="https://typst.app/docs/reference/visualize/color/#definitions-rgb",
)
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
    _func_name = original_name(rgb)
    if len(args) not in (1, 3, 4):
        raise ValueError(f"Invalid number of arguments: {len(args)}.")
    return Color(rf"#{_func_name}{render(RenderType.VALUE)(args)}")


@implement(
    True,
    original_name="luma",
    hyperlink="https://typst.app/docs/reference/visualize/color/#definitions-luma",
)
def luma(lightness: int | Ratio, alpha: Optional[Ratio] = None) -> Color:
    """Interface of `luma` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-luma) for more information.

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
    _func_name = original_name(luma)
    if alpha:
        return Color(rf"#{_func_name}{render(RenderType.VALUE)((lightness, alpha))}")
    return Color(rf"#{_func_name}({render(RenderType.VALUE)(lightness)})")


@implement(
    True,
    original_name="cmyk",
    hyperlink="https://typst.app/docs/reference/visualize/color/#definitions-cmyk",
)
def cmyk(cyan: Ratio, magenta: Ratio, yellow: Ratio, key: Ratio) -> Color:
    """Interface of `cmyk` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) for more information.

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
    _func_name = original_name(cmyk)
    return Color(
        rf"#{_func_name}{render(RenderType.VALUE)((cyan, magenta, yellow, key))}"
    )


@implement(
    True,
    original_name="color.linear-rgb",
    hyperlink="https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb",
)
def _color_linear_rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `color.linear-rgb` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) for more information.

    Args:
        red (int | Ratio): The red component.
        green (int | Ratio): The green component.
        blue (int | Ratio): The blue component.
        alpha (Optional[int | Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in linear RGB space.

    Examples:
        >>> color.linear_rgb(255, 255, 255)
        Content(content='#color.linear-rgb(255, 255, 255)')
        >>> color.linear_rgb(255, 255, 255, 0.5)
        Content(content='#color.linear-rgb(255, 255, 255, 0.5)')
    """
    _func_name = original_name(_color_linear_rgb)
    params = (red, green, blue)
    if alpha:
        params += (alpha,)  # type:ignore
    return Color(rf"#{_func_name}{render(RenderType.VALUE)(params)}")


@implement(
    True,
    original_name="color.hsl",
    hyperlink="https://typst.app/docs/reference/visualize/color/#definitions-hsl",
)
def _color_hsl(
    hue: Angle,
    saturation: int | Ratio,
    lightness: int | Ratio,
    alpha: Optional[int | Ratio] = None,
) -> Color:
    """Interface of `color.hsl` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-hsl) for more information.

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
    _func_name = original_name(_color_hsl)
    params = (hue, saturation, lightness)
    if alpha:
        params += (alpha,)  # type:ignore
    return Color(rf"#{_func_name}{render(RenderType.VALUE)(params)}")


@attach_func(rgb)
@attach_func(luma)
@attach_func(cmyk)
@attach_func(_color_linear_rgb, "linear_rgb")
@attach_func(_color_hsl, "hsl")
@implement(False)
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


@implement(
    True,
    original_name="image",
    hyperlink="https://typst.app/docs/reference/visualize/image/",
)
def image(
    path: str,
    *,
    format: Optional[str] = None,
    width: Optional[Relative] = None,
    height: Optional[Relative] = None,
    alt: Optional[str] = None,
    fit: Optional[str] = None,
) -> Block:
    """Interface of `image` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/image/) for more information.

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
    _func_name = original_name(image)
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
        return rf"#{_func_name}({render(RenderType.VALUE)(path)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"


# endregion
