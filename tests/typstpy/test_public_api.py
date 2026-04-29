import typstpy
from typstpy import std, subpar
from typstpy.document import Document


def test_top_level_package_exports_document_and_modules():
    assert typstpy.__all__ == ['std', 'subpar', 'Document']
    assert typstpy.Document is Document
    assert typstpy.std is std
    assert typstpy.subpar is subpar


def test_key_implemented_functions_have_where_and_with_helpers():
    for func in [std.heading, std.figure, std.text, std.grid, std.table]:
        assert callable(func.where)
        assert callable(func.with_)


def test_attached_functions_are_available_from_std_exports():
    assert std.figure.caption('[Hi]') == '#figure.caption([Hi])'
    assert std.grid.cell('[Hi]') == '#grid.cell([Hi])'
    assert std.table.cell('[Hi]') == '#table.cell([Hi])'
