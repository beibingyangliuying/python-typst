import pytest

from typstpy.std.layout import (
    align,
    columns,
    grid,
    pad,
    page,
    pagebreak,
    place,
    rotate,
    scale,
    stack,
)


def test_layout_attached_functions_render_typst_calls():
    assert grid.cell('[Hi]', x=1) == '#grid.cell([Hi], x: 1)'
    assert grid.hline(y=2) == '#grid.hline(y: 2)'
    assert grid.hline(position='bottom') == '#grid.hline(position: bottom)'
    assert grid.vline(position='right') == '#grid.vline(position: right)'
    assert grid.header('[Head]', level=2) == '#grid.header(level: 2, [Head])'
    assert grid.footer('[Foot]') == '#grid.footer([Foot])'
    assert place.flush() == '#place.flush()'


def test_layout_functions_render_updated_typst_calls():
    assert align('[Hi]') == '#align([Hi])'
    assert align('[Hi]', 'center') == '#align(center, [Hi])'
    assert columns('[Hi]', 3) == '#columns(3, [Hi])'
    assert columns('[Hi]', 3, gutter='8% + 0pt') == (
        '#columns(3, [Hi], gutter: 8% + 0pt)'
    )
    assert pad('[Hi]', '1em') == '#pad(1em, [Hi])'
    assert page() == '#page()'
    assert page('[Body]', supplement='[p.]') == '#page([Body], supplement: [p.])'
    assert page('[Body]', footer_descent='20% + 0pt') == (
        '#page([Body], footer-descent: 20% + 0pt)'
    )
    assert page('[Body]', footer_ascent='20% + 0pt') == (
        '#page([Body], footer-descent: 20% + 0pt)'
    )
    assert page('[Body]', binding='left') == '#page([Body], binding: left)'
    assert pagebreak(to='"odd"') == '#pagebreak(to: "odd")'
    assert place('[Hi]', 'top') == '#place(top, [Hi])'
    assert rotate('[Hi]', '20deg') == '#rotate(20deg, [Hi])'
    assert scale('[Hi]', '50%') == '#scale(50%, [Hi])'


def test_stack_uses_post_series_order():
    assert stack('[a]', '[b]', dir='btt') == '#stack(dir: btt, [a], [b])'


def test_stack_does_not_spread_single_plain_child():
    assert stack('[a]') == '#stack([a])'


def test_page_rejects_unknown_paper_size():
    with pytest.raises(ValueError):
        page('[Body]', paper='"not-a-paper"')


@pytest.mark.parametrize(
    'call',
    [
        lambda: grid.hline(position='middle'),
        lambda: grid.vline(position='middle'),
        lambda: page('[Body]', binding='middle'),
        lambda: pagebreak(to='"middle"'),
        lambda: place('[Body]', scope='"bad"'),
        lambda: stack('[Body]', dir='diagonal'),
    ],
)
def test_layout_functions_reject_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()


@pytest.mark.parametrize(
    'call',
    [
        lambda: page('[Body]', footer_descent='20% + 0pt', footer_ascent='10% + 0pt'),
        lambda: page('[Body]', not_a_field=True),
    ],
)
def test_page_rejects_invalid_legacy_kwargs(call):
    with pytest.raises(TypeError):
        call()
