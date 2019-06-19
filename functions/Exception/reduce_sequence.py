from operator import add, mul, truediv

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial. The returned value of the first element will be the initial value of the second element.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial

def divide_all(n, ds):
    """Divide numrator by every denominator in ds.

    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
