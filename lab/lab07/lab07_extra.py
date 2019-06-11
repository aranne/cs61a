""" Optional Questions for Lab 07 """

from lab07 import *

# Q9
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    """
    if link is not Link.empty:
        if link.rest is not Link.empty:
            while link.first == value:
                link.first = link.second
                link.rest = link.rest.rest
            remove_all(link.rest, value)
        else:
            if link.first == value:
                # Here we will encounter an problem: if the list.first of the last linked list == value, we cannot get rid of the last linked list.
                # We cannot change the link.rest of last link to be Link.empty.
                # So we need to detect the link.first of the next link whether is value or not.
    """
    "*** YOUR CODE HERE ***"
    # Official answer:
    if link.rest is not Link.empty:
        if link.rest.first == value:    # if the last
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)

# Q10
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link is not Link.empty:
        if isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
        else:
            link.first = fn(link.first)
        deep_map_mut(fn, link.rest)

# Q11
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    a, x = {}, 0
    while link.rest is not Link.empty:
        for n in a:
            if a[n] is link:
                return True
        a[x], x = link, x+1
        link = link.rest
    return False
    # Official answer:
    seen = []
    while link.rest is not Link.empty:
        if link in seen:
            return True
        seen.append(link)             # The key is to track the link object rather than link.first value.
        link = link.rest
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    origin, k = link, 0
    while link.rest is not Link.empty:
        test_link, test = origin, k
        while test > 0:
            if test_link is link:
                return True
            test_link = test_link.rest
            test -= 1
        link, k = link.rest, k+1
    return False
    # Official answer:
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False
    slow, fast = link, link.rest     # fast pointer is one-move more than slow pointer.
    while fast != Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:    # if there's a cycle, then if we keep move fast and slow pointer, the fast pointer will chase up the slow pointer.
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest  # everytime we move slow and fast pointer, slow pointer moves one move, fast pointer moves two moves.
    return False

# Q12
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
