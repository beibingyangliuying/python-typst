from textwrap import dedent

from typstpy import Document
from typstpy.std import (
    emph,
    figure,
    heading,
    import_,
    lorem,
    par,
    set_,
    show_,
    text,
)


def test_empty_document_renders_empty_string():
    assert str(Document()) == ''


def test_document_with_only_content_has_no_prefix_spacing():
    doc = Document()
    doc.add_content('[Body]')

    assert str(doc) == '[Body]'


def test_document_renders_sections_in_typst_order_with_blank_lines():
    doc = Document()
    doc.add_import('#import "module.typ": foo')
    doc.add_set_rule('#set text(fill: red)')
    doc.add_show_rule('#show heading: it => it')
    doc.add_content('[Body]')

    expected = dedent(
        """
        #import "module.typ": foo

        #set text(fill: red)

        #show heading: it => it

        [Body]
        """
    ).strip()

    assert str(doc) == expected


def test_document_renders_complete_typst_source():
    doc = Document()
    doc.add_import(import_('"@preview/cetz:0.3.1"'))
    doc.add_set_rule(set_(heading, outlined=True))
    doc.add_show_rule(show_(heading, set_(text, fill='red')))
    doc.add_show_rule(show_(figure.caption, emph))
    doc.add_show_rule(show_(None, 'it => it'))
    doc.add_content(heading(lorem(20)))
    doc.add_content(par(lorem(20)))

    expected = dedent(
        """
        #import "@preview/cetz:0.3.1": 

        #set heading(outlined: true)

        #show heading: set text(fill: red)
        #show figure.caption: emph
        #show : it => it

        #heading(lorem(20))

        #par(lorem(20))
        """
    ).strip()

    assert str(doc) == expected
