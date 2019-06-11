def evens(start, end):
    """A generator function that returns even numbers between start and end.

    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    >>> t = evens(2, 10)
    >>> next(t)
    2
    >>> next(t)
    4
    """
    even = start + (start % 2)  # This expressing doesn't need to decide whether start is even or odd. (start % 2) is either 1 or 0.
    while even < end:
        yield even
        even += 2
