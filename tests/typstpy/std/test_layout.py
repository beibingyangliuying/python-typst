import pytest

from typstpy.std.layout import grid, page, place, stack


def test_layout_attached_functions_render_typst_calls():
    assert grid.cell('[Hi]', x=1) == '#grid.cell([Hi], x: 1)'
    assert grid.hline(y=2) == '#grid.hline(y: 2)'
    assert place.flush() == '#place.flush()'


def test_stack_uses_post_series_order():
    assert stack('[a]', '[b]', dir='btt') == '#stack(dir: btt, [a], [b])'


def test_page_rejects_unknown_paper_size():
    with pytest.raises(AssertionError):
        page('[Body]', paper='"not-a-paper"')
