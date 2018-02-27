from .lexer import tokens

import ply.yacc as yacc

import interpreter.functions as functions


def p_funccall(p):
    """
    funccall : IDENTIFIER
             | IDENTIFIER OPENBKT args CLOSEBKT
    """
    func = getattr(functions, p[1])
    if len(p) == 2:
        p[0] = func()
    else:
        p[0] = func(*p[3])


def p_funccall_dflttext(p):
    """
    funccall : funccall DFLTTEXT STR
             | funccall DFLTFUNC funccall
    """
    if p[1] == '':
        p[0] = p[3]
    else:
        p[0] = p[1]


def p_args(p):
    """
    args :
         | arg
         | args ARGSEP arg
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_args_concatenation(p):
    """
    args : args arg
    """
    p[1][-1] = p[1][-1] + p[2]
    p[0] = p[1]


def p_args_missed_arg(p):
    """
    args : args ARGSEP ARGSEP arg
    """
    p[0] = p[1] + ['', p[4]]


def p_arg_empty(p):
    """
    arg :
    """
    p[0] = ''


def p_arg_int(p):
    """
    arg : INT
    """
    p[0] = int(p[1])


def p_arg_float(p):
    """
    arg : FLOAT
    """
    p[0] = float(p[1])


def p_arg_other(p):
    """
    arg : STR
        | funccall
    """
    p[0] = p[1]


def p_error(p):
    print('Unexpected token:', p)


parser = yacc.yacc()
