import doctest
import unittest

from typstpy import functions


def load_tests(loader, tests, ignore):
    modules = [functions]
    for module in modules:
        tests.addTests(doctest.DocTestSuite(module))
    return tests


if __name__ == "__main__":
    unittest.main()
