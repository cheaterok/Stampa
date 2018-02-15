from itertools import zip_longest


def if_(s, ifeq, ifne):
    return ifeq if s else ifne


def ncase0(s, dv, *vs):
    try:
        return vs[s]
    except IndexError:
        return dv


def ncase1(s, dv, *vs):
    if 1 <= s <= len(vs):
        return vs[s-1]
    else:
        return dv


def _pairwise(iterable, fillvalue=None):
    args = [iter(iterable)] * 2
    return zip_longest(fillvalue=fillvalue, *args)


def rcase(s, *args):
    args = list(args)
    dv = args.pop()
    pairs = list(_pairwise(args))
    for pair in pairs:
        if s < pair[1]:
            return pair[0]
    else:
        return dv


def lcase(s, *args):
    args = list(args)
    dv = args.pop()
    pairs = list(_pairwise(args))
    for pair in pairs:
        if s <= pair[1]:
            return pair[0]
    else:
        return dv


def tcase(s, *args):
    args = list(args)
    dv = args.pop() if len(args) % 2 != 0 else ''
    pairs = dict(_pairwise(args))
    return pairs.get(s, dv)



