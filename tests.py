import doctest
import unittest


def load_tests(loader, tests, ignore):
    modules = [f'typstpy.std.{i}' for i in ['layout', 'model', 'text', 'visualize']] + [
        'typstpy.utils'
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


if __name__ == '__main__':
    unittest.main()
