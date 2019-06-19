def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    "*** YOUR CODE HERE ***"
    if not n // 10:
        return Link(n)
    t, k = n, 0
    while t // 10:
        t, k = t // 10, k + 1
    return Link(t, store_digits(n-t*10**k))

    # official answer:
    "*** YOUR CODE HERE ***"
    so_far = Link.empty
    while n > 0:
        last, n = n % 10, n // 10
        so_far = Link(last, so_far)
    return so_far
