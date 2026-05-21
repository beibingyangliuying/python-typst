import pytest

import typstpy.std as std


@pytest.mark.parametrize('name', std.__all__)
def test_std_all_names_are_importable(name):
    assert hasattr(std, name)


def test_std_exports_core_rule_helpers():
    assert std.import_('"module.typ"', 'foo') == '#import "module.typ": foo'
    assert std.set_(std.heading, outlined=True) == '#set heading(outlined: true)'
    assert std.show_(None, 'it => it') == '#show: it => it'
