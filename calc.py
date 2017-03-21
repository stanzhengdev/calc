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


class EvaluationError(Exception):
    """Exception when invalid expression evaluation"""
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
        return self.d.pop() if len(self) != 0 else None

    def push(self, val):
        if val is not None:
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

    args:
        expression - a string expression that is parsed to be evaluated

    returns:
        Stack - a post-fix oriented stack
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

    args:
        type string expression - raw valid expression
    returns:
        integer - evaluation of statement is valid
    raises:
        ParseError - if the expression has invalid unrecognized characters that cannot be identified
    """

    try:
        # Parse into a Stack and evaluate
        parsed = parse(expression)
        exp = postfix_eval(parsed)
        return exp
    except ParseError as parse_error:
        return parse_error
    except (EvaluationError) as e:
        return None
    except Exception:
        return "Error"


def postfix_eval(stack):
    """postfix_eval takes a stack and evaluates the function

    args:
        stack (Stack): prepared expression put in postfix notation

    returns:
        int: integer evaluation of the expression
    """
    try:
        stack.reverse()
        temp = Stack()
        while stack:
            token = stack.pop()
            if token in "()":
                continue
            elif token in OPERATORS:
                oper = OPERATORS[token]
                if len(temp) < 2:
                    right, left = temp.pop(), stack.pop()
                else:
                    right, left = temp.pop(), temp.pop()
                temp.push(oper.function(left, right))
            else:
                temp.push(int(token))

            if temp.peek() is None:
                raise EvaluationError
        return temp.peek()
    except (TypeError, EvaluationError) as e:
        return EvaluationError("Cannot be evaluated")
