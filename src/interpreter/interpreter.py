from .parser import parser


def evaluate(code):
    return str(parser.parse(code))
