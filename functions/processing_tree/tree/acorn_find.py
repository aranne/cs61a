def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    if label(t) == 'acorn':
        return True
    else:
        for b in branches(t):
            if acorn_finder(b):
                return True
    return False
