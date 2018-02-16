trim = str.strip
trimt = str.rstrip
triml = str.lstrip
uc = str.upper
lc = str.lower


def nws(s):
    return ' '.join(str.split(s))


def part(text, size, n):
    start, end = n*size, (n+1)*size
    if len(text) < end:
        raise IndexError
    return text[start:end]


def f(format, *args):
    return format % args


def sed(text, expr):
    pass


def tr(text, set1, set2):
    pass
