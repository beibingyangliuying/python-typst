from typstpy.customizations import (
    instance,
    normal,
    positional,
    post_series,
    pre_series,
)


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


def test_post_series_factory_places_keywords_before_children():
    table = post_series('table')

    assert table('[1]', '[2]', columns=['1fr', '2fr']) == (
        '#table(columns: (1fr, 2fr), [1], [2])'
    )
