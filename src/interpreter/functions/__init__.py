def args_typecheck(func):
    """
    Декоратор для проверки типов аргументов функции.
    """
    def wrapper(type):
        def inner(*args):
            if not all(map(lambda x: isinstance(x, type), args)):
                raise TypeError
            return func(*args)
        return inner
    return wrapper