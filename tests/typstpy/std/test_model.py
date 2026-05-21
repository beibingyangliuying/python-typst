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


def test_table_does_not_spread_single_plain_child():
    assert table('[1]') == '#table([1])'


def test_terms_keeps_single_term_pair_as_one_child():
    assert terms(('[term]', '[description]')) == '#terms(([term], [description]))'


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
    with pytest.raises(ValueError):
        call()
