
class ParseError(Exception):
    pass


def parse(expression):
    pass


def evaluate(expression, base=10):
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
