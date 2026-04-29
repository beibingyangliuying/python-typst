import pytest

from typstpy.std.model import (
    bibliography,
    bullet_list,
    cite,
    figure,
    par,
    ref,
    table,
    terms,
)


def test_model_attached_functions_render_typst_calls():
    assert bullet_list.item('[Hi]') == '#list.item([Hi])'
    assert figure.caption('[Hi]', position='top') == (
        '#figure.caption([Hi], position: top)'
    )
    assert table.cell('[Hi]', x=1) == '#table.cell([Hi], x: 1)'
    assert terms.item('"term"', '"description"') == (
        '#terms.item("term", "description")'
    )


@pytest.mark.parametrize(
    'call',
    [
        lambda: bibliography('"bibliography.bib"', style='"not-a-style"'),
        lambda: cite('<label>', form='"bad"'),
        lambda: figure('[Body]', scope='"bad"'),
        lambda: par('[Body]', linebreaks='"bad"'),
        lambda: ref('<label>', form='"bad"'),
    ],
)
def test_model_functions_reject_invalid_arguments(call):
    with pytest.raises(AssertionError):
        call()
