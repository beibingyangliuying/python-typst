from typing import Any, cast

import pytest

from typstpy.std.visualize import (
    circle,
    cmyk,
    color,
    curve,
    gradient,
    image,
    oklab,
    oklch,
    path,
    polygon,
    rgb,
    square,
)

rgb_untyped = cast(Any, rgb)


def test_visualize_attached_functions_render_typst_calls():
    assert color.lighten(rgb(255, 255, 255), '50%') == (
        '#rgb(255, 255, 255).lighten(50%)'
    )
    assert gradient.kind(gradient.linear('red', 'blue')) == (
        '#gradient.linear(red, blue).kind()'
    )
    assert curve.move(('10pt', '10pt')) == '#curve.move((10pt, 10pt))'


def test_image_renders_representative_output():
    assert (
        image('"image.png"', fit='"contain"') == '#image("image.png", fit: "contain")'
    )
    assert image('"document.pdf"', page=2) == '#image("document.pdf", page: 2)'
    assert image('"image.webp"', format='"webp"', scaling='"pixelated"') == (
        '#image("image.webp", format: "webp", scaling: "pixelated")'
    )


def test_visualize_functions_render_updated_typst_calls():
    assert circle('[Hi]', width='100%') == '#circle([Hi], width: 100%)'
    assert square('[Hi]', width='100%') == '#square([Hi], width: 100%)'
    assert oklab(rgb(0, 0, 0)) == '#oklab(rgb(0, 0, 0))'
    assert oklch(rgb(0, 0, 0)) == '#oklch(rgb(0, 0, 0))'
    assert color.linear_rgb(rgb(0, 0, 0)) == '#color.linear-rgb(rgb(0, 0, 0))'
    assert cmyk(rgb(0, 0, 0)) == '#cmyk(rgb(0, 0, 0))'
    assert color.hsl(rgb(0, 0, 0)) == '#color.hsl(rgb(0, 0, 0))'
    assert color.hsv(rgb(0, 0, 0)) == '#color.hsv(rgb(0, 0, 0))'
    assert gradient.linear('red', 'blue', dir='ttb') == (
        '#gradient.linear(red, blue, dir: ttb)'
    )
    assert gradient.linear('red', 'blue', angle='45deg') == (
        '#gradient.linear(red, blue, angle: 45deg)'
    )
    assert image.decode('"data"', format='"pdf"', scaling='"smooth"') == (
        '#image.decode("data", format: "pdf", scaling: "smooth")'
    )


def test_path_and_polygon_accept_even_odd_fill_rule():
    assert path(('0%', '0%'), fill_rule='"even-odd"') == (
        '#path(fill-rule: "even-odd", (0%, 0%))'
    )
    assert polygon(('0%', '0%'), fill_rule='"even-odd"') == (
        '#polygon(fill-rule: "even-odd", (0%, 0%))'
    )


@pytest.mark.parametrize(
    'call',
    [
        lambda: color.map('not-a-map'),
        lambda: circle('[Hi]', width='100%', height='100%'),
        lambda: curve.close(mode='"bad"'),
        lambda: image('"image.png"', fit='"bad"'),
        lambda: image('"image.png"', format='"bmp"'),
        lambda: image('"image.png"', scaling='"nearest"'),
        lambda: square('[Hi]', size='1em', width='100%'),
    ],
)
def test_visualize_functions_reject_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()


@pytest.mark.parametrize(
    'call',
    [
        lambda: rgb_untyped(),
        lambda: rgb_untyped(1, 2),
        lambda: oklab('50%', '0%'),
        lambda: oklch('50%', '0%'),
        lambda: color.linear_rgb('50%', '50%'),
        lambda: cmyk('0%', '0%', '0%'),
        lambda: color.hsl('0deg', '50%'),
        lambda: color.hsv('0deg', '50%'),
    ],
)
def test_color_constructors_reject_invalid_argument_counts(call):
    with pytest.raises(TypeError):
        call()
