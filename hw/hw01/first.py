from operator import floordiv, mod
def divide(n, d):
    """Return the quotient and remainder of dividing N by d.

    >>> q, r = divide(2013, 10)
    >>> q
    201
    >>> r
    2
    """
    return floordiv(n, d), mod(n, d)
