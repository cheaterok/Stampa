def join(s, *args):
    return s.join(args)


def enclose(l, text, t):
    return "".join((l, text, t))


def ejoin(l, s, t, *args):
    return enclose(l, join(s, *args), t)


def coalesce(*args):
    return next(arg for arg in args if arg is not None)
