"""
Calculator lib

Shunting-yard_algorithm https://en.wikipedia.org/wiki/Shunting-yard_algorithm
Operator-precedence parser
"""


OPERATORS = {
    "(": 0,
    ")": 0,
    "^": 1,
    "*": 2,
    "/": 2,
    "+": 3,
    "-": 3,
    None: 100
}
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPACE = ' '


class ParseError(Exception):
    pass


class Stack():
    """Stack implementation wrapping Python Lists"""

    def __init__(self):
        self.d = []

    def peek(self):
        return self.d[-1] if len(self) != 0 else None

    def pop(self):
        return self.d.pop()

    def push(self, val):
        if val:
            self.d.append(val)

    def __len__(self):
        return len(self.d)

    def __str__(self):
        return str(self.d)


def parse(expression):
    """
    Parses an expression into postfix notation to be evaluated later stackwise
    # Assumes one character-size token/operators

    If Invalid expression, can raise a ParseError
    """

    operator_stack = Stack()
    precedent = Stack()
    output_stack = Stack()

    for t in expression:
        if t in NUMBERS:
            output_stack.push(t)
        elif t == SPACE:
            continue
        elif t in OPERATORS:
            while operator_stack:
                last_token = operator_stack.peek()
                if t != ")" and last_token != "(":
                    output_stack.push(operator_stack.pop())
                else:
                    if last_token != "(":
                        output_stack.push(operator_stack.pop())
                    else:
                        operator_stack.pop()
                        break
            if t != ")":
                operator_stack.push(t)
        else:
            raise ParseError("Invalid Character")
    while operator_stack:
        output_stack.push(operator_stack.pop())

    return output_stack


def evaluate(expression):
    """

    type string expression - raw valid expression
    type int    expression

    """

    try:
        # BUILD AST
        # Evaluate infix Style
        # parse (expression )
        return eval(expression)
    except ParseError as e:
        return e
    except Exception as e:
        return False
