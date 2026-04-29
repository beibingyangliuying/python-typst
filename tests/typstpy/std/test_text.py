import pytest

from typstpy.std.text import highlight, raw, smartquote, text


def test_raw_line_attached_function_renders_typst_call():
    assert raw.line(1, 1, '"a"', '"b"') == '#raw.line(1, 1, "a", "b")'


def test_text_functions_render_representative_outputs():
    assert text('"x"', style='"italic"') == '#text("x", style: "italic")'
    assert smartquote(quotes=('"()"', '"dict()"')) == (
        '#smartquote(quotes: ("()", "dict()"))'
    )


@pytest.mark.parametrize(
    'call',
    [
        lambda: highlight('"x"', top_edge='"bad"'),
        lambda: text('"x"', style='"bad"'),
    ],
)
def test_text_functions_reject_invalid_arguments(call):
    with pytest.raises(AssertionError):
        call()
