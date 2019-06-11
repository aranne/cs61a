# Define a generator function generate_paths which takes in a tree t, a value x,and yields each path from the root of t to a node that has label x.
# Each path should be represented as a list of the labels along that path in the tree.

# Offical answer:
"""
First we don't need to generate paths all, we just need to find one of them.
"""
def a_path(t, x):
    """ Return a path from the root of t to that ends with x.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> a_path(t1, 1)
    [1]
    >>> a_path(t1, 4)
    [1, 2, 4]
    >>> a_path(t1, 5)
    [1, 2, 5]
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        rest_of_path = a_path(b, x)
        if rest_of_path:                      # if this branch has a rest of the path, then return the whole path.
            return [label(t)] + rest_of_path
"""
Now we need to yield all the paths.
"""
def generate_paths(t, x):
    """Yields all possible paths from the root of t to a node with the label x
    as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** YOUR CODE HERE ***"
    path = []              # everytime the recursive funtion is called, clear path value.
    path.append(label(t))
    if label(t) == x:
        yield path          # this recusive function have a special base case: if t is a leaf, and label(t) != x, then yield nothing
    for b in branches(t):
        for p in generate_paths(b, x):   # generate_paths is a generator. connect current label(t) (path) to the paths from branches below (p)
            yield path + p




# Tree ADT:
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
