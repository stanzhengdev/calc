
"""

A calculator function that takes a single string
of input that includes numbers and operators and returns the numeric result of the equation.

Examples:
- A string of "5+5+32" returns 42 as an integer
- A string of "3 * 4" returns 12 as an integer
"""

import calc


def main():

    while True:
        print("Enter a statement to be evaluated: ")
        exp = input()
        print("expression '{}' was evaluated to {}".format(
            exp, calc.evaluate(exp)))

if __name__ == '__main__':
    main()
