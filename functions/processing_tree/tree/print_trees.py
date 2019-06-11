def print_tree(tree):
    """
    >>> print_tree(fib_tree(4))
    3
    1
    0
    1
    2
    1
    1
    0
    1
    This tree doesn't have a structure of the fibonacci tree.
    """
    print label(tree)
    for b in branches(tree):
        print_tree(b)

"""
we will now use indentation in order to show the structure of a tree.
>>> print(' ' * 5 + str(5))
     5
"""
def print_tree(tree, indent=0):
    """
    print the structure of a tree.
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  '*indent + str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent+1)
