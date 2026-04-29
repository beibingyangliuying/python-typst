import pytest

from typstpy.std.visualize import color, curve, gradient, image, rgb


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


@pytest.mark.parametrize(
    'call',
    [
        lambda: color.map('not-a-map'),
        lambda: curve.close(mode='"bad"'),
        lambda: image('"image.png"', fit='"bad"'),
    ],
)
def test_visualize_functions_reject_invalid_arguments(call):
    with pytest.raises(AssertionError):
        call()
