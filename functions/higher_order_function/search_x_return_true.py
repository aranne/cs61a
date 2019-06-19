def search(f):
    """ search x that makes the f(x) function is True."""
    x = 0
    """while True:
        if f(x):
            return x
        x += 1"""
    while not f(x):
        x += 1
    return x 

def square(x):
    return x * x

def positive(x):
    """
    >>> search(positive)
    11
    """
    return max(0, square(x) - 100)

def inverse(f):
    """return g(y) such that g(f(x)) -> x.
    >>> sqrt = inverse(square)
    >>> sqrt(256)
    16
    """
    return lambda y: search(lambda x: f(x) == y) #g(y) means if we get a y, we need to
                                                 #find out the x which makes f(x) == y
    #in search function, when f(x) == y is True, the while loop will break, and then return the x value.
