def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.
    n: The number of partitions of a positive integer
    m: is the larest parts of the integer
    n can be expressed as the sum of positive integer parts in increasing order.
    This problem is called count partitions, which will be much easier if we use tree recursion.
    2 + 4 = 6

    1 + 1 + 4 = 6

    3 + 3 = 6

    1 + 2 + 3 = 6

    1 + 1 + 1 + 3 = 6

    2 + 2 + 2 = 6

    1 + 1 + 2 + 2 = 6

    1 + 1 + 1 + 1 + 2 = 6

    1 + 1 + 1 + 1 + 1 + 1 = 6

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    # The base case is important to understand
    if n == 0:
        # if we need to calculate (2,2), we split it into (0,2) and (2,1)
        return 1
    elif n < 0:  # (0,2) has one solution, that is 0 + 2 = 2
        # then we split (2,1) into (1,1) and (2,0), in which (2,0) has no solution
        return 0
    elif m == 0:  # (1,1) split into (0,1) and (1,0), in which (1,0) has no solution
        return 0  # (0,1) has one solution, that is 0 + 1 = 1
    else:  # Above all, (2,2) has two positive solutions, (0,2) and (0,1)

        with_m = count_partitions(n-m, m)  # There're two positve partitions,
        # One is that the partitions have m, the other one is not.
        without_m = count_partitions(n, m-1)
        return with_m + without_m

##############################
# Trees can also be used to represent the partitions of an integer.
# A partition tree for n using parts up to size m is a binary (two branch) tree
# that represents the choices taken during computation


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m.
    The labels at the leaves of a partition tree express whether the path
    from the root of the tree to the leaf represents a successful partition of n.
    >>> partition_tree(2, 2)
    [2, [True], [1, [1, [True], [False]], [False]]]
    """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        # No matter how left changes, the m in it doesn't change.
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])         # Mark down m in left


def print_parts(tree, partition=[]):
    """Print the partitions.
    >>> print_parts(partition_tree(6, 4))
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if is_leaf(tree):
        # Only the left part can return the True value.
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        # Accumulate m using partition when it is the left part
        print_parts(left, partition + [m])
        print_parts(right, partition)


#############################
# Linked lists are particularly useful when constructing sequences incrementally
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        # Only using_m can return [empty, empty]
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        # No matter how the partitions(n-m, m) changes, the m in using_m does'n change. So mark down that m
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)


def print_partitions(n, m):
    """Print the partitions.
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    # Join the lists in every first element
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    # Join all the first elements together.
    print(join_link(strings, "\n"))
