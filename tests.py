import doctest
import unittest


def load_tests(loader, tests, ignore):
    modules = [f'typstpy.std.{i}' for i in ['layout', 'model', 'text', 'visualize']] + [
        'typstpy.utils',
        'typstpy.document',
    ]
    for module in modules:
        tests.addTests(doctest.DocTestSuite(module))
    return tests


class MainTestCase(unittest.TestCase):
    def test_where_with(self):
        from typstpy.std import heading, outline

        self.assertRaises(ValueError, heading.where, outline=True)  # type: ignore
        self.assertRaises(ValueError, heading.with_, outline=True)  # type: ignore
        self.assertFalse(heading.where is outline.where)  # type: ignore

    def test_document(self):
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

        doc = Document()
        doc.add_import(import_('"@preview/cetz:0.3.1"'))
        doc.add_set_rule(set_(heading, outlined=True))
        doc.add_show_rule(show_(heading, set_(text, fill='red')))
        doc.add_show_rule(show_(figure.caption, emph))  # type: ignore
        doc.add_show_rule(show_(None, 'it => it'))
        doc.add_content(heading(lorem(20)))
        doc.add_content(par(lorem(20)))

        self.assertEqual(
            str(doc),
            """
#import "@preview/cetz:0.3.1": 

#set heading(outlined: true)

#show heading: set text(fill: red)
#show figure.caption: emph
#show : it => it

#heading(lorem(20))

#par(lorem(20))
""".strip(),
        )


if __name__ == '__main__':
    unittest.main()
