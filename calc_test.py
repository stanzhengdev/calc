
import unittest
from calc import parse, evaluate


class TestParse(unittest.TestCase):

    def test_func(self):
        testcases = [
            ("3+4+5+8"),
            ("4+8/4"),
            ("(4+8)/4"),
            ("((4+8)/4)^2"),
            ("((4+8)/4)^2^3")
        ]
        for test in testcases:
            self.assertEqual(parse(test[0]), test[1])


class TestEvaluate(unittest.TestCase):

    def test_func(self):
        testcases = [
            ("3+3", 6),
            ("2+4*2", 10)
        ]
        for test in testcases:
            self.assertEqual(evaluate(test[0]), test[1])


if __name__ == '__main__':
    unittest.main()
