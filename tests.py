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


if __name__ == "__main__":
    unittest.main()
