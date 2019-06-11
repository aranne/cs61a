def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():            # if t is a leaf, then do nothing.
        a = []
        for b in t.branches:
            a.append(b.label)     # Using a to store the label of the nodes.
        for b in t.branches:
            b.label = a.pop()     # reassign every node in a reversed order. Attention: a.pop() has a reverse effect.
        for b in t.branches:
            if not b.is_leaf():
                for next_b in b.branches:  # to reverse the other level tree.
                    reverse_other(next_b)
    # Official answer:
    "*** YOUR CODE HERE ***"
    def reverse_odd(tree, odd=True):
        if tree.is_leaf():
            return
        else:
            branch_labels_reversed = [b.label for b in tree.branches][::-1]    # a[::-1] means get a new reversed list.
            for branch, label_reversed in zip(tree.branches, branch_labels_reversed):   # get the branch and the corresponding reversed label.
                if odd:
                    branch.label = label_reversed
                reverse_odd(branch, not odd)
    return reverse_odd(t)
