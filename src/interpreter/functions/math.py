import operator
from numbers import Number
import math

from interpreter.functions.__init__ import args_typecheck


def r(n, p, key):
    dict = {
        "up": lambda n, p: math.ceil(n/p)*p,
        "down" : lambda n, p: math.floor(n/p)*p,
        "nearest": lambda n, p: round(n/p)*p
    }
    if key in dict:
        return dict[key](n, p)
    else:
        raise TypeError


div = lambda x, y: x/y
rem = lambda x, y: x % y
abs_ = lambda x: abs(x)
mod = lambda x, y: x//y

operator_names = ["add", "sub", "mul", "neg"]

for name in operator_names:
    globals()[name] = args_typecheck(getattr(operator, name))(Number)
