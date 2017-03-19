
import unittest
from calc import parse, evaluate, Stack, postfix_eval, ParseError, EvaluationError

# testcase = namedtuple("testcase", ["expression", "representation", "sum"])
testcases = [
    # basic testing
    ("5+4", ['5', '4', '+'], 9),
    ("1-5", ['1', '5', '-'], -4),
    ("(4/2)", ['4', '2', '/'], 2),
    ("4*2", ['4', '2', '*'], 8),
    ("3+4+5+8", ['3', '4', '5', '8', '+', '+', '+'], 20),
    ("(4 + 8) / 4)", ['4', '8', '+', '4', '/'], 3),
    ("((4+8)/4)^2", ['4', '8', '+', '4', '/', '2', '^'], 9),
    ('((4+8)/4)^2^3', ['4', '8', '+',  '4', '/', '2', '3', '^', '^'], 6561),
    ("314*2", ['314', '2', '*'], 628),
    # mentioned testing
    ("5+5+32", ['5', '5', '32', '+', '+'], 42),
    ("3 * 4", ['3', '4', '*'], 12),
    # edgecase testing
    ("0001 + 1002", ['0001', '1002', '+'], 1003)
]


class TestParse(unittest.TestCase):
    """tests the calc.parse method"""

    test_raise_data = [
        ("c4lculat0r", ParseError),
        ("(|)", ParseError),
    ]

    def test_func(self):
        for test in testcases:
            # cleanup Stackinput
            parsed = list(i for i in parse(test[0]).dump() if i not in "()")
            if parsed:
                self.assertEqual(parsed, test[1])

    def test_raise(self):

        for test in self.test_raise_data:
            with self.assertRaises(test[1]):
                parse(test[0])


class TestEvaluate(unittest.TestCase):
    """tests the evaluate method"""

    def test_func(self):
        for test in testcases:
            init_stack = Stack(test[1])
            self.assertEqual(postfix_eval(init_stack), test[2])


if __name__ == '__main__':
    unittest.main()
