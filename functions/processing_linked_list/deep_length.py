def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    "*** YOUR CODE HERE ***"
    if lnk.rest is Link.empty:             # The base case
        if isinstance(lnk.first, Link):
            return deep_len(lnk.first)
        return 1
    elif isinstance(lnk.first, Link):
        return deep_len(lnk.first) + deep_len(lnk.rest)
    else:
        return 1 + deep_len(lnk.rest)
    # official answer:
    "*** YOUR CODE HERE ***"
    if lnk is Link.empty:
        return 0
    elif not isinstance(lnk, Link):
        return 1
    else:
        return deep_len(lnk.first) + deep_len(lnk.rest)
