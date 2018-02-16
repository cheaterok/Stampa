import operator
from numbers import Number

from interpreter.functions.__init__ import args_typecheck


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


# Оказывается, что функции из модуля operator называются так же
# и делают то же, что и функции из библиотеки интерпретатора
# Можем использовать это для автоматической кодогенерации
# Названия нужных функций из operator приведены в списке ниже,
# названия функций из библиотеки формируются как [s/n](тип строка или число) + название соотв. функции из operator
operator_names = ["eq", "ne", "gt", "ge", "lt", "le"]

for name in operator_names:
    globals()["s" + name] = bool_to_int(args_typecheck(getattr(operator, name))(str))
    globals()["n" + name] = bool_to_int(args_typecheck(getattr(operator, name))(Number))

even = lambda x: x % 2 == 0

odd = lambda x: x % 2 != 0
