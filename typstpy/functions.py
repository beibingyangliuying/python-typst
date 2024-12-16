from typing import Optional, overload

from cytoolz.curried import assoc  # type:ignore

from ._utils import (
    RenderType,
    attach_func,
    filter_default_params,
    implement,
    original_name,
    render,
    valid_styles,
)
from .param_types import (
    Alignment,
    Angle,
    Array,
    Auto,
    Block,
    Color,
    Content,
    Function,
    Label,
    Length,
    Ratio,
    Relative,
)

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
        '#rgb(255, 255, 255)'
        >>> rgb(255, 255, 255, 0.5)
        '#rgb(255, 255, 255, 0.5)'
        >>> rgb(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
        '#rgb(50%, 50%, 50%, 50%)'
    """


@overload
def rgb(hex: str) -> Color:
    """Interface of `rgb` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Args:
        hex (str): The color in hexadecimal notation.

    Returns:
        Color: The color in RGB space.

    Examples:
        >>> rgb("#ffffff")
        '#rgb("#ffffff")'
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
        '#rgb(255, 255, 255)'
        >>> rgb(255, 255, 255, 0.5)
        '#rgb(255, 255, 255, 0.5)'
        >>> rgb(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
        '#rgb(50%, 50%, 50%, 50%)'
        >>> rgb("#ffffff")
        '#rgb("#ffffff")'
    """
    _func_name = original_name(rgb)
    if len(args) not in (1, 3, 4):
        raise ValueError(f"Invalid number of arguments: {len(args)}.")
    return rf"#{_func_name}{render(RenderType.VALUE)(args)}"


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
        '#luma(50)'
        >>> luma(50, 0.5)
        '#luma(50, 0.5)'
        >>> luma(Ratio(50), Ratio(50))
        '#luma(50%, 50%)'
    """
    _func_name = original_name(luma)
    if alpha:
        return rf"#{_func_name}{render(RenderType.VALUE)((lightness, alpha))}"
    return rf"#{_func_name}({render(RenderType.VALUE)(lightness)})"


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
        >>> cmyk(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
        '#cmyk(50%, 50%, 50%, 50%)'
    """
    _func_name = original_name(cmyk)
    return rf"#{_func_name}{render(RenderType.VALUE)((cyan, magenta, yellow, key))}"


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
        '#color.linear-rgb(255, 255, 255)'
        >>> color.linear_rgb(255, 255, 255, 0.5)
        '#color.linear-rgb(255, 255, 255, 0.5)'
        >>> color.linear_rgb(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
        '#color.linear-rgb(50%, 50%, 50%, 50%)'
    """
    _func_name = original_name(_color_linear_rgb)
    params = (red, green, blue)
    if alpha:
        params += (alpha,)  # type:ignore
    return rf"#{_func_name}{render(RenderType.VALUE)(params)}"


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
        alpha (Optional[int | Ratio], optional): The alpha component. Defaults to None.

    Returns:
        Color: The color in HSL space.

    Examples:
        >>> color.hsl(Angle.deg(30), Ratio(100), Ratio(50), Ratio(50))
        '#color.hsl(30deg, 100%, 50%, 50%)'
        >>> color.hsl(Angle.deg(30), 100, 50)
        '#color.hsl(30deg, 100, 50)'
    """
    _func_name = original_name(_color_hsl)
    params = (hue, saturation, lightness)
    if alpha:
        params += (alpha,)  # type:ignore
    return rf"#{_func_name}{render(RenderType.VALUE)(params)}"


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
        '#luma(0)'
        >>> color("gray")
        '#luma(170)'
        >>> color("silver")
        '#luma(221)'
        >>> color("white")
        '#luma(255)'
        >>> color("navy")
        '#rgb("#001f3f")'
        >>> color("blue")
        '#rgb("#0074d9")'
        >>> color("aqua")
        '#rgb("#7fdbff")'
        >>> color("teal")
        '#rgb("#39cccc")'
        >>> color("eastern")
        '#rgb("#239dad")'
        >>> color("purple")
        '#rgb("#b10dc9")'
        >>> color("fuchsia")
        '#rgb("#f012be")'
        >>> color("maroon")
        '#rgb("#85144b")'
        >>> color("red")
        '#rgb("#ff4136")'
        >>> color("orange")
        '#rgb("#ff851b")'
        >>> color("yellow")
        '#rgb("#ffdc00")'
        >>> color("olive")
        '#rgb("#3d9970")'
        >>> color("green")
        '#rgb("#2ecc40")'
        >>> color("lime")
        '#rgb("#01ff70")'
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
    format: Auto | str = Auto(),
    width: Auto | Relative = Auto(),
    height: Auto | Relative = Auto(),
    alt: None | str = None,
    fit: str = "cover",
) -> Block:
    """Interface of `image` function in typst. See [the documentation](https://typst.app/docs/reference/visualize/image/) for more information.

    Args:
        path (str): Path to an image file.
        format (Auto | str, optional): The image's format. Options are "png", "jpg", "gif", and "svg". Defaults to Auto().
        width (Auto | Relative, optional): The width of the image. Defaults to Auto().
        height (Auto | Relative, optional): The height of the image. Defaults to Auto().
        alt (None | str, optional): A text describing the image. Defaults to None.
        fit (str, optional): How the image should adjust itself to a given area (the area is defined by the width and height fields). Options are "cover", "contain", and "stretch". Defaults to "cover".

    Returns:
        Block: Executable typst block.

    Examples:
        >>> image("image.png")
        '#image("image.png")'
        >>> image("image.png", format="png")
        '#image("image.png", format: "png")'
        >>> image("image.png", width=Ratio(50))
        '#image("image.png", width: 50%)'
        >>> image("image.png", height=Ratio(50))
        '#image("image.png", height: 50%)'
        >>> image("image.png", alt="An image")
        '#image("image.png", alt: "An image")'
    """
    if isinstance(format, str) and format not in ("png", "jpg", "gif", "svg"):
        raise ValueError(f"Invalid value for format: {format}.")
    if isinstance(fit, str) and fit not in ("cover", "contain", "stretch"):
        raise ValueError(f"Invalid value for fit: {fit}.")
    _func_name = original_name(image)
    params = filter_default_params(
        image,
        {"format": format, "width": width, "height": height, "alt": alt, "fit": fit},
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(path)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"


# endregion
# region model


@implement(
    True,
    original_name="bibliography",
    hyperlink="https://typst.app/docs/reference/model/bibliography/",
)
def bibliography(
    path: str | Array[str],
    *,
    title: None | Auto | Block = Auto(),
    full: bool = False,
    style: str = "ieee",
) -> Block:
    """Interface of `bibliography` function in typst. See [the documentation](https://typst.app/docs/reference/model/bibliography/) for more information.

    Args:
        path (str | Array[str]): Path(s) to Hayagriva .yml and/or BibLaTeX .bib files.
        title (None | Auto | Block, optional): The title of the bibliography. Defaults to Auto().
        full (bool, optional): Whether to include all works from the given bibliography files, even those that weren't cited in the document. Defaults to False.
        style (str, optional): The bibliography style. Defaults to "ieee".

    Raises:
        ValueError: If parameter `style` is not valid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> bibliography("references.bib")
        '#bibliography("references.bib")'
        >>> bibliography("references.bib", title="My Bib")
        '#bibliography("references.bib", title: [My Bib])'
        >>> bibliography("references.bib", title=None)
        '#bibliography("references.bib", title: none)'
        >>> bibliography("references.bib", full=True)
        '#bibliography("references.bib", full: true)'
        >>> bibliography("references.bib", style="annual-reviews")
        '#bibliography("references.bib", style: "annual-reviews")'
        >>> bibliography("references.bib", title="My Bib", full=True, style="annual-reviews")
        '#bibliography("references.bib", title: [My Bib], full: true, style: "annual-reviews")'
    """
    if style and style not in valid_styles():
        raise ValueError(
            rf"Style {style} is not valid. See https://typst.app/docs/reference/model/bibliography/ for available styles."
        )

    _func_name = original_name(bibliography)
    params = filter_default_params(
        bibliography,
        {
            "title": Content(title) if isinstance(title, Block) else title,
            "full": full,
            "style": style,
        },
    )

    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(path)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(path)}, {render(RenderType.DICT)(params)})"


@implement(
    True, original_name="cite", hyperlink="https://typst.app/docs/reference/model/cite/"
)
def cite(
    key: Label,
    *,
    supplement: None | Block = None,
    form: None | str = "normal",
    style: Auto | str = Auto(),
) -> Block:
    """Interface of `cite` function in typst. See [the documentation](https://typst.app/docs/reference/model/cite/) for more information.

    Args:
        key (Label): The citation key that identifies the entry in the bibliography that shall be cited, as a label.
        supplement (None | Block, optional): A supplement for the citation such as page or chapter number. Defaults to None.
        form (None | str, optional): The kind of citation to produce. Different forms are useful in different scenarios: A normal citation is useful as a source at the end of a sentence, while a "prose" citation is more suitable for inclusion in the flow of text. Defaults to "normal".
        style (Auto | str, optional): The citation style. Defaults to Auto().

    Raises:
        ValueError: If parameter `form` or `style` is not valid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> label = Label("Essay")
        >>> cite(label)
        '#cite(<Essay>)'
        >>> cite(label, supplement="1")
        '#cite(<Essay>, supplement: [1])'
        >>> cite(label, form="prose")
        '#cite(<Essay>, form: "prose")'
        >>> cite(label, style="ieee")
        '#cite(<Essay>, style: "ieee")'
        >>> cite(label, supplement="1", form="prose", style="ieee")
        '#cite(<Essay>, supplement: [1], form: "prose", style: "ieee")'
    """
    if form and form not in ("normal", "prose", "full", "author", "year"):
        raise ValueError(
            "Parameter `form` must be one of 'normal','prose','full','author','year'."
        )
    if isinstance(style, str) and style not in valid_styles():
        raise ValueError(
            "See https://typst.app/docs/reference/model/cite/ for available styles."
        )

    _func_name = original_name(cite)
    params = filter_default_params(
        cite,
        {
            "supplement": Content(supplement)
            if isinstance(supplement, Block)
            else supplement,
            "form": form,
            "style": style,
        },
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
        '#emph([Hello, World!])'
        >>> emph(text("Hello, World!", font="Arial", fallback=True))
        '#emph(text(font: "Arial")[Hello, World!])'
    """
    _func_name = original_name(emph)
    _body = Content(body)

    return rf"#{_func_name}({render(RenderType.VALUE)(_body)})"


@implement(
    True,
    original_name="figure.caption",
    hyperlink="https://typst.app/docs/reference/model/figure/#definitions-caption",
)
def _figure_caption(
    body: Block,
    *,
    position: Alignment = Alignment.BOTTOM,
    separator: Auto | Block = Auto(),
) -> Block:
    """Interface of `figure.caption` function in typst. See [the documentation](https://typst.app/docs/reference/model/figure/#definitions-caption) for more information.

    Args:
        body (Block): The caption's body.
        position (Alignment, optional): The caption's position in the figure. Either top or bottom. Defaults to Alignment.BOTTOM.
        separator (Auto | Block, optional): The separator which will appear between the number and body. Defaults to Auto().

    Returns:
        Block: The caption of a `figure`.

    Raises:
        ValueError: If parameter `position` is not valid.

    Examples:
        >>> figure.caption("This is a caption.")
        'This is a caption.'
        >>> figure.caption(strong("This is a caption."))
        '#strong[This is a caption.]'
        >>> figure.caption("This is a caption.", position=Alignment.TOP)
        '#figure.caption(position: top, [This is a caption.])'
        >>> figure.caption(strong("This is a caption."), position=Alignment.TOP)
        '#figure.caption(position: top, strong[This is a caption.])'
        >>> figure.caption("This is a caption.", separator="---")
        '#figure.caption(separator: [---], [This is a caption.])'
        >>> figure.caption("This is a caption.", position=Alignment.TOP, separator="---")
        '#figure.caption(position: top, separator: [---], [This is a caption.])'
    """
    if (
        position and not (Alignment.TOP | Alignment.BOTTOM) & position
    ):  # TODO: Solve problem: Alignment.TOP | Alignment.BOTTOM
        raise ValueError(rf"Invalid value for position: {position}.")

    _func_name = original_name(_figure_caption)
    params = filter_default_params(
        _figure_caption,
        {
            "position": position,
            "separator": Content(separator)
            if isinstance(separator, Block)
            else separator,
        },
    )

    if not params:
        return body
    return rf"#{_func_name}({render(RenderType.DICT)(params)}, {render(RenderType.VALUE)(Content(body))})"


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
    placement: None | Auto | Alignment = None,
    caption: None | Block = None,
    kind: Auto | str | Function = Auto(),
    supplement: None | Auto | Block | Function = Auto(),
    numbering: None | str | Function = "1",
    gap: Length = Length.em(0.65),
    outlined: bool = True,
) -> Block:
    """Interface of `figure` function in typst. See [the documentation](https://typst.app/docs/reference/model/figure/) for more information.

    Args:
        body (Block): The content of the figure. Often, an image.
        label (Optional[Label], optional): Cross-reference for the figure. Defaults to None.
        placement (None | Auto | Alignment, optional): The figure's placement on the page. Defaults to None.
        caption (None | Block, optional): The figure's caption. Defaults to None.
        kind (Auto | str | Function, optional): The kind of figure this is. Defaults to Auto().
        supplement (None | Auto | Block | Function, optional): The figure's supplement. Defaults to Auto().
        numbering (None | str | Function, optional): How to number the figure. Accepts a [numbering pattern or function](https://typst.app/docs/reference/model/numbering/). Defaults to None.
        gap (Optional[Length], optional): The vertical gap between the body and caption. Defaults to Length.em(0.65).
        outlined (bool, optional): Whether the figure should appear in an [outline](https://typst.app/docs/reference/model/outline/) of figures. Defaults to None.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> figure(image("image.png"))
        '#figure(image("image.png"))'
        >>> figure(image("image.png"), Label("fig:Figure"))
        '#figure(image("image.png")) <fig:Figure>'
        >>> figure(image("image.png"), placement=Alignment.TOP)
        '#figure(image("image.png"), placement: top)'
        >>> figure(image("image.png"), caption="This is a caption.")
        '#figure(image("image.png"), caption: [This is a caption.])'
        >>> figure(image("image.png"), caption=figure.caption("This is a caption.", position=Alignment.TOP, separator="---"))
        '#figure(image("image.png"), caption: figure.caption(position: top, separator: [---], [This is a caption.]))'
        >>> figure(image("image.png"), kind="figure")
        '#figure(image("image.png"), kind: "figure")'
        >>> figure(image("image.png"), supplement="Bar")
        '#figure(image("image.png"), supplement: [Bar])'
        >>> figure(image("image.png"), numbering="1.")
        '#figure(image("image.png"), numbering: "1.")'
        >>> figure(image("image.png"), gap=Length.em(0.5))
        '#figure(image("image.png"), gap: 0.5em)'
        >>> figure(image("image.png"), outlined=False)
        '#figure(image("image.png"), outlined: false)'
    """
    _func_name = original_name(figure)
    params = filter_default_params(
        figure,
        {
            "placement": placement,
            "caption": Content(caption) if isinstance(caption, Block) else caption,
            "kind": kind,
            "supplement": Content(supplement)
            if isinstance(supplement, Block)
            else supplement,
            "numbering": numbering,
            "gap": gap,
            "outlined": outlined,
        },
    )
    _body = Content(body)

    if not params:
        result = rf"#{_func_name}({render(RenderType.VALUE)(_body)})"
    else:
        result = rf"#{_func_name}({render(RenderType.VALUE)(_body)}, {render(RenderType.DICT)(params)})"

    if label:
        result += f" {label}"

    return result


@implement(
    True,
    original_name="footnote",
    hyperlink="https://typst.app/docs/reference/model/footnote/",
)
def footnote(body: Label | Block, *, numbering: str | Function = "1") -> Block:
    """Interface of `footnote` function in typst. See [the documentation](https://typst.app/docs/reference/model/footnote/) for more information.

    Args:
        body (Label | Block): The content to put into the footnote. Can also be the label of another footnote this one should point to.
        numbering (str | Function, optional): How to number footnotes. Defaults to "1".

    Returns:
        Block: Executable typst block.

    Examples:
        >>> footnote("Hello, World!")
        '#footnote([Hello, World!])'
        >>> footnote(text("Hello, World!", font="Arial"))
        '#footnote(text(font: "Arial")[Hello, World!])'
    """
    _func_name = original_name(footnote)
    params = filter_default_params(footnote, {"numbering": numbering})
    _body = Content(body) if isinstance(body, Block) else body

    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(_body)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(_body)}, {render(RenderType.DICT)(params)})"


@implement(
    True,
    original_name="heading",
    hyperlink="https://typst.app/docs/reference/model/heading/",
)
def heading(
    body: Block,
    label: Optional[Label] = None,
    *,
    level: Auto | int = Auto(),
    depth: int = 1,
    offset: int = 0,
    numbering: None | str | Function = None,
    supplement: None | Auto | Block | Function = Auto(),
    outlined: bool = True,
    bookmarked: Auto | bool = Auto(),
) -> Block:
    """Interface of `heading` function in typst. See [the documentation](https://typst.app/docs/reference/model/heading/) for more information.

    Args:
        body (Block): The heading's title.
        label (Optional[Label], optional): Cross-reference for the heading. Defaults to None.
        level (Auto | int, optional): The absolute nesting depth of the heading, starting from one. If set to auto, it is computed from offset + depth. Defaults to Auto().
        depth (int, optional): The relative nesting depth of the heading, starting from one. This is combined with offset to compute the actual level. Defaults to 1.
        offset (int, optional): The starting offset of each heading's level, used to turn its relative depth into its absolute level. Defaults to 0.
        numbering (None | str | Function, optional): How to number the heading. Accepts a numbering pattern or function. Defaults to None.
        supplement (None | Auto | Block | Function, optional): A supplement for the heading. Defaults to Auto().
        outlined (bool, optional): Whether the heading should appear in the outline. Defaults to True.
        bookmarked (Auto | bool, optional): Whether the heading should appear as a bookmark in the exported PDF's outline. Doesn't affect other export formats, such as PNG. Defaults to Auto().

    Returns:
        Block: Executable typst block.

    Examples:
        >>> heading("Hello, World!")
        '= Hello, World!'
        >>> heading("Hello, World!", level=2)
        '== Hello, World!'
        >>> heading("Hello, World!", depth=2)
        '== Hello, World!'
        >>> heading("Hello, World!", offset=1)
        '== Hello, World!'
        >>> heading("Hello, World!", level=4, depth=2, offset=1)
        '==== Hello, World!'
        >>> heading("Hello, World!", numbering="a.")
        '#heading(numbering: "a.", level: 1)[Hello, World!]'
        >>> heading("Hello, World!", supplement="Chapter")
        '#heading(supplement: [Chapter], level: 1)[Hello, World!]'
        >>> heading("Hello, World!", outlined=False)
        '#heading(outlined: false, level: 1)[Hello, World!]'
        >>> heading("Hello, World!", bookmarked=False)
        '#heading(bookmarked: false, level: 1)[Hello, World!]'
    """
    if isinstance(level, Auto):
        level = depth + offset
    _func_name = original_name(heading)
    params = filter_default_params(
        heading,
        {
            "numbering": numbering,
            "supplement": Content(supplement)
            if isinstance(supplement, Block)
            else supplement,
            "outlined": outlined,
            "bookmarked": bookmarked,
        },
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
    leading: Length = Length.em(0.65),
    justify: bool = False,
    linebreaks: Auto | str = Auto(),
    first_line_indent: Length = Length.pt(0),
    hanging_indent: Length = Length.pt(0),
) -> Block:
    """Interface of `par` function in typst. See [the documentation](https://typst.app/docs/reference/model/par/) for more information.

    Args:
        body (Block): The contents of the paragraph.
        leading (Length, optional): The spacing between lines. Defaults to Length.em(0.65).
        justify (bool, optional): Whether to justify text in its line. Defaults to False.
        linebreaks (Auto | str, optional): How to determine line breaks. Options are "simple" and "optimized". Defaults to Auto().
        first_line_indent (Length, optional): The indent the first line of a paragraph should have. Defaults to Length.pt(0).
        hanging_indent (Length, optional): The indent all but the first line of a paragraph should have. Defaults to Length.pt(0).

    Raises:
        ValueError: If parameter `linebreaks` is invalid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> par("Hello, World!")
        'Hello, World!'
        >>> par("Hello, World!", leading=Length.em(1.5))
        '#par(leading: 1.5em)[Hello, World!]'
        >>> par("Hello, World!", justify=True)
        '#par(justify: true)[Hello, World!]'
        >>> par("Hello, World!", linebreaks="optimized")
        '#par(linebreaks: "optimized")[Hello, World!]'
        >>> par("Hello, World!", first_line_indent=Length.em(1.5))
        '#par(first-line-indent: 1.5em)[Hello, World!]'
        >>> par("Hello, World!", hanging_indent=Length.em(1.5))
        '#par(hanging-indent: 1.5em)[Hello, World!]'
        >>> par("Hello, World!", leading=Length.em(1.5), justify=True, linebreaks="optimized", first_line_indent=Length.em(1.5), hanging_indent=Length.em(1.5))
        '#par(leading: 1.5em, justify: true, linebreaks: "optimized", first-line-indent: 1.5em, hanging-indent: 1.5em)[Hello, World!]'
    """
    if isinstance(linebreaks, str) and linebreaks not in ("simple", "optimized"):
        raise ValueError(f"Invalid value for linebreaks: {linebreaks}.")
    _func_name = original_name(par)
    params = filter_default_params(
        par,
        {
            "leading": leading,
            "justify": justify,
            "linebreaks": linebreaks,
            "first_line_indent": first_line_indent,
            "hanging_indent": hanging_indent,
        },
    )
    if not params:
        return body
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){Content(body)}"


@implement(
    True, original_name="ref", hyperlink="https://typst.app/docs/reference/model/ref/"
)
def ref(target: Label, *, supplement: None | Auto | Block | Function = Auto()) -> Block:
    """Interface of `ref` function in typst. See [the documentation](https://typst.app/docs/reference/model/ref/) for more information.

    Args:
        target (Label): The target label that should be referenced.
        supplement (None | Auto | Block | Function, optional): A supplement for the reference. Defaults to Auto().

    Returns:
        Block: Executable typst block.

    Examples:
        >>> label = Label("chap:chapter")
        >>> ref(label)
        '#ref(<chap:chapter>)'
        >>> ref(Label("chap:chapter"), supplement="Spam!")
        '#ref(<chap:chapter>, supplement: [Spam!])'
        >>> ref(Label("chap:chapter"), supplement=None)
        '#ref(<chap:chapter>, supplement: none)'
    """
    _func_name = original_name(ref)
    params = filter_default_params(
        ref,
        {
            "supplement": Content(supplement)
            if isinstance(supplement, Block)
            else supplement
        },
    )
    if not params:
        return rf"#{_func_name}({render(RenderType.VALUE)(target)})"
    return rf"#{_func_name}({render(RenderType.VALUE)(target)}, {render(RenderType.DICT)(params)})"


@implement(
    True,
    original_name="strong",
    hyperlink="https://typst.app/docs/reference/model/strong/",
)
def strong(body: Block, *, delta: int = 300) -> Block:
    """Interface of `strong` function in typst. See [the documentation](https://typst.app/docs/reference/model/strong/) for more information.

    Args:
        body (Block): The content to strongly emphasize.
        delta (int, optional): The delta to apply on the font weight. Defaults to 300.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> strong("Hello, World!")
        '#strong[Hello, World!]'
        >>> strong("Hello, World!", delta=400)
        '#strong(delta: 400)[Hello, World!]'
        >>> strong(text("Hello, World!", font="Arial"), delta=400)
        '#strong(delta: 400)[#text(font: "Arial")[Hello, World!]]'
    """
    _func_name = original_name(strong)
    params = filter_default_params(strong, {"delta": delta})
    _body = Content(body)
    if not params:
        return rf"#{_func_name}{_body}"
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){_body}"


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
    original_name="lower",
    hyperlink="https://typst.app/docs/reference/text/lower/",
)
def lower(text: Block) -> Block:
    """Interface of `lower` function in typst. See [the documentation](https://typst.app/docs/reference/text/lower/) for more information.

    Args:
        text (Block): The text to convert to lowercase.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> lower("Hello, World!")
        '#lower([Hello, World!])'
        >>> lower(text("Hello, World!", font="Arial"))
        '#lower(text(font: "Arial")[Hello, World!])'
        >>> lower(emph("Hello, World!"))
        '#lower(emph([Hello, World!]))'
    """
    _func_name = original_name(lower)
    _body = Content(text)
    return rf"#{_func_name}({render(RenderType.VALUE)(_body)})"


@implement(
    True,
    original_name="smallcaps",
    hyperlink="https://typst.app/docs/reference/text/smallcaps/",
)
def smallcaps(body: Block) -> Block:
    """Interface of `smallcaps` function in typst. See [the documentation](https://typst.app/docs/reference/text/smallcaps/) for more information.

    Args:
        body (Block): The content to display in small capitals.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> smallcaps("Hello, World!")
        '#smallcaps([Hello, World!])'
    """
    _func_name = original_name(smallcaps)
    _body = Content(body)
    return rf"#{_func_name}({render(RenderType.VALUE)(_body)})"


@implement(
    True,
    original_name="sub",
    hyperlink="https://typst.app/docs/reference/text/sub/",
)
def sub(
    body: Block,
    *,
    typographic: bool = True,
    baseline: Length = Length.em(0.2),
    size: Length = Length.em(0.6),
) -> Block:
    """Interface of `sub` function in typst. See [the documentation](https://typst.app/docs/reference/text/sub/) for more information.

    Args:
        body (Block): The text to display in subscript.
        typographic (bool, optional): Whether to prefer the dedicated subscript characters of the font. Defaults to True.
        baseline (Length, optional): The baseline shift for synthetic subscripts. Does not apply if typographic is true and the font has subscript codepoints for the given body. Defaults to Length.em(0.2).
        size (Length, optional): The font size for synthetic subscripts. Does not apply if typographic is true and the font has subscript codepoints for the given body. Defaults to Length.em(0.6).

    Returns:
        Block: Executable typst block.

    Examples:
        >>> sub("Hello, World!")
        '#sub[Hello, World!]'
        >>> sub("Hello, World!", typographic=False)
        '#sub(typographic: false)[Hello, World!]'
        >>> sub("Hello, World!", baseline=Length.em(0.4))
        '#sub(baseline: 0.4em)[Hello, World!]'
        >>> sub("Hello, World!", size=Length.em(0.8))
        '#sub(size: 0.8em)[Hello, World!]'
        >>> sub("Hello, World!", typographic=False, baseline=Length.em(0.4), size=Length.em(0.8))
        '#sub(typographic: false, baseline: 0.4em, size: 0.8em)[Hello, World!]'
    """
    _func_name = original_name(sub)
    params = filter_default_params(
        sub, {"typographic": typographic, "baseline": baseline, "size": size}
    )
    _body = Content(body)
    if not params:
        return rf"#{_func_name}{_body}"
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){_body}"


@implement(
    True,
    original_name="super",
    hyperlink="https://typst.app/docs/reference/text/super/",
)
def sup(
    body: Block,
    *,
    typographic: bool = True,
    baseline: Length = Length.em(-0.5),
    size: Length = Length.em(0.6),
) -> Block:
    """Interface of `super` function in typst. See [the documentation](https://typst.app/docs/reference/text/super/) for more information.

    Args:
        body (Block): The text to display in superscript.
        typographic (bool, optional): Whether to prefer the dedicated superscript characters of the font. Defaults to True.
        baseline (Length, optional): The baseline shift for synthetic superscripts. Does not apply if typographic is true and the font has superscript codepoints for the given body. Defaults to -Length.em(0.5).
        size (Length, optional): The font size for synthetic superscripts. Does not apply if typographic is true and the font has superscript codepoints for the given body. Defaults to Length.em(0.6).

    Returns:
        Block: Executable typst block.

    Examples:
        >>> sup("Hello, World!")
        '#super[Hello, World!]'
        >>> sup("Hello, World!", typographic=False)
        '#super(typographic: false)[Hello, World!]'
        >>> sup("Hello, World!", baseline=Length.em(0.4))
        '#super(baseline: 0.4em)[Hello, World!]'
        >>> sup("Hello, World!", size=Length.em(0.8))
        '#super(size: 0.8em)[Hello, World!]'
        >>> sup("Hello, World!", typographic=False, baseline=Length.em(0.4), size=Length.em(0.8))
        '#super(typographic: false, baseline: 0.4em, size: 0.8em)[Hello, World!]'
    """
    _func_name = original_name(sup)
    params = filter_default_params(
        sup, {"typographic": typographic, "baseline": baseline, "size": size}
    )
    _body = Content(body)
    if not params:
        return rf"#{_func_name}{_body}"
    return rf"#{_func_name}({render(RenderType.DICT)(params)}){_body}"


@implement(
    True,
    original_name="text",
    hyperlink="https://typst.app/docs/reference/text/text/",
)
def text(
    body: Block,
    *,
    font: str | Array[str] = "linux libertine",
    fallback: bool = True,
    style: str = "normal",
    weight: int | str = "regular",
    stretch: Ratio = Ratio(100),
    size: Length = Length.pt(11),
    fill: Color = luma(Ratio(0)),
) -> Block:
    """Interface of `text` function in typst. See [the documentation](https://typst.app/docs/reference/text/text/) for more information.

    Args:
        body (Block): Content in which all text is styled according to the other arguments or the text.
        font (str | Array[str], optional): A font family name or priority list of font family names. Defaults to "linux libertine".
        fallback (bool, optional): Whether to allow last resort font fallback when the primary font list contains no match. Defaults to True.
        style (str, optional): The desired font style. Options are "normal", "italic", and "oblique". Defaults to "normal".
        weight (int | str, optional): The desired thickness of the font's glyphs. When passing a string, options are "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black", and "extrablack". Defaults to "regular".
        stretch (Length, optional): The desired width of the glyphs. Defaults to Ratio(100).
        size (Length, optional): The size of the glyphs. Defaults to Length.pt(11).
        fill (Color, optional): The glyph fill paint. Defaults to luma(Ratio(0)).

    Raises:
        ValueError: If parameter `style` or `weight` are not valid.

    Returns:
        Block: Executable typst block.

    Examples:
        >>> text("Hello, World!")
        'Hello, World!'
        >>> text("Hello, World!", font="Arial")
        '#text(font: "Arial")[Hello, World!]'
        >>> text("Hello, World!", font=("Arial", "Times New Roman"))
        '#text(font: ("Arial", "Times New Roman"))[Hello, World!]'
        >>> text("Hello, World!", fallback=False)
        '#text(fallback: false)[Hello, World!]'
        >>> text("Hello, World!", style="italic")
        '#text(style: "italic")[Hello, World!]'
        >>> text("Hello, World!", weight="bold")
        '#text(weight: "bold")[Hello, World!]'
        >>> text("Hello, World!", weight=300)
        '#text(weight: 300)[Hello, World!]'
        >>> text("Hello, World!", stretch=Ratio(50))
        '#text(stretch: 50%)[Hello, World!]'
        >>> text("Hello, World!", size=Length(12, "pt"))
        '#text(size: 12pt)[Hello, World!]'
        >>> text("Hello, World!", fill=color("red"))
        '#text(fill: rgb("#ff4136"))[Hello, World!]'
    """
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
    _func_name = original_name(text)
    params = filter_default_params(
        text,
        {
            "font": font,
            "fallback": fallback,
            "style": style,
            "weight": weight,
            "stretch": stretch,
            "size": size,
            "fill": fill,
        },
    )
    if "fill" in params:
        params["fill"] = Content(params["fill"])
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
def pagebreak(*, weak: bool = False, to: None | str = None) -> Block:
    """Interface of `pagebreak` function in typst. See [the documentation](https://typst.app/docs/reference/layout/pagebreak/) for more information.

    Args:
        weak (bool, optional): If true, the page break is skipped if the current page is already empty. Defaults to False.
        to (None | str, optional): If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary. Defaults to None.

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
    if to and to not in ("even", "odd"):
        raise ValueError(f"Invalid value for to: {to}.")
    _func_name = original_name(pagebreak)
    params = filter_default_params(pagebreak, {"weak": weak, "to": to})
    if not params:
        return rf"#{_func_name}()"
    return rf"#{_func_name}({render(RenderType.DICT)(params)})"


# endregion
