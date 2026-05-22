import pytest

from typstpy.std.text import highlight, raw, smartquote, subscript, superscript, text


def test_raw_line_attached_function_renders_typst_call():
    assert raw.line(1, 1, '"a"', '"b"') == '#raw.line(1, 1, "a", "b")'


def test_text_functions_render_representative_outputs():
    assert text('"x"', style='"italic"') == '#text("x", style: "italic")'
    assert text('"x"', baseline='1pt') == '#text("x", baseline: 1pt)'
    assert text('"x"', cjk_latin_spacing=None) == (
        '#text("x", cjk-latin-spacing: none)'
    )
    assert text('"x"', dir='rtl') == '#text("x", dir: rtl)'
    assert text('"x"', weight=100) == '#text("x", weight: 100)'
    assert text('"x"', stylistic_set=(1, 20)) == ('#text("x", stylistic-set: (1, 20))')
    assert subscript('"x"', typographic=False) == '#sub("x", typographic: false)'
    assert superscript('"x"', typographic=False) == '#super("x", typographic: false)'
    assert smartquote(quotes=('"()"', '"dict()"')) == (
        '#smartquote(quotes: ("()", "dict()"))'
    )


@pytest.mark.parametrize(
    'call',
    [
        lambda: highlight('"x"', top_edge='"bad"'),
        lambda: text('"x"', style='"bad"'),
        lambda: text('"x"', weight=99),
        lambda: text('"x"', cjk_latin_spacing='bad'),
        lambda: text('"x"', dir='diagonal'),
        lambda: text('"x"', stylistic_set=(0,)),
        lambda: text('"x"', stylistic_set=(21,)),
    ],
)
def test_text_functions_reject_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()
