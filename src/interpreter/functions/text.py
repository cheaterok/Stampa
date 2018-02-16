import sys

from interpreter.functions.__init__ import args_typecheck

trim = args_typecheck(lambda text: text.strip())(str)
trimt = args_typecheck(lambda text: text.rstrip())(str)
triml = args_typecheck(lambda text: text.lstrip())(str)
nws = None # Дописать
uc = args_typecheck(lambda text: text.upper())(str)
lc = args_typecheck(lambda text: text.lower())(str)

def part():
    # text[n : n + size]
    # Дописать проверку ошибок
    pass

def f(format, *args):
    # Исправить функцию
    sys.stdout.write(format % args)

def sed(text, expr):
    pass

def tr(text, set1, set2):
    pass
