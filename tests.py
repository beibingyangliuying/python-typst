import doctest
import unittest


def load_tests(loader, tests, ignore):
    modules = [f'typstpy.std.{i}' for i in ['layout', 'model', 'text', 'visualize']] + [
        'typstpy._utils.concepts'
    ]
    for module in modules:
        tests.addTests(doctest.DocTestSuite(module))
    return tests


if __name__ == '__main__':
    unittest.main()
