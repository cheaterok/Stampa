import operator
from functools import reduce
from numbers import Number


def args_typecheck(type):
    """
    Декоратор для проверки типов аргументов функции.
    """
    
    def wrapper(func):
        def inner(*args):
            if not all(map(lambda x: isinstance(x, type), args)):
                raise TypeError
            return func(*args)

        return inner

    return wrapper


def bool_to_int(func):
    """
    Декоратор для конвертирования булевого результата функции в числовой (1 или 0).
    """

    def wrapper(*args):
        return int(func(*args))

    return wrapper


@bool_to_int
def and_(*args):
    return all(args)


@bool_to_int
def or_(*args):
    return any(args)


@bool_to_int
def not_(a):
    return not a


@bool_to_int
@args_typecheck(str)
def seq(*args):
    return reduce(operator.eq, args)


@args_typecheck(str)
@bool_to_int
def sne(*args):
    return reduce(operator.ne, args)


@args_typecheck(str)
@bool_to_int
def sgt(*args):
    return reduce(operator.gt, args)


@args_typecheck(str)
@bool_to_int
def sge(*args):
    return reduce(operator.ge, args)


@args_typecheck(str)
@bool_to_int
def slt(*args):
    return reduce(operator.lt, args)


@args_typecheck(str)
@bool_to_int
def sle(*args):
    return reduce(operator.le, args)


@args_typecheck(Number)
@bool_to_int
def neq(*args):
    return reduce(operator.eq, args)


@args_typecheck(Number)
@bool_to_int
def nne(*args):
    return reduce(operator.ne, args)


@args_typecheck(Number)
@bool_to_int
def ngt(*args):
    return reduce(operator.gt, args)


@args_typecheck(Number)
@bool_to_int
def nge(*args):
    return reduce(operator.ge, args)


@args_typecheck(Number)
@bool_to_int
def nlt(*args):
    return reduce(operator.lt, args)


@args_typecheck(Number)
@bool_to_int
def nle(*args):
    return reduce(operator.le, args)


even = lambda x: x % 2 == 0

odd = lambda x: x % 2 != 0
