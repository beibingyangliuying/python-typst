from typing import Optional

from cytoolz.curried import valfilter  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from param_types import Content, Label, Length, Relative
from utils import RenderType, examine_sharp, render


def text(
    content: str,
    *,
    font: Optional[str | tuple[str]] = None,
    fallback: Optional[bool] = None,
) -> str:
    """_summary_

    Args:
        content (str): _description_
        font (Optional[str  |  tuple[str]], optional): _description_. Defaults to None.
        fallback (Optional[bool], optional): _description_. Defaults to None.

    Returns:
        str: _description_

    Examples:
        >>> text("Hello, World!", font="Arial", fallback=True)
        '#text(font: "Arial", fallback: true)[Hello, World!]'
        >>> text("Hello, World!", font=("Arial", "Times New Roman"), fallback=True)
        '#text(font: ("Arial", "Times New Roman"), fallback: true)[Hello, World!]'
    """
    params = (
        Pipe({"font": font, "fallback": fallback})
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    if not params:
        return content
    return rf"#text({render(RenderType.DICT)(params)})[{content}]"


def emph(content: str) -> str:
    """_summary_

    Args:
        content (str): _description_

    Returns:
        str: _description_

    Examples:
        >>> emph("Hello, World!")
        '#emph[Hello, World!]'
    """
    return rf"#emph[{content}]"


def strong(content: str) -> str:
    """_summary_

    Args:
        content (str): _description_

    Returns:
        str: _description_

    Examples:
        >>> strong("Hello, World!")
        '#strong[Hello, World!]'
    """
    return rf"#strong[{content}]"


def par(
    content: str,
    *,
    leading: Optional[Length] = None,
    justify: Optional[bool] = None,
    linebreaks: Optional[str] = None,
    first_line_indent: Optional[Length] = None,
    hanging_indent: Optional[Length] = None,
) -> str:
    """_summary_

    Args:
        content (str): _description_
        leading (Optional[Length], optional): _description_. Defaults to None.
        justify (Optional[bool], optional): _description_. Defaults to None.
        linebreaks (Optional[str], optional): _description_. Defaults to None.
        first_line_indent (Optional[Length], optional): _description_. Defaults to None.
        hanging_indent (Optional[Length], optional): _description_. Defaults to None.

    Returns:
        str: _description_

    Examples:
        >>> par("Hello, World!", leading=Length(1.5, "em"))
        '#par(leading: 1.5em)[Hello, World!]'
    """
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


def image(
    path: str,
    *,
    format: Optional[str] = None,
    width: Optional[Relative] = None,
    height: Optional[Relative] = None,
    alt: Optional[str] = None,
    fit: Optional[str] = None,
) -> str:
    """_summary_

    Args:
        path (str): _description_
        format (Optional[str], optional): _description_. Defaults to None.
        width (Optional[Relative], optional): _description_. Defaults to None.
        height (Optional[Relative], optional): _description_. Defaults to None.
        alt (Optional[str], optional): _description_. Defaults to None.
        fit (Optional[str], optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    params = (
        Pipe(
            {"format": format, "width": width, "height": height, "alt": alt, "fit": fit}
        )
        .map(valfilter(lambda x: x is not None))
        .flush()
    )
    return (
        rf"#image({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"
    )


def figure(
    content: str, *, caption: Optional[Content] = None, label: Optional[Label] = None
) -> str:
    """_summary_

    Args:
        content (str): _description_
        caption (Optional[Content], optional): _description_. Defaults to None.
        label (Optional[Label], optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    params = Pipe({"caption": caption}).map(valfilter(lambda x: x is not None)).flush()
    result = rf"#figure({examine_sharp(content)}, {render(RenderType.DICT)(params)})"
    if label:
        result += str(label)
    return result
