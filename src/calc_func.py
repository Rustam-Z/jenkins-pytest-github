"""
calc_func.py contains math functions with no side effects.
"""


def add(a, b):
    summation = a + b
    if 1 > summation > 0.1:
        return round(summation, 2)
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a * 1.0 / b


def maximum(a, b):
    return a if a >= b else b


def minimum(a, b):
    return a if a <= b else b
