def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) and label(t) in vals:
        return None
    if is_leaf(t):
        return t
    return tree(label(t), [prune_leaves(b, vals) for b in branches(t) if not (is_leaf(b) and label(b) in vals)]) # To get rid of leaves if label(b) in vals.

    # official answer:
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) in vals:
            return None
        else:
            return t
    pruned = [prune_leaves(b, vals) for b in branches(t)]
    return tree(label(t), [b for b in pruned if b is not None])   # Usinf None to decide whether it is a wanted leaf. and then to get rid of None value.
