from typing import Any, cast

import pytest

from typstpy.std.visualize import color, curve, gradient, image, path, polygon, rgb

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
        lambda: curve.close(mode='"bad"'),
        lambda: image('"image.png"', fit='"bad"'),
    ],
)
def test_visualize_functions_reject_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()


@pytest.mark.parametrize('call', [lambda: rgb_untyped(), lambda: rgb_untyped(1, 2)])
def test_rgb_rejects_invalid_argument_counts(call):
    with pytest.raises(TypeError):
        call()
