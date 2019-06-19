"""
Define a function make_counter that returns a counter function, which takes a string and returns the number of times that the function has been called on that string.
"""
def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    a = []
    def counter(s):
        a.append(s)
        return a.count(s)
    return counter
