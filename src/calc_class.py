"""
calc_class.py contains the Calculator class.
It uses the math functions from calc_func.
"""

import src.calc_func as calc


class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def _do_math(self, a, b, func):
        self._last_answer = func(a, b)
        return self.last_answer

    def add(self, a, b):
        return self._do_math(a, b, calc.add)

    def subtract(self, a, b):
        return self._do_math(a, b, calc.subtract)

    def multiply(self, a, b):
        return self._do_math(a, b, calc.multiply)

    def divide(self, a, b):
        return self._do_math(a, b, calc.divide)

    def maximum(self, a, b):
        return self._do_math(a, b, calc.maximum)

    def minimum(self, a, b):
        return self._do_math(a, b, calc.minimum)


if __name__ == "__main__":
    c = Calculator()
    print(c.add(10, 23))
    print(c.multiply(11, 11))
