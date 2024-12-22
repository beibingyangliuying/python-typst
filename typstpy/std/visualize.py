from typing import Any, Iterable, Optional, overload

from cytoolz.curried import (  # type:ignore
    identity,
    map,
)
from pymonad.maybe import Maybe  # type:ignore

from .._utils import (
    attach_func,
    implement,
    instance,
    is_valid,
    normal,
    pad,
    positional,
    post_series,
    pre_series,
)
from ..typings import Block


@implement(
    True,
    original_name='circle',
    hyperlink='https://typst.app/docs/reference/visualize/circle/',
)
def circle(
    body: str | None = '',
    *,
    radius: str = '0pt',
    width: str = 'auto',
    height: str = 'auto',
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = 'auto',
    inset: str | dict[str, Any] = '0% + 5pt',
    outset: str | dict[str, Any] = dict(),
) -> Block:
    """Interface of `circle` in typst. See [the documentation](https://typst.app/docs/reference/visualize/circle/) for more information.

    Args:
        body (str | None, optional): The content to place into the circle. Defaults to ''.
        radius (str, optional): The circle's radius. Defaults to '0pt'.
        width (str, optional): The circle's width. Defaults to 'auto'.
        height (str, optional): The circle's height. Defaults to 'auto'.
        fill (str | None, optional): How to fill the circle. Defaults to None.
        stroke (str | dict[str, Any] | None, optional): How to stroke the circle. Defaults to 'auto'.
        inset (str | dict[str, Any], optional): How much to pad the circle's content. Defaults to '0% + 5pt'.
        outset (str | dict[str, Any], optional): How much to expand the circle's size without affecting the layout. Defaults to dict().

    Returns:
        Block: Executable typst code.

    Examples:
        >>> circle('[Hello, world!]')
        '#circle([Hello, world!])'
        >>> circle('[Hello, world!]', radius='10pt')
        '#circle([Hello, world!], radius: 10pt)'
        >>> circle('[Hello, world!]', width='100%', height='100%')
        '#circle([Hello, world!], width: 100%, height: 100%)'
    """
    is_valid(
        lambda: (width == 'auto' and height == 'auto') if radius != '0pt' else True
    )
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


@implement(False)
def _color_map(name: str, /) -> Block:
    """Interface of `color.map` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#predefined-color-maps) for more information.

    Args:
        name (str): The name of the color map.

    Raises:
        ValueError: Invalid name.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.map('turbo')
        '#color.map.turbo'
    """
    is_valid(
        lambda: name
        in (
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
        ),
    )
    return f'#color.map.{name}'


@implement(
    True,
    original_name='luma',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-luma',
)
def luma(lightness: str | int, alpha: Optional[str] = None, /) -> Block:
    """Interface of `luma` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-luma) for more information.

    Args:
        lightness (str | int): The lightness component.
        alpha (Optional[str], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> luma('50%')
        '#luma(50%)'
        >>> luma('50%', '50%')
        '#luma(50%, 50%)'
    """
    args = (
        Maybe([lightness], alpha)
        .map(lambda x: x + [alpha])
        .maybe([lightness], identity)
    )
    return positional(luma, *args)


@implement(
    True,
    original_name='oklab',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-oklab',
)
def oklab(
    lightness: str, a: str | float, b: str | float, alpha: Optional[str] = None, /
) -> Block:
    """Interface of `oklab` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-oklab) for more information.

    Args:
        lightness (str): The lightness component.
        a (str | float): The a ("green/red") component.
        b (str | float): The b ("blue/yellow") component.
        alpha (Optional[str], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> oklab('50%', '0%', '0%')
        '#oklab(50%, 0%, 0%)'
        >>> oklab('50%', '0%', '0%', '50%')
        '#oklab(50%, 0%, 0%, 50%)'
    """
    args = (
        Maybe([lightness, a, b], alpha)
        .map(lambda x: x + [alpha])
        .maybe([lightness, a, b], identity)
    )
    return positional(oklab, *args)


@implement(
    True,
    original_name='oklch',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-oklch',
)
def oklch(
    lightness: str, chroma: str | float, hue: str, alpha: Optional[str] = None, /
) -> Block:
    """Interface of `oklch` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-oklch) for more information.

    Args:
        lightness (str): The lightness component.
        chroma (str | float): The chroma component.
        hue (str): The hue component.
        alpha (Optional[str], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> oklch('50%', '0%', '0deg')
        '#oklch(50%, 0%, 0deg)'
        >>> oklch('50%', '0%', '0deg', '50%')
        '#oklch(50%, 0%, 0deg, 50%)'
    """
    args = (
        Maybe([lightness, chroma, hue], alpha)
        .map(lambda x: x + [alpha])
        .maybe([lightness, chroma, hue], identity)
    )
    return positional(oklch, *args)


@implement(
    True,
    original_name='color.linear-rgb',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb',
)
def _color_linear_rgb(
    red: str | int,
    green: str | int,
    blue: str | int,
    alpha: Optional[str | int] = None,
    /,
) -> Block:
    """Interface of `color.linear-rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) for more information.

    Args:
        red (str | int): The red component.
        green (str | int): The green component.
        blue (str | int): The blue component.
        alpha (Optional[str  |  int], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.linear_rgb(255, 255, 255)
        '#color.linear-rgb(255, 255, 255)'
        >>> color.linear_rgb('50%', '50%', '50%', '50%')
        '#color.linear-rgb(50%, 50%, 50%, 50%)'
    """
    args = (
        Maybe([red, green, blue], alpha)
        .map(lambda x: x + [alpha])
        .maybe([red, green, blue], identity)
    )
    return positional(_color_linear_rgb, *args)


@overload
def rgb(
    red: str | int,
    green: str | int,
    blue: str | int,
    alpha: Optional[str | int] = None,
    /,
) -> Block: ...


@overload
def rgb(hex: str) -> Block: ...


@implement(
    True,
    original_name='rgb',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-rgb',
)
def rgb(*args) -> Block:
    """Interface of `rgb` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rgb) for more information.

    Raises:
        ValueError: If the number of arguments is not 1, 3, or 4.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> rgb(255, 255, 255)
        '#rgb(255, 255, 255)'
        >>> rgb('50%', '50%', '50%', '50%')
        '#rgb(50%, 50%, 50%, 50%)'
        >>> rgb('"#ffffff"')
        '#rgb("#ffffff")'
    """
    is_valid(lambda: len(args) in (1, 3, 4))
    return positional(rgb, *args)  # type: ignore


@implement(
    True,
    original_name='cmyk',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-cmyk',
)
def cmyk(cyan: str, magenta: str, yellow: str, key: str, /) -> Block:
    """Interface of `cmyk` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) for more information.

    Args:
        cyan (str): The cyan component.
        magenta (str): The magenta component.
        yellow (str): The yellow component.
        key (str): The key component.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> cmyk('0%', '0%', '0%', '0%')
        '#cmyk(0%, 0%, 0%, 0%)'
        >>> cmyk('50%', '50%', '50%', '50%')
        '#cmyk(50%, 50%, 50%, 50%)'
    """
    return positional(cmyk, cyan, magenta, yellow, key)


@implement(
    True,
    original_name='color.hsl',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-hsl',
)
def _color_hsl(
    hue: str,
    saturation: str | int,
    lightness: str | int,
    alpha: Optional[str | int] = None,
    /,
) -> Block:
    """Interface of `color.hsl` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-hsl) for more information.

    Args:
        hue (str): The hue angle.
        saturation (str | int): The saturation component.
        lightness (str | int): The lightness component.
        alpha (Optional[str  |  int], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.hsl('0deg', '50%', '50%', '50%')
        '#color.hsl(0deg, 50%, 50%, 50%)'
        >>> color.hsl('0deg', '50%', '50%')
        '#color.hsl(0deg, 50%, 50%)'
    """
    args = (
        Maybe([hue, saturation, lightness], alpha)
        .map(lambda x: x + [alpha])
        .maybe([hue, saturation, lightness], identity)
    )
    return positional(_color_hsl, *args)


@implement(
    True,
    original_name='color.hsv',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-hsv',
)
def _color_hsv(
    hue: str,
    saturation: str | int,
    value: str | int,
    alpha: Optional[str | int] = None,
    /,
) -> Block:
    """Interface of `color.hsv` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-hsv) for more information.

    Args:
        hue (str): The hue angle.
        saturation (str | int): The saturation component.
        value (str | int): The value component.
        alpha (Optional[str  |  int], optional): The alpha component. Defaults to None.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.hsv('0deg', '50%', '50%', '50%')
        '#color.hsv(0deg, 50%, 50%, 50%)'
        >>> color.hsv('0deg', '50%', '50%')
        '#color.hsv(0deg, 50%, 50%)'
    """
    args = (
        Maybe([hue, saturation, value], alpha)
        .map(lambda x: x + [alpha])
        .maybe([hue, saturation, value], identity)
    )
    return positional(_color_hsv, *args)


@implement(
    True,
    original_name='components',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-components',
)
def _color_components(self: Block, /, *, alpha: bool = True) -> Block:
    """Interface of `color.components` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-components) for more information.

    Args:
        self (Block): The instance.
        alpha (bool, optional): Whether to include the alpha component. Defaults to True.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.components(rgb(255, 255, 255))
        '#rgb(255, 255, 255).components()'
    """
    return instance(_color_components, self, alpha=alpha)


@implement(
    True,
    original_name='space',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-space',
)
def _color_space(self: Block, /) -> Block:
    """Interface of `color.space` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-space) for more information.

    Args:
        self (Block): The instance.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.space(rgb(255, 255, 255))
        '#rgb(255, 255, 255).space()'
    """
    return instance(_color_space, self)


@implement(
    True,
    original_name='to-hex',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-to-hex',
)
def _color_to_hex(self: Block, /) -> Block:
    """Interface of `color.to-hex` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-to-hex) for more information.

    Args:
        self (Block): The instance.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.to_hex(rgb(255, 255, 255))
        '#rgb(255, 255, 255).to-hex()'
    """
    return instance(_color_to_hex, self)


@implement(
    True,
    original_name='lighten',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-lighten',
)
def _color_lighten(self: Block, factor: str, /) -> Block:
    """Interface of `color.lighten` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-lighten) for more information.

    Args:
        self (Block): The instance.
        factor (str): The factor to lighten the color by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.lighten(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).lighten(50%)'
    """
    return instance(_color_lighten, self, factor)


@implement(
    True,
    original_name='darken',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-darken',
)
def _color_darken(self: Block, factor: str, /) -> Block:
    """Interface of `color.darken` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-darken) for more information.

    Args:
        self (Block): The instance.
        factor (str): The factor to darken the color by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.darken(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).darken(50%)'
    """
    return instance(_color_darken, self, factor)


@implement(
    True,
    original_name='saturate',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-saturate',
)
def _color_saturate(self: Block, factor: str, /) -> Block:
    """Interface of `color.saturate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-saturate) for more information.

    Args:
        self (Block): The instance.
        factor (str): The factor to saturate the color by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.saturate(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).saturate(50%)'
    """
    return instance(_color_saturate, self, factor)


@implement(
    True,
    original_name='desaturate',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-desaturate',
)
def _color_desaturate(self: Block, factor: str, /) -> Block:
    """Interface of `color.desaturate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-desaturate) for more information.

    Args:
        self (Block): The instance.
        factor (str): The factor to desaturate the color by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.desaturate(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).desaturate(50%)'
    """
    return instance(_color_desaturate, self, factor)


@implement(
    True,
    original_name='negate',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-negate',
)
def _color_negate(self: Block, /, *, space: str = 'oklab') -> Block:
    """Interface of `color.negate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-negate) for more information.

    Args:
        self (Block): The instance.
        space (str, optional): The color space used for the transformation. Defaults to 'oklab'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.negate(rgb(255, 255, 255))
        '#rgb(255, 255, 255).negate()'
        >>> color.negate(rgb(255, 255, 255), space='oklch')
        '#rgb(255, 255, 255).negate(space: oklch)'
    """
    return instance(_color_negate, self, space=space)


@implement(
    True,
    original_name='rotate',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-rotate',
)
def _color_rotate(self: Block, angle: str, /, *, space: str = 'oklch') -> Block:
    """Interface of `color.rotate` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-rotate) for more information.

    Args:
        self (Block): The instance.
        angle (str): The angle to rotate the hue by.
        space (str, optional): The color space used to rotate. Defaults to 'oklch'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.rotate(rgb(255, 255, 255), '90deg')
        '#rgb(255, 255, 255).rotate(90deg)'
    """
    return instance(_color_rotate, self, angle, space=space)


@implement(
    True,
    original_name='color.mix',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-mix',
)
def _color_mix(*colors: str, space: str = 'oklab') -> Block:
    """Interface of `color.mix` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-mix) for more information.

    Args:
        space (str, optional): The color space to mix in. Defaults to 'oklab'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space='oklch')
        '#color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space: oklch)'
    """
    return pre_series(_color_mix, *colors, space=space)


@implement(
    True,
    original_name='transparentize',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-transparentize',
)
def _color_transparentize(self: Block, scale: str, /) -> Block:
    """Interface of `color.transparentize` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-transparentize) for more information.

    Args:
        self (Block): The instance.
        scale (str): The factor to change the alpha value by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.transparentize(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).transparentize(50%)'
    """
    return instance(_color_transparentize, self, scale)


@implement(
    True,
    original_name='opacify',
    hyperlink='https://typst.app/docs/reference/visualize/color/#definitions-opacify',
)
def _color_opacify(self: Block, scale: str, /) -> Block:
    """Interface of `color.opacity` in typst. See [the documentation](https://typst.app/docs/reference/visualize/color/#definitions-opacify) for more information.

    Args:
        self (Block): The instance.
        scale (str): The scale to change the alpha value by.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> color.opacify(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).opacify(50%)'
    """
    return instance(_color_opacify, self, scale)


@attach_func(_color_map, 'map')  # type:ignore
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
    True,
    original_name='color',
    hyperlink='https://typst.app/docs/reference/visualize/color/',
)
def color() -> None:
    pass


@implement(
    True,
    original_name='ellipse',
    hyperlink='https://typst.app/docs/reference/visualize/ellipse/',
)
def ellipse(
    body: str | None = '',
    /,
    *,
    width: str = 'auto',
    height: str = 'auto',
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = None,
    inset: str | dict[str, Any] = '0% + 5pt',
    outset: str | dict[str, Any] = dict(),
) -> Block:
    """Interface of `ellipse` in typst. See [the documentation](https://typst.app/docs/reference/visualize/ellipse/) for more information.

    Args:
        body (str | None, optional): The content to place into the ellipse. Defaults to ''.
        width (str, optional): The ellipse's width, relative to its parent container. Defaults to 'auto'.
        height (str, optional): The ellipse's height, relative to its parent container. Defaults to 'auto'.
        fill (str | None, optional): How to fill the ellipse. Defaults to None.
        stroke (str | dict[str, Any] | None, optional): How to stroke the ellipse. Defaults to None.
        inset (str | dict[str, Any], optional): How much to pad the ellipse's content. Defaults to '0% + 5pt'.
        outset (str | dict[str, Any], optional): How much to expand the ellipse's size without affecting the layout. Defaults to dict().

    Returns:
        Block: Executable typst code.

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
    True,
    original_name='gradient.linear',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-linear',
)
def _gradient_linear(
    *stops: str,
    space: str = 'oklab',
    relative: str = 'auto',
) -> Block:
    """Interface of `gradient.linear` in typst. See [the documentation](https://typst.app/docs/reference/visualize/gradient/#definitions-linear) for more information.

    Args:
        space (str, optional): The color space in which to interpolate the gradient. Defaults to 'oklab'.
        relative (str, optional): The relative placement of the gradient. Defaults to 'auto'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))
        '#gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))'
    """
    return pre_series(_gradient_linear, *stops, space=space, relative=relative)


@implement(
    True,
    original_name='gradient.radial',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-radial',
)
def _gradient_radial(
    *stops: str,
    space: str = 'oklab',
    relative: str = 'auto',
    center: tuple[str, str] = ('50%', '50%'),
    radius: str = '50%',
    focal_center: str | tuple[str, str] = 'auto',
    focal_radius: str = '0%',
) -> Block:
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
    True,
    original_name='gradient.conic',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-conic',
)
def _gradient_conic(
    *stops: str,
    angle: str = '0deg',
    space: str = 'oklab',
    relative: str = 'auto',
    center: tuple[str, str] = ('50%', '50%'),
) -> Block:
    return pre_series(
        _gradient_conic,
        *stops,
        angle=angle,
        space=space,
        relative=relative,
        center=center,
    )


@implement(
    True,
    original_name='sharp',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-sharp',
)
def _gradient_sharp(self: Block, steps: int, /, *, smoothness: str = '0%') -> Block:
    return instance(_gradient_sharp, self, steps, smoothness=smoothness)


@implement(
    True,
    original_name='repeat',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-repeat',
)
def _gradient_repeat(
    self: Block, repetitions: int, /, *, mirror: bool = False
) -> Block:
    return instance(_gradient_repeat, self, repetitions, mirror=mirror)


@implement(
    True,
    original_name='kind',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-kind',
)
def _gradient_kind(self: Block, /) -> Block:
    return instance(_gradient_kind, self)


@implement(
    True,
    original_name='stops',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-stops',
)
def _gradient_stops(self: Block, /) -> Block:
    return instance(_gradient_stops, self)


@implement(
    True,
    original_name='space',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-space',
)
def _gradient_space(self: Block, /) -> Block:
    return instance(_gradient_space, self)


@implement(
    True,
    original_name='relative',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-relative',
)
def _gradient_relative(self: Block, /) -> Block:
    return instance(_gradient_relative, self)


@implement(
    True,
    original_name='angle',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-angle',
)
def _gradient_angle(self: Block, /) -> Block:
    return instance(_gradient_angle, self)


@implement(
    True,
    original_name='sample',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-sample',
)
def _gradient_sample(self: Block, t: str, /) -> Block:
    return instance(_gradient_sample, self, t)


@implement(
    True,
    original_name='samples',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/#definitions-samples',
)
def _gradient_samples(self: Block, /, *ts: str) -> Block:
    return instance(_gradient_samples, self, *ts)


@attach_func(_gradient_linear, 'linear')  # type: ignore
@attach_func(_gradient_radial, 'radial')
@attach_func(_gradient_conic, 'conic')
@attach_func(_gradient_sharp, 'sharp')
@attach_func(_gradient_repeat, 'repeat')
@attach_func(_gradient_kind, 'kind')
@attach_func(_gradient_stops, 'stops')
@attach_func(_gradient_space, 'space')
@attach_func(_gradient_relative, 'relative')
@attach_func(_gradient_angle, 'angle')
@attach_func(_gradient_sample, 'sample')
@attach_func(_gradient_samples, 'samples')
@implement(
    True,
    original_name='gradient',
    hyperlink='https://typst.app/docs/reference/visualize/gradient/',
)
def gradient() -> None:
    pass


@implement(
    True,
    original_name='image.decode',
    hyperlink='https://typst.app/docs/reference/visualize/image/#definitions-decode',
)
def _image_decode(
    data: str,
    /,
    *,
    format: str = 'auto',
    width: str = 'auto',
    height: str = 'auto',
    alt: str | None = None,
    fit: str = '"cover"',
) -> Block:
    return normal(
        _image_decode, data, format=format, width=width, height=height, alt=alt, fit=fit
    )


@attach_func(_image_decode, 'decode')
@implement(
    True,
    original_name='image',
    hyperlink='https://typst.app/docs/reference/visualize/image/',
)
def image(
    path: str,
    /,
    *,
    format: str = 'auto',
    width: str = 'auto',
    height: str = 'auto',
    alt: str | None = None,
    fit: str = '"cover"',
) -> Block:
    """Interface of `image` in typst. See [the documentation](https://typst.app/docs/reference/visualize/image/) for more information.

    Args:
        path (str): Path to an image file.
        format (str, optional): The image's format. Defaults to 'auto'.
        width (str, optional): The width of the image. Defaults to 'auto'.
        height (str, optional): The height of the image. Defaults to 'auto'.
        alt (str | None, optional): A text describing the image. Defaults to None.
        fit (str, optional): How the image should adjust itself to a given area (the area is defined by the width and height fields). Defaults to '"cover"'.

    Returns:
        Block: Executable typst code.

    Examples:
        >>> image('"image.png"')
        '#image("image.png")'
        >>> image('"image.png"', fit='"contain"')
        '#image("image.png", fit: "contain")'
    """
    is_valid(
        lambda: format == 'auto' or format in map(pad, ('png', 'jpg', 'gif', 'svg')),
        lambda: fit in map(pad, ('cover', 'contain', 'stretch')),
    )
    return normal(
        image,
        path,
        format=format,
        width=width,
        height=height,
        alt=alt,
        fit=fit,
    )


@implement(
    True,
    original_name='line',
    hyperlink='https://typst.app/docs/reference/visualize/line/',
)
def line(
    *,
    start: tuple[str, str] = ('0% + 0pt', '0% + 0pt'),
    end: tuple[str, str] | None = None,
    length: str = '0% + 30pt',
    angle: str = '0deg',
    stroke: str | dict[str, Any] = '1pt + black',
) -> Block:
    return normal(line, start=start, end=end, length=length, angle=angle, stroke=stroke)


@implement(
    True,
    original_name='path',
    hyperlink='https://typst.app/docs/reference/visualize/path/',
)
def path(
    *vertices: tuple[str, str] | tuple[tuple[str, str], ...],
    fill: str | None = None,
    fill_rule: str = '"non-zero"',
    stroke: str | dict[str, Any] | None = 'auto',
    closed: bool = False,
) -> Block:
    return post_series(
        path, *vertices, fill=fill, fill_rule=fill_rule, stroke=stroke, closed=closed
    )


@implement(
    True,
    original_name='pattern',
    hyperlink='https://typst.app/docs/reference/visualize/pattern/',
)
def pattern(
    body: str,
    /,
    *,
    size: str | Iterable[str] = 'auto',
    spacing: tuple[str, str] = ('0pt', '0pt'),
    relative: str = 'auto',
) -> Block:
    return normal(pattern, body, size=size, spacing=spacing, relative=relative)


@implement(
    True,
    original_name='polygon.regular',
    hyperlink='https://typst.app/docs/reference/visualize/polygon/#definitions-regular',
)
def _polygon_regular(
    *,
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = None,
    size: str = '1em',
    vertices: int = 3,
) -> Block:
    return normal(
        _polygon_regular, fill=fill, stroke=stroke, size=size, vertices=vertices
    )


@attach_func(_polygon_regular, 'regular')
@implement(
    True,
    original_name='polygon',
    hyperlink='https://typst.app/docs/reference/visualize/polygon/',
)
def polygon(
    *vertices: tuple[str, str] | tuple[tuple[str, str], ...],
    fill: str | None = None,
    fill_rule: str = '"non-zero"',
    stroke: str | dict[str, Any] | None = 'auto',
) -> Block:
    return post_series(
        polygon, *vertices, fill=fill, fill_rule=fill_rule, stroke=stroke
    )


@implement(
    True,
    original_name='rect',
    hyperlink='https://typst.app/docs/reference/visualize/rect/',
)
def rect(
    body: str = '',
    /,
    *,
    width: str = 'auto',
    height: str = 'auto',
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = 'auto',
    radius: str | dict[str, Any] = dict(),
    inset: str | dict[str, Any] = '0% + 5pt',
    outset: str | dict[str, Any] = dict(),
) -> Block:
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


@implement(
    True,
    original_name='square',
    hyperlink='https://typst.app/docs/reference/visualize/square/',
)
def square(
    body: str = '',
    /,
    *,
    size: str = 'auto',
    width: str = 'auto',
    height: str = 'auto',
    fill: str | None = None,
    stroke: str | dict[str, Any] | None = 'auto',
    radius: str | dict[str, Any] = dict(),
    inset: str | dict[str, Any] = '0% + 5pt',
    outset: str | dict[str, Any] = dict(),
) -> Block:
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


@implement(
    True,
    original_name='stroke',
    hyperlink='https://typst.app/docs/reference/visualize/stroke/',
)
def stroke(
    paint: Optional[str] = None,
    thickness: Optional[str] = None,
    cap: Optional[str] = None,
    join: Optional[str] = None,
    dash: Optional[str] = None,
    miter_limit: Optional[str] = None,
    /,
) -> Block:
    return positional(stroke, paint, thickness, cap, join, dash, miter_limit)
