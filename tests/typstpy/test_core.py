import pytest

from typstpy._core import (
    implement,
    import_,
    instance,
    normal,
    positional,
    post_series,
    pre_series,
    set_,
    show_,
)
from typstpy.std import heading, outline, text


@implement('demo')
def demo(body='', /, *, fill=None, outlined=True):
    return normal(demo, body, fill=fill, outlined=outlined)


@implement('demo.pos')
def demo_pos(*args):
    return positional(demo_pos, *args)


@implement('demo.method')
def demo_method(target, /, *args, tone='auto'):
    return instance(demo_method, target, *args, tone=tone)


@implement('demo.pre')
def demo_pre(*children, gap='auto'):
    return pre_series(demo_pre, *children, gap=gap)


@implement('demo.post')
def demo_post(*children, gap='auto'):
    return post_series(demo_post, *children, gap=gap)


def test_set_show_and_import_rules_render_typst_code():
    assert set_(heading, outlined=True) == '#set heading(outlined: true)'
    assert show_(heading, set_(text, fill='red')) == (
        '#show heading: set text(fill: red)'
    )
    assert show_(None, 'it => it') == '#show : it => it'
    assert import_('"module.typ"', 'foo', 'bar') == '#import "module.typ": foo, bar'


def test_set_rejects_unknown_function_fields():
    with pytest.raises(AssertionError):
        set_(heading, outline=True)


def test_implemented_functions_have_distinct_where_and_with_helpers():
    assert heading.where(outlined=True) == '#heading.where(outlined: true)'
    assert heading.with_('[Intro]', outlined=False) == (
        '#heading.with([Intro], outlined: false)'
    )
    assert heading.where is not outline.where


@pytest.mark.parametrize('helper', [heading.where, heading.with_])
def test_where_and_with_reject_unknown_function_fields(helper):
    with pytest.raises(AssertionError):
        helper(outline=True)


def test_normal_protocol_omits_defaults_and_renders_non_defaults():
    assert demo('[Hello]') == '#demo([Hello])'
    assert demo('[Hello]', fill='red', outlined=False) == (
        '#demo([Hello], fill: red, outlined: false)'
    )


def test_positional_protocol_renders_tuple_like_call():
    assert demo_pos(1, True, None) == '#demo.pos(1, true, none)'


def test_instance_protocol_renders_method_call():
    assert demo_method(demo_pos(1), '50%', tone='warm') == (
        '#demo.pos(1).demo.method(50%, tone: warm)'
    )


def test_pre_series_protocol_places_children_before_keywords():
    assert demo_pre('[a]', '[b]', gap='1em') == '#demo.pre([a], [b], gap: 1em)'


def test_post_series_protocol_places_keywords_before_children():
    assert demo_post('[a]', '[b]', gap='1em') == '#demo.post(gap: 1em, [a], [b])'
