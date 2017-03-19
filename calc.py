"""
Calculator lib

Shunting-yard_algorithm https://en.wikipedia.org/wiki/Shunting-yard_algorithm
Operator-precedence parser
"""

import operator
from collections import namedtuple

operation = namedtuple(
    "operation", ["operator", "precedent", "function"])

OPERATORS = {
    "(": operation("(", -1, None,),
    ")": operation(")", 10, None),
    "^": operation("^", 1, operator.__pow__),
    "*": operation("*", 2, operator.__mul__),
    "/": operation("/", 2, operator.__floordiv__),
    "+": operation("+", 3, operator.__add__),
    "-": operation("-", 3, operator.__sub__),
    None: operation("", 100, None)
}


NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPACE = ' '


class ParseError(Exception):
    """Exception when invalid character in input"""
    pass


class Stack():
    """Stack implementation wrapping Python Lists"""

    def __init__(self, d=None):
        if d is None:
            d = []
        self.d = d

    def dump(self):
        return self.d

    def peek(self):
        return self.d[-1] if len(self) != 0 else None

    def pop(self):
        return self.d.pop()

    def push(self, val):
        if val:
            self.d.append(val)

    def reverse(self):
        self.d = self.d[::-1]

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
    output_stack = Stack()

    for index, t in enumerate(expression):
        if t in NUMBERS:
            if t in NUMBERS:
                if index != 0 and expression[index - 1] in NUMBERS:
                    t = output_stack.pop() + t
            output_stack.push(t)
        elif t == SPACE:
            continue
        elif t in OPERATORS:
            last_token = operator_stack.peek()
            if OPERATORS[t].precedent > OPERATORS[last_token].precedent:
                while operator_stack:
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
        if operator_stack.peek() in "()":
            operator_stack.pop()
        output_stack.push(operator_stack.pop())

    return output_stack


def evaluate(expression):
    """

    type string expression - raw valid expression
    type int    expression

    """

    try:
        # Parse into a Stack and evaluate
        parsed = parse(expression)
        return postfix_eval(parsed)
    except ParseError as e:
        return e


def postfix_eval(s):
    s.reverse()
    temp = Stack()
    while s:
        token = s.pop()
        if token in NUMBERS:
            temp.push(int(token))
        elif token in "()":
            continue
        else:
            op = OPERATORS[token]
            print(op, s, temp)
            if len(temp) < 2:
                right, left = temp.pop(), s.pop()
            else:
                right, left = temp.pop(), temp.pop()
            temp.push(op.function(left, right))
    print(temp.peek())
    return temp.peek()

if __name__ == '__main__':

    postfix_eval(parse("4+8/4"))
    postfix_eval(parse("((4+8)/4)"))
