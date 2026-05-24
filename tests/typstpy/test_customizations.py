from typstpy.customizations import (
    call_,
    instance,
    normal,
    positional,
    post_series,
    pre_series,
)


def test_call_factory_renders_positional_args_and_keywords():
    demo = call_('demo')

    assert demo(1, 2, 3, fill='red') == '#demo(1, 2, 3, fill: red)'


def test_call_factory_renders_only_keywords():
    demo = call_('demo')

    assert demo(fill='red') == '#demo(fill: red)'


def test_normal_factory_renders_body_and_keywords():
    pad = normal('pad')

    assert pad('[Hello]', left='1em') == '#pad([Hello], left: 1em)'


def test_positional_factory_renders_positional_arguments():
    rgb = positional('rgb')

    assert rgb(255, 255, 255, '50%') == '#rgb(255, 255, 255, 50%)'


def test_instance_factory_renders_method_call():
    rgb = positional('rgb')
    lighten = instance('lighten')

    assert lighten(rgb(255, 255, 255), '50%') == ('#rgb(255, 255, 255).lighten(50%)')


def test_pre_series_factory_places_children_before_keywords():
    subpar_grid = pre_series('subpar.grid')

    assert subpar_grid('[]', '[]', columns=('1fr', '1fr')) == (
        '#subpar.grid([], [], columns: (1fr, 1fr))'
    )


def test_pre_series_factory_does_not_spread_single_plain_child():
    subpar_grid = pre_series('subpar.grid')

    assert subpar_grid('[]') == '#subpar.grid([])'


def test_pre_series_factory_spreads_single_sequence():
    subpar_grid = pre_series('subpar.grid')

    assert subpar_grid(('[]', '[]')) == '#subpar.grid(..([], []))'


def test_pre_series_factory_spreads_single_sequence_for_custom_label():
    demo_series = pre_series('demo.series')

    assert demo_series(('[a]', '[b]')) == '#demo.series(..([a], [b]))'


def test_post_series_factory_places_keywords_before_children():
    table = post_series('table')

    assert table('[1]', '[2]', columns=['1fr', '2fr']) == (
        '#table(columns: (1fr, 2fr), [1], [2])'
    )


def test_post_series_factory_does_not_spread_single_plain_child():
    table = post_series('table')

    assert table('[1]') == '#table([1])'


def test_post_series_factory_spreads_single_sequence():
    table = post_series('table')

    assert table(('[1]', '[2]')) == '#table(..([1], [2]))'


def test_post_series_factory_spreads_single_sequence_for_custom_label():
    demo_series = post_series('demo.series')

    assert demo_series(('[a]', '[b]')) == '#demo.series(..([a], [b]))'
