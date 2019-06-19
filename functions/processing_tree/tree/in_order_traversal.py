def in_order_traversal(t):
    """
    Generator function that generates an "in-order" traversal, in which we
    yield the value of every node in order from left to right, assuming that each node has either 0 or 2 branches.

    For example, take the following tree t:
            1
        2       3
    4     5
         6  7

    We have the in-order-traversal 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        yield t.label
    else:                                                # The generate order is from left branch to label to right branch.
        for node in in_order_traversal(t.branches[0]):
            yield node
        yield t.label
        for node in in_order_traversal(t.branches[1]):
            yield node
