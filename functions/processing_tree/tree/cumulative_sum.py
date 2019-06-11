def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():               # if t is a leaf, then nothing happens.
        for b in t.branches:
            cumulative_sum(b)         # Remember: cumulative_sum is just a function that has an effect on t, returning nothing.
        t.label = t.label + sum([b.label for b in t.branches])
