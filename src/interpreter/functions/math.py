import operator
import math


def r(n, p, key):
    dict = {
        "up": lambda n, p: math.ceil(n/p)*p,
        "down": lambda n, p: math.floor(n/p)*p,
        "nearest": lambda n, p: round(n/p)*p
    }
    if key in dict:
        return dict[key](n, p)
    else:
        raise TypeError


div = operator.truediv
rem = operator.mod
abs_ = abs
mod = operator.floordiv

operator_names = ["add", "sub", "mul", "neg"]

for name in operator_names:
    globals()[name] = getattr(operator, name)
