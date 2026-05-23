import warnings

import pytest

from typstpy._core import (
    attach_func,
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
from typstpy._core.render import render_value
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
    assert show_(None, 'it => it') == '#show: it => it'
    assert import_('"module.typ"', 'foo', 'bar') == '#import "module.typ": foo, bar'
    assert import_('"module.typ"') == '#import "module.typ"'


def test_attach_func_default_name_uses_attached_function_name():
    def child():
        return '#child'

    @attach_func(child)
    def parent():
        return '#parent'

    assert parent.child is child


def test_set_rejects_unknown_function_fields():
    with pytest.raises(TypeError):
        set_(heading, outline=True)


def test_implemented_functions_have_distinct_where_and_with_helpers():
    assert heading.where(outlined=True) == '#heading.where(outlined: true)'
    assert heading.with_('[Intro]', outlined=False) == (
        '#heading.with([Intro], outlined: false)'
    )
    assert heading.where is not outline.where


@pytest.mark.parametrize('helper', [heading.where, heading.with_])
def test_where_and_with_reject_unknown_function_fields(helper):
    with pytest.raises(TypeError):
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


def test_pre_series_protocol_does_not_spread_single_plain_child():
    assert demo_pre('[a]') == '#demo.pre([a])'


def test_post_series_protocol_places_keywords_before_children():
    assert demo_post('[a]', '[b]', gap='1em') == '#demo.post(gap: 1em, [a], [b])'


def test_post_series_protocol_does_not_spread_single_plain_child():
    assert demo_post('[a]') == '#demo.post([a])'


class TestRenderValue:
    def test_bool_renders_lowercase(self):
        assert render_value(True) == 'true'
        assert render_value(False) == 'false'

    def test_none_renders_lowercase(self):
        assert render_value(None) == 'none'

    def test_str_preserves_content(self):
        assert render_value('hello') == 'hello'
        assert render_value('[Hi]') == '[Hi]'

    def test_str_strips_leading_hash(self):
        assert render_value('#red') == 'red'
        assert render_value('#grid') == 'grid'

    def test_bytes_raises_typeerror(self):
        with pytest.raises(TypeError, match='bytes-like'):
            render_value(b'data')
        with pytest.raises(TypeError, match='bytes-like'):
            render_value(bytearray(b'data'))
        with pytest.raises(TypeError, match='bytes-like'):
            render_value(memoryview(b'data'))

    def test_empty_dict_renders_empty_map(self):
        assert render_value({}) == '(:)'

    def test_dict_renders_map_with_kebab_keys(self):
        assert render_value({'fill': 'red', 'column_gutter': '1em'}) == (
            '(fill: red, column-gutter: 1em)'
        )

    def test_empty_list_renders_empty_sequence(self):
        assert render_value([]) == '()'
        assert render_value(()) == '()'

    def test_list_renders_sequence(self):
        assert render_value(['1fr', '2fr', '3fr']) == '(1fr, 2fr, 3fr)'

    def test_nested_mapping_in_sequence(self):
        result = render_value([{'x': '1em'}, {'y': '2em'}])
        assert result == '((x: 1em), (y: 2em))'

    def test_nested_sequence_in_mapping(self):
        result = render_value({'dash': ['solid', '1em']})
        assert result == '(dash: (solid, 1em))'

    def test_deeply_nested_structure(self):
        result = render_value({'columns': ('1fr', '2fr'), 'fill': None})
        assert result == '(columns: (1fr, 2fr), fill: none)'

    def test_unregistered_callable_warns_and_uses_name(self):
        def unregistered():
            return ''

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            render_value(unregistered)
            assert len(w) == 1
            assert 'not been registered' in str(w[0].message)

    def test_placeholder_object_renders_str(self):
        assert render_value(42) == '42'
        assert render_value(3.14) == '3.14'
