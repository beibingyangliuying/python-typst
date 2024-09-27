"""Unit tests for package `typstpy`."""

import doctest
import unittest

from typstpy import functions, param_types
from typstpy.param_types import types


def load_tests(loader, tests, ignore):
    modules = [functions, param_types, types]
    for module in modules:
        tests.addTests(doctest.DocTestSuite(module))
    return tests


class ParamTypesTestCase(unittest.TestCase):
    def test_length_ratio_operations(self):
        from typstpy import Length, Ratio

        self.assertEqual(str(Length(10, "pt") + Length(20, "mm")), "10pt+20mm")
        self.assertEqual(str(Length(10, "pt") - Length(20, "mm")), "10pt-20mm")
        self.assertEqual(str(Length(10, "pt") - Length(-20, "mm")), "10pt+20mm")
        self.assertEqual(str(Length(10, "pt") + Ratio(20)), "10pt+20%")
        self.assertEqual(str(Length(10, "pt") - Ratio(20)), "10pt-20%")
        self.assertEqual(
            str(Length(10, "pt") - Ratio(20) + Length(20, "pt")), "10pt-20%+20pt"
        )
        self.assertEqual(
            str(Length(10, "pt") - (Ratio(20) + Length(20, "pt"))), "10pt-20%-20pt"
        )
        self.assertEqual(
            str(Length(10, "pt") - Ratio(20) - Length(20, "pt")), "10pt-20%-20pt"
        )
        self.assertEqual(
            str(Length(10, "pt") - (Ratio(20) - Length(20, "pt"))), "10pt-20%+20pt"
        )
        self.assertEqual(str(Length(10, "pt") - Ratio(20)), "10pt-20%")
        self.assertEqual(str(Length(10, "pt") + Ratio(20)), "10pt+20%")
        self.assertEqual(
            str((Length(10, "pt") + Ratio(20)) + (Length(10, "pt") + Ratio(20))),
            "10pt+20%+10pt+20%",
        )
        self.assertEqual(
            str((Length(10, "pt") + Ratio(20)) - (Length(10, "pt") + Ratio(20))),
            "10pt+20%-10pt-20%",
        )


class DocumentTestCase(unittest.TestCase):
    def test_document(self):
        from typstpy import (
            Alignment,
            Angle,
            Block,
            Color,
            Content,
            Document,
            Label,
            Length,
            Ratio,
            Relative,
            bibliography,
            cite,
            cmyk,
            color,
            emph,
            figure,
            heading,
            image,
            lorem,
            luma,
            pagebreak,
            par,
            ref,
            rgb,
            strong,
            text,
        )

        document = Document()
        document.add_block(heading("Hello, World!", level=2))
        document.add_block(par("Hello, World!", justify=True))
        document.add_block(
            figure(
                image("image.png", width=Ratio(70)),
                caption=Content("This is a figure."),
                label=Label("fig:figure"),
            )
        )
        document.add_block(
            par(f"Please see {ref(Label('fig:figure'))} for more information.")
        )
        document.add_block(par(lorem(100)))

        print(document)


if __name__ == "__main__":
    unittest.main()
