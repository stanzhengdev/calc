
import unittest
from calc import parse, evaluate, Stack, postfix_eval

# testcase = namedtuple("testcase", ["expression", "representation", "sum"])
testcases = [
    ("5+4", ['5', '4', '+'], 9),
    ("1-5", ['1', '5', '-'], -4),
    ("(4/2)", ['4', '2', '/'], 2),
    ("4*2", ['4', '2', '*'], 8),
    ("3+4+5+8", ['3', '4', '5', '8', '+', '+', '+'], 20),
    ("(4 + 8) / 4)", ['4', '8', '+', '4', '/'], 3),
    ("((4+8)/4)^2", ['4', '8', '+', '4', '/', '2', '^'], 9),
    ('((4+8)/4)^2^3', ['4', '8', '+',  '4', '/', '2', '3', '^', '^'], 6561)
]


class TestParse(unittest.TestCase):

    def test_func(self):
        for test in testcases:
            print(parse(test[0]))
            parsed = list(i for i in parse(test[0]).dump() if i not in "()")
            if parsed:
                self.assertEqual(parsed, test[1])


class TestEvaluate(unittest.TestCase):

    def test_func(self):
        for test in testcases:
            init_stack = Stack(test[1])
            self.assertEqual(postfix_eval(init_stack), test[2])


if __name__ == '__main__':
    unittest.main()
