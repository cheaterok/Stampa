import operator
import math
from functools import reduce


def add(*args):
    return reduce(operator.add, args)


def sub(*args):
    return reduce(operator.sub, args)


def mul(*args):
    return reduce(operator.mul, args)


def div(*args):
    return reduce(operator.truediv, args)


def rem(*args):
    return reduce(operator.mod, args)


def mod(*args):
    return reduce(operator.floordiv, args)


def r(n, p, key):
    dict = {
        "up": lambda n, p: math.ceil(n / p) * p,
        "down": lambda n, p: math.floor(n / p) * p,
        "nearest": lambda n, p: round(n / p) * p
    }
    if key in dict:
        return dict[key](n, p)
    else:
        raise TypeError


abs_ = abs
neg = operator.neg
