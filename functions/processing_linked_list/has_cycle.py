def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    a, x = {}, 0
    while link.rest is not Link.empty:
        for n in a:
            if a[n] is link:
                return True
        a[x], x = link, x+1
        link = link.rest
    return False
    # Official answer:
    seen = []
    while link.rest is not Link.empty:
        if link in seen:
            return True
        seen.append(link)             # The key is to track the link object rather than link.first value.
        link = link.rest
    return False
"""
These two solutions are both linear space. The solution below only has a constant space.
"""
def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    origin, k = link, 0                       # origin is the putin link.
    while link.rest is not Link.empty:
        test_link, test = origin, k           # in order to not affect origin and k when we test, we give origin and k values to test_link and test.
        while test > 0:
            if test_link is link:             # if we find link in the orgin, if proves that there's a cycle.
                return True
            test_link = test_link.rest
            test -= 1
        link, k = link.rest, k+1              # k is used to record how many times we use the attribute .rest
    return False
    # Official answer:
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False
    slow, fast = link, link.rest     # fast pointer is one-move more than slow pointer.
    while fast != Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:    # if there's a cycle, then if we keep move fast and slow pointer, the fast pointer will chase up the slow pointer.
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest  # everytime we move slow and fast pointer, slow pointer moves one move, fast pointer moves two moves.
    return False
