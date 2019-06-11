def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    The path is represented as a linked list of node values that starts from root and ends at leaf.
    The length of a path is the number of edges in the path (i.e. one less than the number of nodes in the path).
    Paths are listed in order from left to right.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    "*** YOUR CODE HERE ***"
    if tree.is_leaf():
        if n <= 0:                     # if n <= 0, which means the longth of paths is greater than n, because everytime you add a node, n = n-1
            return [Link(tree.label)]
        return []                      # if n > 0, return a [].
    else:
        paths = []
        for b in tree.branches:
            paths += long_paths(b, n-1)
        return [Link(tree.label, path) for path in paths]  # if paths is [], then this will return []
    #Official answer:
    "*** YOUR CODE HERE ***"   # the answer is much conciser than mine.
    paths = []
    if n <= 0 and tree.is_leaf():
        paths.append(Link(tree.label))
    for b in tree.branches:
        for path in long_paths(b, n-1):
            paths.append(Link(tree.label, path))
    return paths    # if no condition satisfied, return [].
