import re

import ply.lex as lex


tokens = ("INT", "FLOAT", "IDENTIFIER", "OPENBKT", "CLOSEBKT",
          "ARGSEP", "DFLTTEXT", "DFLTFUNC", "STR")


t_INT = r"[0-9]+"
t_FLOAT = r"[0-9]+\.[0-9]+"
t_IDENTIFIER = r"[_A-Za-z][a-zA-Z0-9_]*"

t_OPENBKT = r"\("
t_CLOSEBKT = r"\)"
t_ARGSEP = r','
t_DFLTTEXT = r":-"
t_DFLTFUNC = r":\+"

t_ignore = ' \r\n\t\f'

OPENSTRBKTs = ("'", '"', '`', r'\{', r'\[', '<', '/')
CLOSESTRBKTs = ("'", '"', '`', r'\}', r'\]', '>', '/')
TEMPLATE = "({}.*?{})"


@lex.TOKEN('|'.join(TEMPLATE.format(*brackets) for brackets in zip(OPENSTRBKTs, CLOSESTRBKTs)))
def t_STR(t):
    # Убираем символы строкового литерала
    t.value = t.value[1:-1]
    return t


class ParserError(Exception):
    pass


def t_error(t):
    raise(ParserError(f"Illegal sequence '{t.value}' at {t.lineno}: {t.lexpos}"))


lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)
