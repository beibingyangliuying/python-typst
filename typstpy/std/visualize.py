# pylint: disable = W0102, W0611, R0913, R0914, R1735, C0302

from typing import Any, Optional, Sequence, overload

from deprecated import deprecated  # type: ignore[import-untyped]

from typstpy._core import (
    attach_func,
    implement,
    instance,
    normal,
    positional,
    post_series,
    pre_series,
)
from typstpy.typings import (
    Angle,
    Auto,
    BoxInset,
    BoxOutset,
    Color,
    Content,
    Fraction,
    Function,
    Gradient,
    Length,
    Literal,
    Ratio,
    RectangleRadius,
    RectangleStroke,
    Relative,
    Stroke,
    Tiling,
)


@implement('circle', 'https://typst.app/docs/reference/visualize/circle/')
def circle(
    body: None | Content = '',
    *,
    radius: Length = '0pt',
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Function = 'auto',
    fill: None | Color | Gradient | Tiling = None,
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = 'auto',
    inset: Relative | BoxInset = '0% + 5pt',
    outset: Relative | BoxOutset = {},
):
    """Interface of `circle` in typst. See [the documentation](https://typst.app/docs/reference/visualize/circle/) for more information.

    Args:
        body: The content to place into the circle. Defaults to ''.
        radius: The circle's radius. Defaults to '0pt'.
        width: The circle's width. Defaults to 'auto'.
        height: The circle's height. Defaults to 'auto'.
        fill: How to fill the circle. Defaults to None.
        stroke: How to stroke the circle. Defaults to 'auto'.
        inset: How much to pad the circle's content. Defaults to '0% + 5pt'.
        outset: How much to expand the circle's size without affecting the layout. Defaults to {}.

    Raises:
        AssertionError: If `radius` is not '0pt' and either `width` or `height` is not 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> circle('[Hello, world!]')
        '#circle([Hello, world!])'
        >>> circle('[Hello, world!]', radius='10pt')
        '#circle([Hello, world!], radius: 10pt)'
        >>> circle('[Hello, world!]', width='100%', height='100%')
        '#circle([Hello, world!], width: 100%, height: 100%)'
    """
    assert (width == 'auto' and height == 'auto') if radius != '0pt' else True

    return normal(
        circle,
        body,
        radius=radius,
        width=width,
        height=height,
        fill=fill,
        stroke=stroke,
        inset=inset,
        outset=outset,
    )


@implement(
    'color.map',
    'https://typst.app/docs/reference/visualize/color/#predefined-color-maps',
)
def _color_map(name: str, /) -> Color:
    """Interface of `color.map` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#predefined-color-maps) for more information.

    Args:
        name: The name of the color map.

    Raises:
        AssertionError: If `name` is invalid.

    Returns:
        A color in a specific color space.

    Examples:
        >>> color.map('turbo')
        '#color.map.turbo'
    """
    assert name in {
        'turbo',
        'cividis',
        'rainbow',
        'spectral',
        'viridis',
        'inferno',
        'magma',
        'plasma',
        'rocket',
        'mako',
        'vlag',
        'icefire',
        'flare',
        'crest',
    }
    return f'#color.map.{name}'


@implement('luma', 'https://typst.app/docs/reference/visualize/color/#definitions-luma')
def luma(lightness: Ratio | int, alpha: Optional[Ratio] = None, /) -> Color:
    """Interface of `luma` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-luma) for more information.

    Args:
        lightness: The lightness component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> luma('50%')
        '#luma(50%)'
        >>> luma('50%', '50%')
        '#luma(50%, 50%)'
    """
    return positional(luma, *([lightness] if alpha is None else [lightness, alpha]))


@implement(
    'oklab', 'https://typst.app/docs/reference/visualize/color/#definitions-oklab'
)
def oklab(
    lightness: Ratio,
    a: float | Ratio,
    b: float | Ratio,
    alpha: Optional[Ratio] = None,
    /,
) -> Color:
    """Interface of `oklab` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-oklab) for more information.

    Args:
        lightness: The lightness component.
        a: The a ("green/red") component.
        b: The b ("blue/yellow") component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> oklab('50%', '0%', '0%')
        '#oklab(50%, 0%, 0%)'
        >>> oklab('50%', '0%', '0%', '50%')
        '#oklab(50%, 0%, 0%, 50%)'
    """
    return positional(
        oklab,
        *([lightness, a, b] if alpha is None else [lightness, a, b, alpha]),
    )


@implement(
    'oklch', 'https://typst.app/docs/reference/visualize/color/#definitions-oklch'
)
def oklch(
    lightness: Ratio,
    chroma: float | Ratio,
    hue: Angle,
    alpha: Optional[Ratio] = None,
    /,
) -> Color:
    """Interface of `oklch` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-oklch) for more information.

    Args:
        lightness: The lightness component.
        chroma: The chroma component.
        hue: The hue component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> oklch('50%', '0%', '0deg')
        '#oklch(50%, 0%, 0deg)'
        >>> oklch('50%', '0%', '0deg', '50%')
        '#oklch(50%, 0%, 0deg, 50%)'
    """
    return positional(
        oklch,
        *(
            [lightness, chroma, hue]
            if alpha is None
            else [lightness, chroma, hue, alpha]
        ),
    )


@implement(
    'color.linear-rgb',
    'https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb',
)
def _color_linear_rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
    /,
) -> Color:
    """Interface of `color.linear-rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) for more information.

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> color.linear_rgb(255, 255, 255)
        '#color.linear-rgb(255, 255, 255)'
        >>> color.linear_rgb('50%', '50%', '50%', '50%')
        '#color.linear-rgb(50%, 50%, 50%, 50%)'
    """
    return positional(
        _color_linear_rgb,
        *([red, green, blue] if alpha is None else [red, green, blue, alpha]),
    )


@overload
def rgb(
    red: int | Ratio,
    green: int | Ratio,
    blue: int | Ratio,
    alpha: Optional[int | Ratio] = None,
    /,
) -> Color:
    """Interface of `rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> rgb(255, 255, 255)
        '#rgb(255, 255, 255)'
    """


@overload
def rgb(hex: str, /) -> Color:
    """Interface of `rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Args:
        hex: The color in hexadecimal notation.

    Returns:
        A color in a specific color space.

    Examples:
        >>> rgb('"#ffffff"')
        '#rgb("#ffffff")'
    """


@implement('rgb', 'https://typst.app/docs/reference/visualize/color/#definitions-rgb')
def rgb(*args):
    """Interface of `rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Raises:
        AssertionError: If the number of arguments is not 1, 3, or 4.

    Returns:
        A color in a specific color space.

    Examples:
        >>> rgb(255, 255, 255)
        '#rgb(255, 255, 255)'
        >>> rgb('50%', '50%', '50%', '50%')
        '#rgb(50%, 50%, 50%, 50%)'
        >>> rgb('"#ffffff"')
        '#rgb("#ffffff")'
    """
    assert len(args) in (1, 3, 4)

    return positional(rgb, *args)  # type: ignore


@implement('cmyk', 'https://typst.app/docs/reference/visualize/color/#definitions-cmyk')
def cmyk(cyan: Ratio, magenta: Ratio, yellow: Ratio, key: Ratio, /) -> Color:
    """Interface of `cmyk` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) for more information.

    Args:
        cyan: The cyan component.
        magenta: The magenta component.
        yellow: The yellow component.
        key: The key component.

    Returns:
        A color in a specific color space.

    Examples:
        >>> cmyk('0%', '0%', '0%', '0%')
        '#cmyk(0%, 0%, 0%, 0%)'
        >>> cmyk('50%', '50%', '50%', '50%')
        '#cmyk(50%, 50%, 50%, 50%)'
    """
    return positional(cmyk, cyan, magenta, yellow, key)


@implement(
    'color.hsl', 'https://typst.app/docs/reference/visualize/color/#definitions-hsl'
)
def _color_hsl(
    hue: Angle,
    saturation: int | Ratio,
    lightness: int | Ratio,
    alpha: Optional[int | Ratio] = None,
    /,
) -> Color:
    """Interface of `color.hsl` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-hsl) for more information.

    Args:
        hue: The hue angle.
        saturation: The saturation component.
        lightness: The lightness component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> color.hsl('0deg', '50%', '50%', '50%')
        '#color.hsl(0deg, 50%, 50%, 50%)'
        >>> color.hsl('0deg', '50%', '50%')
        '#color.hsl(0deg, 50%, 50%)'
    """
    return positional(
        _color_hsl,
        *(
            [hue, saturation, lightness]
            if alpha is None
            else [hue, saturation, lightness, alpha]
        ),
    )


@implement(
    'color.hsv', 'https://typst.app/docs/reference/visualize/color/#definitions-hsv'
)
def _color_hsv(
    hue: Angle,
    saturation: int | Ratio,
    value: int | Ratio,
    alpha: Optional[int | Ratio] = None,
    /,
) -> Color:
    """Interface of `color.hsv` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-hsv) for more information.

    Args:
        hue: The hue angle.
        saturation: The saturation component.
        value: The value component.
        alpha: The alpha component. Defaults to None.

    Returns:
        A color in a specific color space.

    Examples:
        >>> color.hsv('0deg', '50%', '50%', '50%')
        '#color.hsv(0deg, 50%, 50%, 50%)'
        >>> color.hsv('0deg', '50%', '50%')
        '#color.hsv(0deg, 50%, 50%)'
    """
    return positional(
        _color_hsv,
        *(
            [hue, saturation, value]
            if alpha is None
            else [hue, saturation, value, alpha]
        ),
    )


@implement(
    'components',
    'https://typst.app/docs/reference/visualize/color/#definitions-components',
)
def _color_components(self: Color, /, *, alpha: bool = True):
    """Interface of `color.components` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-components) for more information.

    Args:
        self: A color in a specific color space.
        alpha: Whether to include the alpha component. Defaults to True.

    Returns:
        Executable typst code.

    Examples:
        >>> color.components(rgb(255, 255, 255))
        '#rgb(255, 255, 255).components()'
    """
    return instance(_color_components, self, alpha=alpha)


@implement(
    'space', 'https://typst.app/docs/reference/visualize/color/#definitions-space'
)
def _color_space(self: Color, /):
    """Interface of `color.space` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-space) for more information.

    Args:
        self: A color in a specific color space.

    Returns:
        Executable typst code.

    Examples:
        >>> color.space(rgb(255, 255, 255))
        '#rgb(255, 255, 255).space()'
    """
    return instance(_color_space, self)


@implement(
    'to-hex', 'https://typst.app/docs/reference/visualize/color/#definitions-to-hex'
)
def _color_to_hex(self: Color, /):
    """Interface of `color.to-hex` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-to-hex) for more information.

    Args:
        self: A color in a specific color space.

    Returns:
        Executable typst code.

    Examples:
        >>> color.to_hex(rgb(255, 255, 255))
        '#rgb(255, 255, 255).to-hex()'
    """
    return instance(_color_to_hex, self)


@implement(
    'lighten', 'https://typst.app/docs/reference/visualize/color/#definitions-lighten'
)
def _color_lighten(self: Color, factor: Ratio, /):
    """Interface of `color.lighten` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-lighten) for more information.

    Args:
        self: A color in a specific color space.
        factor: The factor to lighten the color by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.lighten(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).lighten(50%)'
    """
    return instance(_color_lighten, self, factor)


@implement(
    'darken', 'https://typst.app/docs/reference/visualize/color/#definitions-darken'
)
def _color_darken(self: Color, factor: Ratio, /):
    """Interface of `color.darken` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-darken) for more information.

    Args:
        self: A color in a specific color space.
        factor: The factor to darken the color by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.darken(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).darken(50%)'
    """
    return instance(_color_darken, self, factor)


@implement(
    'saturate', 'https://typst.app/docs/reference/visualize/color/#definitions-saturate'
)
def _color_saturate(self: Color, factor: Ratio, /):
    """Interface of `color.saturate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-saturate) for more information.

    Args:
        self: A color in a specific color space.
        factor: The factor to saturate the color by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.saturate(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).saturate(50%)'
    """
    return instance(_color_saturate, self, factor)


@implement(
    'desaturate',
    'https://typst.app/docs/reference/visualize/color/#definitions-desaturate',
)
def _color_desaturate(self: Color, factor: Ratio, /):
    """Interface of `color.desaturate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-desaturate) for more information.

    Args:
        self: A color in a specific color space.
        factor: The factor to desaturate the color by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.desaturate(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).desaturate(50%)'
    """
    return instance(_color_desaturate, self, factor)


@implement(
    'negate', 'https://typst.app/docs/reference/visualize/color/#definitions-negate'
)
def _color_negate(self: Color, /, *, space: Any = 'oklab'):
    """Interface of `color.negate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-negate) for more information.

    Args:
        self: A color in a specific color space.
        space: The color space used for the transformation. Defaults to 'oklab'.

    Returns:
        Executable typst code.

    Examples:
        >>> color.negate(rgb(255, 255, 255))
        '#rgb(255, 255, 255).negate()'
        >>> color.negate(rgb(255, 255, 255), space='oklch')
        '#rgb(255, 255, 255).negate(space: oklch)'
    """
    return instance(_color_negate, self, space=space)


@implement(
    'rotate', 'https://typst.app/docs/reference/visualize/color/#definitions-rotate'
)
def _color_rotate(self: Color, angle: Angle, /, *, space: Any = 'oklch'):
    """Interface of `color.rotate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rotate) for more information.

    Args:
        self: A color in a specific color space.
        angle: The angle to rotate the hue by.
        space: The color space used to rotate. Defaults to 'oklch'.

    Returns:
        Executable typst code.

    Examples:
        >>> color.rotate(rgb(255, 255, 255), '90deg')
        '#rgb(255, 255, 255).rotate(90deg)'
    """
    return instance(_color_rotate, self, angle, space=space)


@implement(
    'color.mix', 'https://typst.app/docs/reference/visualize/color/#definitions-mix'
)
def _color_mix(*colors: Color | tuple[Color, Ratio], space: Any = 'oklab'):
    """Interface of `color.mix` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-mix) for more information.

    Args:
        space: The color space to mix in. Defaults to 'oklab'.

    Returns:
        Executable typst code.

    Examples:
        >>> color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space='oklch')
        '#color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space: oklch)'
    """
    return pre_series(_color_mix, *colors, space=space)


@implement(
    'transparentize',
    'https://typst.app/docs/reference/visualize/color/#definitions-transparentize',
)
def _color_transparentize(self: Color, scale: Ratio, /):
    """Interface of `color.transparentize` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-transparentize) for more information.

    Args:
        self: A color in a specific color space.
        scale: The factor to change the alpha value by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.transparentize(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).transparentize(50%)'
    """
    return instance(_color_transparentize, self, scale)


@implement(
    'opacify', 'https://typst.app/docs/reference/visualize/color/#definitions-opacify'
)
def _color_opacify(self: Content, scale: Ratio, /):
    """Interface of `color.opacity` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-opacify) for more information.

    Args:
        self: A color in a specific color space.
        scale: The scale to change the alpha value by.

    Returns:
        Executable typst code.

    Examples:
        >>> color.opacify(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).opacify(50%)'
    """
    return instance(_color_opacify, self, scale)


@attach_func(_color_map, 'map')
@attach_func(luma)
@attach_func(oklab)
@attach_func(oklch)
@attach_func(_color_linear_rgb, 'linear_rgb')
@attach_func(rgb)
@attach_func(cmyk)
@attach_func(_color_hsl, 'hsl')
@attach_func(_color_hsv, 'hsv')
@attach_func(_color_components, 'components')
@attach_func(_color_space, 'space')
@attach_func(_color_to_hex, 'to_hex')
@attach_func(_color_lighten, 'lighten')
@attach_func(_color_darken, 'darken')
@attach_func(_color_saturate, 'saturate')
@attach_func(_color_desaturate, 'desaturate')
@attach_func(_color_negate, 'negate')
@attach_func(_color_rotate, 'rotate')
@attach_func(_color_mix, 'mix')
@attach_func(_color_transparentize, 'transparentize')
@attach_func(_color_opacify, 'opacify')
@implement(
    'color',
    'https://typst.app/docs/reference/visualize/color/',
)
def color():
    """Interface of `color` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/) for more information.

    Returns:
        Executable typst code.

    Examples:
        >>> color()
        '#color'
    """
    return '#color'


@implement(
    'curve.move', 'https://typst.app/docs/reference/visualize/curve/#definitions-move'
)
def _curve_move(start: tuple[Length, Length], /, *, relative: bool = False):
    """Interface of `curve.move` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/#definitions-move) for more information.

    Args:
        start: The starting point for the new component.
        relative: Whether the coordinates are relative to the previous point. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> curve.move(('10pt', '10pt'))
        '#curve.move((10pt, 10pt))'
        >>> curve.move(('10pt', '10pt'), relative=True)
        '#curve.move((10pt, 10pt), relative: true)'
    """
    return normal(_curve_move, start, relative=relative)


@implement(
    'curve.line', 'https://typst.app/docs/reference/visualize/curve/#definitions-line'
)
def _curve_line(end: tuple[Length, Length], /, *, relative: bool = False):
    """Interface of `curve.line` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/#definitions-line) for more information.

    Args:
        end: The point at which the line shall end.
        relative: Whether the coordinates are relative to the previous point. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> curve.line(('10pt', '10pt'))
        '#curve.line((10pt, 10pt))'
        >>> curve.line(('10pt', '10pt'), relative=True)
        '#curve.line((10pt, 10pt), relative: true)'
    """
    return normal(_curve_line, end, relative=relative)


@implement(
    'curve.quad', 'https://typst.app/docs/reference/visualize/curve/#definitions-quad'
)
def _curve_quad(
    control: None | Auto | tuple[Length, Length],
    end: tuple[Length, Length],
    /,
    *,
    relative: bool = False,
):
    """Interface of `curve.quad` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/#definitions-quad) for more information.

    Args:
        control: The control point of the quadratic Bézier curve.
        end: The point at which the segment shall end.
        relative: Whether the control and end coordinates are relative to the previous point. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'))
        '#curve.quad((10pt, 10pt), (20pt, 20pt))'
        >>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'), relative=True)
        '#curve.quad((10pt, 10pt), (20pt, 20pt), relative: true)'
    """
    return pre_series(_curve_quad, control, end, relative=relative)


@implement(
    'curve.cubic', 'https://typst.app/docs/reference/visualize/curve/#definitions-cubic'
)
def _curve_cubic(
    control_start: None | Auto | tuple[Length, Length],
    control_end: None | tuple[Length, Length],
    end: tuple[Length, Length],
    /,
    *,
    relative: bool = False,
):
    """Interface of `curve.cubic` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/#definitions-cubic) for more information.

    Args:
        control_start: The control point going out from the start of the curve segment.
        control_end: The control point going into the end point of the curve segment.
        end: The point at which the curve segment shall end.
        relative: Whether the control-start, control-end, and end coordinates are relative to the previous point. Defaults to False.

    Returns:
        Executable typst code.

    Examples:
        >>> curve.cubic(('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'))
        '#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt))'
        >>> curve.cubic(('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'), relative=True)
        '#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt), relative: true)'
    """
    return pre_series(_curve_cubic, control_start, control_end, end, relative=relative)


@implement(
    'curve.close', 'https://typst.app/docs/reference/visualize/curve/#definitions-close'
)
def _curve_close(*, mode: str = '"smooth"'):
    """Interface of `curve.close` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/#definitions-close) for more information.

    Args:
        mode: How to close the curve.

    Raises:
        AssertionError: If `mode` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> curve.close(mode='"smooth"')
        '#curve.close()'
        >>> curve.close(mode='"straight"')
        '#curve.close(mode: "straight")'
    """
    assert mode in {'"smooth"', '"straight"'}

    return normal(_curve_close, '', mode=mode)


@attach_func(_curve_move, 'move')
@attach_func(_curve_line, 'line')
@attach_func(_curve_quad, 'quad')
@attach_func(_curve_cubic, 'cubic')
@attach_func(_curve_close, 'close')
@implement('curve', 'https://typst.app/docs/reference/visualize/curve/')
def curve(
    *components: Content,
    fill: None | Color | Gradient | Tiling = None,
    fill_rule: str = '"non-zero"',
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | dict[str, Any] = 'auto',
):
    """Interface of `curve` in typst. See [the documentation](https://typst.app/docs/reference/visualize/curve/) for more information.

    Args:
        fill: How to fill the curve. Defaults to None.
        fill_rule: The drawing rule used to fill the curve. Defaults to '"non-zero"'.
        stroke: How to stroke the curve. Defaults to 'auto'.

    Raises:
        AssertionError: If `fill_rule` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> curve(
        ...     curve.move(('0pt', '50pt')),
        ...     curve.line(('100pt', '50pt')),
        ...     curve.cubic(None, ('90pt', '0pt'), ('50pt', '0pt')),
        ...     curve.close(),
        ...     stroke='blue',
        ... )
        '#curve(stroke: blue, curve.move((0pt, 50pt)), curve.line((100pt, 50pt)), curve.cubic(none, (90pt, 0pt), (50pt, 0pt)), curve.close())'
    """
    assert fill_rule in {'"non-zero"', '"even-odd"'}

    return post_series(
        curve, *components, fill=fill, fill_rule=fill_rule, stroke=stroke
    )


@implement('ellipse', 'https://typst.app/docs/reference/visualize/ellipse/')
def ellipse(
    body: None | Content = '',
    /,
    *,
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    fill: None | Color | Gradient | Tiling = None,
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = None,
    inset: Relative | BoxInset = '0% + 5pt',
    outset: Relative | BoxOutset = {},
):
    """Interface of `ellipse` in typst. See [the documentation](https://typst.app/docs/reference/visualize/ellipse/) for more information.

    Args:
        body: The content to place into the ellipse. Defaults to ''.
        width: The ellipse's width, relative to its parent container. Defaults to 'auto'.
        height: The ellipse's height, relative to its parent container. Defaults to 'auto'.
        fill: How to fill the ellipse. Defaults to None.
        stroke: How to stroke the ellipse. Defaults to None.
        inset: How much to pad the ellipse's content. Defaults to '0% + 5pt'.
        outset: How much to expand the ellipse's size without affecting the layout. Defaults to {}.

    Returns:
        Executable typst code.

    Examples:
        >>> ellipse('[Hello, World!]')
        '#ellipse([Hello, World!])'
        >>> ellipse('[Hello, World!]', width='100%')
        '#ellipse([Hello, World!], width: 100%)'
    """
    return normal(
        ellipse,
        body,
        width=width,
        height=height,
        fill=fill,
        stroke=stroke,
        inset=inset,
        outset=outset,
    )


@implement(
    'gradient.linear',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-linear',
)
def _gradient_linear(
    *stops: Color | tuple[Color, Ratio],
    space: Any = 'oklab',
    relative: Auto | Literal['"self"', '"parent"'] = 'auto',  # noqa
) -> Gradient:  # TODO: Implement argument `dir` and `angle`.
    """Interface of `gradient.linear` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-linear) for more information.

    Args:
        space: The color space in which to interpolate the gradient. Defaults to 'oklab'.
        relative: The relative placement of the gradient. Defaults to 'auto'.

    Raises:
        AssertionError: If the number of `stops` is less than 2 or relative is invalid.

    Returns:
        A color gradient.

    Examples:
        >>> gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))
        '#gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))'
    """
    assert relative == 'auto' or relative in {'"self"', '"parent"'}

    return pre_series(_gradient_linear, *stops, space=space, relative=relative)


@implement(
    'gradient.radial',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-radial',
)
def _gradient_radial(
    *stops: Color | tuple[Color, Ratio],
    space: Any = 'oklab',
    relative: Auto | Literal['"self"', '"parent"'] = 'auto',  # noqa
    center: tuple[Ratio, Ratio] = ('50%', '50%'),
    radius: Ratio = '50%',
    focal_center: Auto | tuple[Ratio, Ratio] = 'auto',
    focal_radius: Ratio = '0%',
) -> Gradient:
    """Interface of `gradient.radial` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-radial) for more information.

    Args:
        space: The color space in which to interpolate the gradient. Defaults to 'oklab'.
        relative: The relative placement of the gradient. Defaults to 'auto'.
        center: The center of the end circle of the gradient. Defaults to ('50%', '50%').
        radius: The radius of the end circle of the gradient. Defaults to '50%'.
        focal_center: The center of the focal circle of the gradient. Defaults to 'auto'.
        focal_radius: The radius of the focal circle of the gradient. Defaults to '0%'.

    Raises:
        AssertionError: If `relative` is invalid.

    Returns:
        A color gradient.

    Examples:
        >>> gradient.radial(
        ...     color.map('viridis'), focal_center=('10%', '40%'), focal_radius='5%'
        ... )
        '#gradient.radial(..color.map.viridis, focal-center: (10%, 40%), focal-radius: 5%)'
    """
    assert relative == 'auto' or relative in {'"self"', '"parent"'}

    return pre_series(
        _gradient_radial,
        *stops,
        space=space,
        relative=relative,
        center=center,
        radius=radius,
        focal_center=focal_center,
        focal_radius=focal_radius,
    )


@implement(
    'gradient.conic',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-conic',
)
def _gradient_conic(
    *stops: Color | tuple[Color, Ratio],
    angle: Angle = '0deg',
    space: Any = 'oklab',
    relative: Auto | Literal['"self"', '"parent"'] = 'auto',  # noqa
    center: tuple[Ratio, Ratio] = ('50%', '50%'),
) -> Gradient:
    """Interface of `gradient.conic` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-conic) for more information.

    Args:
        angle: The angle of the gradient. Defaults to '0deg'.
        space: The color space in which to interpolate the gradient. Defaults to 'oklab'.
        relative: The relative placement of the gradient. Defaults to 'auto'.
        center: The center of the last circle of the gradient. Defaults to ('50%', '50%').

    Raises:
        AssertionError: If `relative` is invalid.

    Returns:
        A color gradient.

    Examples:
        >>> gradient.conic(color.map('viridis'), angle='90deg', center=('10%', '40%'))
        '#gradient.conic(..color.map.viridis, angle: 90deg, center: (10%, 40%))'
    """
    assert relative == 'auto' or relative in {'"self"', '"parent"'}

    return pre_series(
        _gradient_conic,
        *stops,
        angle=angle,
        space=space,
        relative=relative,
        center=center,
    )


@implement(
    'sharp', 'https://typst.app/docs/reference/visualize/gradient/#definitions-sharp'
)
def _gradient_sharp(
    self: Gradient, steps: int, /, *, smoothness: Ratio = '0%'
) -> Gradient:
    """Interface of `gradient.sharp` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-sharp) for more information.

    Args:
        self: A color gradient.
        steps: The number of stops in the gradient.
        smoothness: How much to smooth the gradient. Defaults to '0%'.

    Returns:
        A color gradient.

    Examples:
        >>> gradient.sharp(gradient.linear(color.map('rainbow')), 5, smoothness='50%')
        '#gradient.linear(..color.map.rainbow).sharp(5, smoothness: 50%)'
    """
    return instance(_gradient_sharp, self, steps, smoothness=smoothness)


@implement(
    'repeat', 'https://typst.app/docs/reference/visualize/gradient/#definitions-repeat'
)
def _gradient_repeat(
    self: Gradient, repetitions: int, /, *, mirror: bool = False
) -> Gradient:
    """Interface of `gradient.repeat` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-repeat) for more information.

    Args:
        self: A color gradient.
        repetitions: The number of times to repeat the gradient.
        mirror: Whether to mirror the gradient at each repetition. Defaults to False.

    Returns:
        A color gradient.
    """
    return instance(_gradient_repeat, self, repetitions, mirror=mirror)


@implement(
    'kind', 'https://typst.app/docs/reference/visualize/gradient/#definitions-kind'
)
def _gradient_kind(self: Gradient, /):
    """Interface of `gradient.kind` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-kind) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_kind, self)


@implement(
    'stops', 'https://typst.app/docs/reference/visualize/gradient/#definitions-stops'
)
def _gradient_stops(self: Gradient, /):
    """Interface of `gradient.stops` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-stops) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_stops, self)


@implement(
    'space', 'https://typst.app/docs/reference/visualize/gradient/#definitions-space'
)
def _gradient_space(self: Gradient, /):
    """Interface of `gradient.space` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-space) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_space, self)


@implement(
    'relative',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-relative',
)
def _gradient_relative(self: Gradient, /):
    """Interface of `gradient.relative` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-relative) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_relative, self)


@implement(
    'angle', 'https://typst.app/docs/reference/visualize/gradient/#definitions-angle'
)
def _gradient_angle(self: Gradient, /):
    """Interface of `gradient.angle` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-angle) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_angle, self)


@implement(
    'center', 'https://typst.app/docs/reference/visualize/gradient/#definitions-center'
)
def _gradient_center(self: Gradient, /):
    """Interface of `gradient.center` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-center) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_center, self)


@implement(
    'radius', 'https://typst.app/docs/reference/visualize/gradient/#definitions-radius'
)
def _gradient_radius(self: Gradient, /):
    """Interface of `gradient.radius` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-radius) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_radius, self)


@implement(
    'focal-center',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center',
)
def _gradient_focal_center(self: Gradient, /):
    """Interface of `gradient.focal-center` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_focal_center, self)


@implement(
    'focal-radius',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius',
)
def _gradient_focal_radius(self: Gradient, /):
    """Interface of `gradient.focal-radius` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_focal_radius, self)


@implement(
    'sample', 'https://typst.app/docs/reference/visualize/gradient/#definitions-sample'
)
def _gradient_sample(self: Gradient, t: Angle | Ratio, /) -> Color:
    """Interface of `gradient.sample` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-sample) for more information.

    Args:
        self: A color gradient.
        t: The position at which to sample the gradient.

    Returns:
        A color in a specific color space.
    """
    return instance(_gradient_sample, self, t)


@implement(
    'samples',
    'https://typst.app/docs/reference/visualize/gradient/#definitions-samples',
)
def _gradient_samples(self: Gradient, /, *ts: Angle | Ratio):
    """Interface of `gradient.samples` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-samples) for more information.

    Args:
        self: A color gradient.

    Returns:
        Executable typst code.
    """
    return instance(_gradient_samples, self, *ts)


@attach_func(_gradient_linear, 'linear')
@attach_func(_gradient_radial, 'radial')
@attach_func(_gradient_conic, 'conic')
@attach_func(_gradient_sharp, 'sharp')
@attach_func(_gradient_repeat, 'repeat')
@attach_func(_gradient_kind, 'kind')
@attach_func(_gradient_stops, 'stops')
@attach_func(_gradient_space, 'space')
@attach_func(_gradient_relative, 'relative')
@attach_func(_gradient_angle, 'angle')
@attach_func(_gradient_center, 'center')
@attach_func(_gradient_radius, 'radius')
@attach_func(_gradient_focal_center, 'focal_center')
@attach_func(_gradient_focal_radius, 'focal_radius')
@attach_func(_gradient_sample, 'sample')
@attach_func(_gradient_samples, 'samples')
@implement('gradient', 'https://typst.app/docs/reference/visualize/gradient/')
def gradient():
    """Interface of `gradient` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/) for more information.

    Returns:
        Executable typst code.

    Examples:
        >>> gradient()
        '#gradient'
    """
    return '#gradient'


@deprecated(
    version='1.1.1',
    reason='The `image.decode` is deprecated, directly pass bytes to `image` instead.',
)
@implement(
    'image.decode',
    'https://typst.app/docs/reference/visualize/image/#definitions-decode',
)
def _image_decode(
    data: str,
    /,
    *,
    format: Auto | Literal['"png"', '"jpg"', '"gif"', '"svg"'] = 'auto',  # noqa
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    alt: None | str = None,
    fit: Literal['"cover"', '"contain"', '"stretch"'] = '"cover"',  # noqa
):
    """Interface of `image.decode` in typst. See [the documentation](https://typst.app/docs/reference/visualize/image/#definitions-decode) for more information.

    Args:
        data: The data to decode as an image. Can be a string for SVGs.
        format: The image's format. Defaults to 'auto'.
        width: The width of the image. Defaults to 'auto'.
        height: The height of the image. Defaults to 'auto'.
        alt: A text describing the image. Defaults to None.
        fit: How the image should adjust itself to a given area. Defaults to '"cover"'.

    Raises:
        AssertionError: If `format` or `fit` is invalid.

    Returns:
        Executable typst code.
    """
    assert format == 'auto' or format in {'"png"', '"jpg"', '"gif"', '"svg"'}
    assert fit in {'"cover"', '"contain"', '"stretch"'}

    return normal(
        _image_decode, data, format=format, width=width, height=height, alt=alt, fit=fit
    )


@attach_func(_image_decode, 'decode')
@implement('image', 'https://typst.app/docs/reference/visualize/image/')
def image(
    source: str,  # TODO: Consider support `bytes` in the future.
    /,
    *,
    format: Auto
    | Literal['"png"', '"jpg"', '"gif"', '"svg"']  # noqa
    | dict[str, Any] = 'auto',
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    alt: None | str = None,
    fit: Literal['"cover"', '"contain"', '"stretch"'] = '"cover"',  # noqa
    scaling: Auto | Literal['"smooth"', '"pixelated"'] = 'auto',  # noqa
    icc: Auto | str = 'auto',  # TODO: Consider support `bytes` in the future.
):
    """Interface of `image` in typst. See [the documentation](https://typst.app/docs/reference/visualize/image/) for more information.

    Args:
        source: A path to an image file or raw bytes making up an image in one of the supported formats.
        format: The image's format. Defaults to 'auto'.
        width: The width of the image. Defaults to 'auto'.
        height: The height of the image. Defaults to 'auto'.
        alt: A text describing the image. Defaults to None.
        fit: How the image should adjust itself to a given area (the area is defined by the width and height fields). Defaults to '"cover"'.
        scaling: A hint to viewers how they should scale the image. Defaults to 'auto'.
        icc: An ICC profile for the image. Defaults to 'auto'.

    Raises:
        AssertionError: If `format` or `fit` or `scaling` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> image('"image.png"')
        '#image("image.png")'
        >>> image('"image.png"', fit='"contain"')
        '#image("image.png", fit: "contain")'
    """
    assert format == 'auto' or format in {'"png"', '"jpg"', '"gif"', '"svg"'}
    assert fit in {'"cover"', '"contain"', '"stretch"'}
    assert scaling == 'auto' or scaling in {'"smooth"', '"pixelated"'}

    return normal(
        image,
        source,
        format=format,
        width=width,
        height=height,
        alt=alt,
        fit=fit,
        scaling=scaling,
        icc=icc,
    )


@implement('line', 'https://typst.app/docs/reference/visualize/line/')
def line(
    *,
    start: tuple[Relative, Relative] = ('0% + 0pt', '0% + 0pt'),
    end: None | tuple[Relative, Relative] = None,
    length: Relative = '0% + 30pt',
    angle: Angle = '0deg',
    stroke: Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = '1pt + black',
):
    """Interface of `line` in typst. See [the documentation](https://typst.app/docs/reference/visualize/line/) for more information.

    Args:
        start: The start point of the line. Defaults to ('0% + 0pt', '0% + 0pt').
        end: The offset from start where the line ends. Defaults to None.
        length: The line's length. Defaults to '0% + 30pt'.
        angle: The angle at which the line points away from the origin. Defaults to '0deg'.
        stroke: How to stroke the line. Defaults to '1pt + black'.

    Returns:
        Executable typst code.

    Examples:
        >>> line()
        '#line()'
        >>> line(end=('100% + 0pt', '100% + 0pt'))
        '#line(end: (100% + 0pt, 100% + 0pt))'
        >>> line(angle='90deg')
        '#line(angle: 90deg)'
        >>> line(stroke='1pt + red')
        '#line(stroke: 1pt + red)'
    """
    return normal(line, start=start, end=end, length=length, angle=angle, stroke=stroke)


@deprecated(
    version='1.1.1', reason='The `path` function is deprecated, use `curve` instead.'
)
@implement('path', 'https://typst.app/docs/reference/visualize/path/')
def path(
    *vertices: tuple[Ratio, Ratio] | Sequence[tuple[Ratio, Ratio]],
    fill: None | Color | Gradient | Tiling = None,
    fill_rule: Literal['"non-zero"', '"evenodd"'] = '"non-zero"',  # noqa
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = 'auto',
    closed: bool = False,
):
    """Interface of `path` in typst. See [the documentation](https://typst.app/docs/reference/visualize/path/) for more information.

    Args:
        fill: How to fill the path. Defaults to None.
        fill_rule: The drawing rule used to fill the path. Defaults to '"non-zero"'.
        stroke: How to stroke the path. Defaults to 'auto'.
        closed: Whether to close this path with one last bezier curve. Defaults to False.

    Raises:
        AssertionError: If `fill_rule` is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> path(('0%', '0%'), ('100%', '0%'), ('100%', '100%'), ('0%', '100%'))
        '#path((0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
        >>> path(('0%', '0%'), ('100%', '0%'), ('100%', '100%'), ('0%', '100%'), fill='red')
        '#path(fill: red, (0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
        >>> path(
        ...     ('0%', '0%'),
        ...     ('100%', '0%'),
        ...     ('100%', '100%'),
        ...     ('0%', '100%'),
        ...     fill='red',
        ...     stroke='blue',
        ... )
        '#path(fill: red, stroke: blue, (0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
    """
    assert fill_rule in {'"non-zero"', '"evenodd"'}

    return post_series(
        path, *vertices, fill=fill, fill_rule=fill_rule, stroke=stroke, closed=closed
    )


@implement('pattern', 'https://typst.app/docs/reference/visualize/pattern/')
def pattern(
    body: Content,
    /,
    *,
    size: Auto | tuple[Length, Length] = 'auto',
    spacing: tuple[Length, Length] = ('0pt', '0pt'),
    relative: Auto | Literal['"self"', '"parent"'] = 'auto',  # noqa
) -> Tiling:
    """Interface of `pattern` in typst. See [the documentation](https://typst.app/docs/reference/visualize/pattern/) for more information.

    Args:
        body: The content of each cell of the pattern.
        size: The bounding box of each cell of the pattern. Defaults to 'auto'.
        spacing: The spacing between cells of the pattern. Defaults to ('0pt', '0pt').
        relative: The relative placement of the pattern. Defaults to 'auto'.

    Raises:
        AssertionError: If `relative` is invalid.

    Returns:
        A repeating pattern fill.
    """
    assert relative == 'auto' or relative in {'"self"', '"parent"'}

    return normal(pattern, body, size=size, spacing=spacing, relative=relative)


@implement(
    'polygon.regular',
    'https://typst.app/docs/reference/visualize/polygon/#definitions-regular',
)
def _polygon_regular(
    *,
    fill: None | Color | Gradient | Tiling = None,
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = None,
    size: Length = '1em',
    vertices: int = 3,
):
    """Interface of `polygon.regular` in typst. See [the documentation](https://typst.app/docs/reference/visualize/polygon/#definitions-regular) for more information.

    Args:
        fill: How to fill the polygon. Defaults to None.
        stroke: How to stroke the polygon. Defaults to None.
        size: The diameter of the circumcircle of the regular polygon. Defaults to '1em'.
        vertices: The number of vertices in the polygon. Defaults to 3.

    Returns:
        Executable typst code.
    """
    return normal(
        _polygon_regular, fill=fill, stroke=stroke, size=size, vertices=vertices
    )


@attach_func(_polygon_regular, 'regular')
@implement('polygon', 'https://typst.app/docs/reference/visualize/polygon/')
def polygon(
    *vertices: tuple[Relative, Relative] | Sequence[tuple[Relative, Relative]],
    fill: None | Color | Gradient | Tiling = None,
    fill_rule: Literal['"non-zero"', '"evenodd"'] = '"non-zero"',  # noqa
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = 'auto',
):
    """Interface of `polygon` in typst. See [the documentation](https://typst.app/docs/reference/visualize/polygon/) for more information.

    Args:
        fill: How to fill the polygon. Defaults to None.
        fill_rule: The drawing rule used to fill the polygon. Defaults to '"non-zero"'.
        stroke: How to stroke the polygon. Defaults to 'auto'.

    Raises:
        AssertionError: If `fill_rule` is invalid.

    Returns:
        Executable typst code.
    """
    assert fill_rule in {'"non-zero"', '"evenodd"'}

    return post_series(
        polygon, *vertices, fill=fill, fill_rule=fill_rule, stroke=stroke
    )


@implement('rect', 'https://typst.app/docs/reference/visualize/rect/')
def rect(
    body: None | Content = '',
    /,
    *,
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    fill: None | Color | Gradient | Tiling = None,
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = 'auto',
    radius: Relative | RectangleRadius = {},
    inset: Relative | BoxInset = '0% + 5pt',
    outset: Relative | BoxOutset = {},
):
    """Interface of `rect` in typst. See [the documentation](https://typst.app/docs/reference/visualize/rect/) for more information.

    Args:
        body: The content to place into the rectangle. Defaults to ''.
        width: The rectangle's width, relative to its parent container. Defaults to 'auto'.
        height: The rectangle's height, relative to its parent container. Defaults to 'auto'.
        fill: How to fill the rectangle. Defaults to None.
        stroke: How to stroke the rectangle. Defaults to 'auto'.
        radius: How much to round the rectangle's corners, relative to the minimum of the width and height divided by two. Defaults to {}.
        inset: How much to pad the rectangle's content. Defaults to '0% + 5pt'.
        outset: How much to expand the rectangle's size without affecting the layout. Defaults to {}.

    Returns:
        Executable typst code.
    """
    return normal(
        rect,
        body,
        width=width,
        height=height,
        fill=fill,
        stroke=stroke,
        radius=radius,
        inset=inset,
        outset=outset,
    )


@implement('square', 'https://typst.app/docs/reference/visualize/square/')
def square(
    body: Content = '',
    /,
    *,
    size: Auto | Length = 'auto',
    width: Auto | Relative = 'auto',
    height: Auto | Relative | Fraction = 'auto',
    fill: None | Color | Gradient | Tiling = None,
    stroke: None
    | Auto
    | Length
    | Color
    | Gradient
    | Stroke
    | Tiling
    | RectangleStroke = 'auto',
    radius: Relative | RectangleRadius = {},
    inset: Relative | BoxInset = '0% + 5pt',
    outset: Relative | BoxOutset = {},
):
    """Interface of `square` in typst. See [the documentation](https://typst.app/docs/reference/visualize/square/) for more information.

    Args:
        body: The content to place into the square. Defaults to ''.
        size: The square's side length. Defaults to 'auto'.
        width: The square's width. Defaults to 'auto'.
        height: The square's height. Defaults to 'auto'.
        fill: How to fill the square. Defaults to None.
        stroke: How to stroke the square. Defaults to 'auto'.
        radius: How much to round the square's corners. Defaults to {}.
        inset: How much to pad the square's content. Defaults to '0% + 5pt'.
        outset: How much to expand the square's size without affecting the layout. Defaults to {}.

    Raises:
        AssertionError: If `size` is not 'auto' when either `width` or `height` is not 'auto'.

    Returns:
        Executable typst code.
    """
    assert (width == 'auto' and height == 'auto') if size != 'auto' else True

    return normal(
        square,
        body,
        size=size,
        width=width,
        height=height,
        fill=fill,
        stroke=stroke,
        radius=radius,
        inset=inset,
        outset=outset,
    )


# TODO: Implement `stroke` when necessary.

__all__ = [
    'circle',
    'luma',
    'oklab',
    'oklch',
    'rgb',
    'cmyk',
    'color',
    'curve',
    'ellipse',
    'gradient',
    'image',
    'line',
    'path',
    'pattern',
    'polygon',
    'rect',
    'square',
]
