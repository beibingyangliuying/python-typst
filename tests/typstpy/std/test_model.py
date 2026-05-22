import pytest

from typstpy.std.model import (
    bibliography,
    bullet_list,
    cite,
    figure,
    numbered_list,
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
    assert table.hline(position='bottom') == '#table.hline(position: bottom)'
    assert table.vline(position='right') == '#table.vline(position: right)'
    assert terms.item('"term"', '"description"') == (
        '#terms.item("term", "description")'
    )
    assert numbered_list.item('[Hi]') == '#enum.item([Hi])'
    assert numbered_list.item('[Hi]', number=2) == '#enum.item(2, [Hi])'


def test_model_functions_render_updated_typst_calls():
    assert cite('<label>', form=None) == '#cite(<label>, form: none)'
    assert cite('<label>', form='none') == '#cite(<label>, form: none)'
    assert cite('<label>', style='"apa"') == '#cite(<label>, style: "apa")'
    assert (
        cite('<label>', style='"custom.csl"') == '#cite(<label>, style: "custom.csl")'
    )
    assert bibliography('"bibliography.bib"', style='"custom.csl"') == (
        '#bibliography("bibliography.bib", style: "custom.csl")'
    )
    assert numbered_list('[Hi]') == '#enum([Hi])'
    assert numbered_list('[Hi]', start=1) == '#enum(start: 1, [Hi])'
    assert par.line(numbering='"1"') == '#par.line(numbering: "1")'


def test_table_does_not_spread_single_plain_child():
    assert table('[1]') == '#table([1])'


def test_terms_keeps_single_term_pair_as_one_child():
    assert terms(('[term]', '[description]')) == '#terms(([term], [description]))'


@pytest.mark.parametrize(
    'call',
    [
        lambda: cite('<label>', form='"bad"'),
        lambda: figure('[Body]', scope='"bad"'),
        lambda: par('[Body]', linebreaks='"bad"'),
        lambda: par.line(numbering_scope='"section"'),
        lambda: ref('<label>', form='"bad"'),
        lambda: table.hline(position='middle'),
        lambda: table.vline(position='middle'),
    ],
)
def test_model_functions_reject_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()
