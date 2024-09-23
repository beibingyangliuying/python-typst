from typing import Optional

from cytoolz.curried import assoc, valfilter  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from .param_types import Block, Content, Label, Length, Relative
from .utils import RenderType, attach_func, render


def text(
    content: Block,
    *,
    font: Optional[str | tuple[str]] = None,
    fallback: Optional[bool] = None,
) -> Block:
    """Interface of `text` function in typst.

    Args:
        content (Block): Content in which all text is styled according to the other arguments.
        font (Optional[str  |  tuple[str]], optional): A font family name or priority list of font family names. Defaults to None.
        fallback (Optional[bool], optional): Whether to allow last resort font fallback when the primary font list contains no match. This lets Typst search through all available fonts for the most similar one that has the necessary glyphs. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> print(text("Hello, World!", font="Arial", fallback=True))
        #text(font: "Arial", fallback: true)[Hello, World!]
        >>> print(text("Hello, World!", font=("Arial", "Times New Roman"), fallback=True))
        #text(font: ("Arial", "Times New Roman"), fallback: true)[Hello, World!]
    """
    params = (
        Pipe({"font": font, "fallback": fallback})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return content
    return rf"#text({render(RenderType.DICT)(params)})[{content}]"


def emph(content: Block) -> Block:
    """Interface of `emph` function in typst.

    Args:
        content (Block): The content to emphasize.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> print(emph("Hello, World!"))
        #emph[Hello, World!]
    """
    return rf"#emph[{content}]"


def strong(content: Block, *, delta: Optional[int] = None) -> Block:
    """Interface of `strong` function in typst.

    Args:
        content (Block): The content to strongly emphasize.
        delta (Optional[int], optional): The delta to apply on the font weight. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> print(strong("Hello, World!"))
        #strong[Hello, World!]
        >>> print(strong("Hello, World!", delta=300))
        #strong(delta: 300)[Hello, World!]
    """
    params = Pipe({"delta": delta}).map(valfilter(lambda x: x is not None)).flush()
    if not params:
        return rf"#strong[{content}]"
    return rf"#strong({render(RenderType.DICT)(params)})[{content}]"


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
        >>> print(par("Hello, World!", leading=Length(1.5, "em")))
        #par(leading: 1.5em)[Hello, World!]
        >>> print(par("Hello, World!", justify=True))
        #par(justify: true)[Hello, World!]
        >>> print(par("Hello, World!"))
        Hello, World!
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
    return rf"#par({render(RenderType.DICT)(params)})[{content}]"


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
        >>> print(heading("Hello, World!", level=2, supplement=Content("Chapter"), label=Label("chap:chapter")))
        #heading(supplement: [Chapter], level: 2)[Hello, World!] <chap:chapter>
        >>> print(heading("Hello, World!", level=2))
        == Hello, World!
    """
    params = (
        Pipe({"supplement": supplement, "numbering": numbering})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        result = rf"{"="*level} {content}"
    else:
        result = rf"#heading({render(RenderType.DICT)(assoc(params,'level',level))})[{content}]"
    if label:
        result += f" {label}"
    return result


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
        >>> print(image("image.png"))
        #image("image.png")
        >>> print(image("image.png", format="png"))
        #image("image.png", format: "png")
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


def _figure_caption(content: Block, *, separator: Optional[Content] = None) -> Content:
    """Interface of `figure.caption` function in typst.

    Args:
        content (Block): The caption's body.
        separator (Optional[Content], optional): The separator which will appear between the number and body. Defaults to None.

    Returns:
        Content: The caption's content.
    """
    params = (
        Pipe({"separator": separator}).map(valfilter(lambda x: x is not None)).flush()
    )
    if not params:
        return Content(content)
    return Content(rf"#figure.caption({render(RenderType.DICT)(params)})[{content}]")


@attach_func(_figure_caption, "caption")
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
        >>> print(figure(image("image.png")))
        #figure(image("image.png"))
        >>> print(figure(image("image.png"), caption=Content("This is a figure.")))
        #figure(image("image.png"), caption: [This is a figure.])
        >>> print(figure(image("image.png"), caption=Content("This is a figure."), label=Label("fig:figure")))
        #figure(image("image.png"), caption: [This is a figure.]) <fig:figure>
        >>> print(figure(image("image.png"), caption=figure.caption("This is a figure.", separator=Content("---"))))
        #figure(image("image.png"), caption: figure.caption(separator: [---])[This is a figure.])
    """
    params = Pipe({"caption": caption}).map(valfilter(lambda x: x is not None)).flush()
    if not params:
        result = rf"#figure({Content.examine_sharp(content)})"
    else:
        result = rf"#figure({Content.examine_sharp(content)}, {render(RenderType.DICT)(params)})"
    if label:
        result += f" {label}"
    return result
