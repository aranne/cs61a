count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
        """ we should know that:
        >>> sum([2, 4], 2)
        8  (6+2)
        >>> sum( [[2,3],[3,4]], [] )
        [2, 3, 3, 4]
        >>> sum( [[3, 2], [[1]]], [] )
        [3, 2, [1]]
        This means sum([...], [])just get rid of one level of list. example: from [2, 3, 5] to 2+3+5, from [[2,3], [4]] to [2, 3, 4], from [[2,3], [[3]]] to [2, 3, [3]]
        """
                
