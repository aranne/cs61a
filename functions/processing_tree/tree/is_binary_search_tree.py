def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return True
    if len(t.branches) > 2:
        return False
    elif len(t.branches) == 1:
        return is_bst(t.branches[0])
    elif max_tree(t.branches[0]) > t.label or min_tree(t.branches[1]) < t.label:
        return False
    else:
        return is_bst(t.branches[0]) and is_bst(t.branches[1])

def min_tree(t):
    """ Returns a minimum value of a tree."""
    if t.is_leaf():
        return t.label
    return min([t.label] + [min_tree(b) for b in t.branches])   # using min([a] + [b for b in sequence]) to get the minimum value.

def max_tree(t):
    """ Returns a maximum value of a tree."""
    if t.is_leaf():
        return t.label
    return max([t.label] + [max_tree(b) for b in t.branches])            
