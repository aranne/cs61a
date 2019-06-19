def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link is not Link.empty:
        if link.rest is not Link.empty:
            while link.first == value:
                link.first = link.second
                link.rest = link.rest.rest
            remove_all(link.rest, value)
        else:
            if link.first == value:
                # Here we will encounter an problem: if the list.first of the last linked list == value, we cannot get rid of the last linked list.
                # We cannot change the link.rest of last link to be Link.empty.
                # So we need to detect the link.first of the next link whether is value or not.
    "*** YOUR CODE HERE ***"
    # Official answer:
    if link.rest is not Link.empty:
        if link.rest.first == value:    # if the last
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)
