############################################
##### Sets as Unordered sequences ##########
############################################
"""
if we use Unordered sets to implement some sets_manipulata functions:
"""
def empty(s):
    """ Determine whether s is an empty set."""
    return s is Link.empty

def set_contains(s, elem):
        """Return True if and only if set s contains an element elem.
        This is a linear-time funtion, which requires Θ(n) time to test membership of an element.

        >>> s = Link(4, Link(1, Link(5)))
        >>> set_contains(s, 2)
        False
        >>> set_contains(s, 5)
        True
        """
        if empty(s):
            return False
        elif s.first == elem:
            return True
        else:
            return set_contains(s.rest, elem)

def adjoin_set(s, elem):
        """Return a set containing all elements of s and element elem.
        Using set_contains linear-time funtion to test membership, so this function is also a linear-time function.

        >>> t = adjoin_set(s, 2)
        >>> t
        Link(2, Link(4, Link(1, Link(5))))
        """
        if set_contains(s, elem):
            return s
        else:
            return Link(elem, s)

def intersect_set(set1, set2):
        """Return a set containing all elements common to set1 and set2.
        Intersecting two sets set1 and set2 also requires membership testing, but this time each element of set1 must be tested for membership in set2.
        So intersect_set funtion is a quadratic-time function, which has a Θ(n^2) order of growth.

        >>> intersect_set(t, apply_to_all_link(s, square))
        Link(4, Link(1))
        """
        return keep_if_link(set1, lambda v: set_contains(set2, v))

def union_set(set1, set2):
        """Return a set containing all elements either in set1 or set2.
        The union_set function also requires a linear number of membership tests, creating a process that also includes Θ(n^2) steps.

        >>> union_set(t, s)
        Link(2, Link(4, Link(1, Link(5))))
        """
        set1_not_set2 = keep_if_link(set1, lambda v: not set_contains(set2, v))
        return extend_link(set1_not_set2, set2)

#########################################
###### Sets as ordered sequences ########
#########################################
"""
if we use ordered sequences to build Set, listing its elements in increasing order.
"""
"""
One advantage of ordering shows up in set_contains:
In checking for the presence of an object, we no longer have to scan the entire set.
If we reach a set element that is larger than the item we are looking for, then we know that the item is not in the set:
"""
def set_contains(s, v):
    """
    In the worst case, we still need to search whole set to compare, in the best case, we don't even to search once.
    So the average steps we need is about n/2.
    This is still Θ(n) order of growth.

    >>> u = Link(1, Link(4, Link(5)))
    >>> set_contains(u, 0)
    False
    >>> set_contains(u, 4)
    True
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def adjoin(s, v):
    """ Create a new set that adjoin value v into an ordered set s.

    >>> set1 = Link(1, Link(4, Link(5)))
    >>> set2 = adjoin(set1, 3)
    >>> set2
    Link(1, Link(3, Link(4, Link(5))))

    """
    if s.first > v:
        return Link(v, s)
    elif s.first == v:
        return s
    elif empty(s):
        return Link(v)
    return Link(s.first, adjoin(s.rest, v))

def union(set1, set2):
    """ Create a new set that is a union of set1 and set2.

    >>> set1 = Link(1, Link(4, Link(6)))
    >>> set2 = Link(2, Link(4, Link(5)))
    >>> set3 = union(set1, set2)
    >>> set3
    Link(4)
    """
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 > e2:
            return Link(e1, union(set1.rest, set2))
        elif e2 > e1:
            return Link(e2, union(set2.rest, set1))

def intersect_set(set1, set2):
    """
    We iterate through both sets simultaneously, tracking an element e1 in set1 and e2 in set2. When e1 and e2 are equal, we include that element in the intersection.
    if e1 < e2, we can discard e1, because e1 is definitely not in set2.

    >>> intersect_set(s, s.rest)
    Link(4, Link(5))
    """
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set(set1.rest, set2)
        elif e2 < e1:
            return intersect_set(set1, set2.rest)
"""
To estimate the number of steps required by this process, observe that in each step we shrink the size of at least one of the sets.
Thus, the number of steps required is at most the sum of the sizes of set1 and set2, rather than the product of the sizes, as with the unordered representation.
So this is Θ(n) order of growth.
"""

def add(s, v):
    """ Add a value to an ordered set, which doesn't create a new set, just change s.

    >>> set1 = Link(2, Link(5, Link(6)))
    >>> add(set1, 4)
    >>> set1
    Link(2, Link(4, Link(5, Link(6))))
    """
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first == v:
        return s
    elif empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


#################################################
######### Construct binary tree #################
#################################################
"""
Binary tree is a new class:
Class Binary_tree:
    def __init___(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
If we build sets in a binary tree, the entry of the root of the tree holds one element of the set.
The entries within the left branch include all elements smaller than the one at the root.
Entries in the right branch include all elements greater than the one at the root.
Now we use this search binary tree to modify our functions:
"""
class Tree:
    """
    >>> a = Tree(3,[Tree(4),Tree(5)])
    >>> a
    Tree(3, [Tree(4), Tree(5)])
    >>> print(a)
    3
     4
     5
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))
    def is_leaf(self):
        return not self.branches
    def __str__(self):
        return '\n'.join(self.indented())
    def indented(self, k=0):
        indent = []
        for b in self.branches:
            for line in b.indented(k+1):
                indent.append(' ' + line)
        return [str(self.label)] + indent

class BTree(Tree):
    """
    Idea 1: Filling the place of missing left or right branch with an empty tree.
    Idea 2: A BTree always has two branches, which means a leaf will has two empty tree.
    """
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({})'.format(self.label)
        elif self.right is BTree.empty:
            return 'BTree({0}, {1})'.format(self.label, repr(self.left))
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'                 # We only show the BTree.empty when self.left is BTree.empty. However, usually in a balanced binary tree, ->
            return 'BTree({0}, {1}, {2})'.format(self.label, left, right)                                         # -> the left part always has a value, not BTree.empty.

# Using BTree:
def fib_tree(n):
    """
    Returns a Tree that has the nth Fibonacci number as its label and a trace of all previously computed Fibonacci numbers within its branches.
    >>> fib_tree(4)
    BTree(3, BTree(1, BTree(0), BTree(1)), BTree(2, BTree(1), BTree(1, BTree(0), BTree(1))))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return BTree(left.label + right.label, left, right)

def contents(t):
    """ Gives a list of all labels of a binary tree.

    >>> t = BTree(3, BTree(1, BTree(0), BTree(1)), BTree(2, BTree(1), BTree(1, BTree(0), BTree(1))))
    >>> contents(t)
    [0, 1, 1, 3, 1, 2, 0, 1, 1]
    """
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)      # Choose the order we put them into a list.

def balanced_bst(s):
    """ Construct a balanced binary search tree from a sorted list."""
    if not s:                    # The base case is s == []
        return BTree.empty
    mid = len(s) // 2            # If s has two value, we put the second one in the middle, leave the first one on the left.
    left = balanced_bst(s[:mid])
    right = balanced_bst(s[mid+1:])
    return BTree(s[mid], left, right)

def largest(bst):
    """ Returns the largest value in a binary search tree."""
    if bst.right is BTree.empty:
        return bst.label
    else:
        return largest(bst.right)

def second_largest(bst):
    """ Returns the second largest value in a binary search tree."""
    if bst.is_leaf():
        return None
    elif bst.right is BTree.empty:  # if bst doesn't have a right branch, we should find the largest value in the left part.
        return largest(bst.left)
    elif bst.right.is_leaf():
        return bst.label
    else:
        return second_largest(bst.right)


###############################################
######### Sets as binary tree #################
###############################################
def set_contains(s, v):
    """ The order of growth is  Θ(log(n)). """
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return set_contains(s.right, v)
    elif s.label > v:
        return set_contains(s.left, v)

def adjoin_set(s, v):
    """
    Adjoin the v value to a ordered set in a balanced binary tree. s will not change, but return a new set in binary tree.

    This is also Θ(logn) order of growth.
    >>> odds = [1, 3, 5, 7, 9]
    >>> bst = balanced_bst(odds)
    >>> bst
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7)))
    >>> adjoin_set(bst, 4)
    BTree(5, BTree(3, BTree(1), BTree(4)), BTree(9, BTree(7)))
    >>> bst
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7)))
    """
    if s is BTree.empty:      # If s is empty, which means v is not in the set, so we add a new branch to a leaf node.
        return BTree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin_set(s.right, v))
    elif s.label > v:
        return BTree(s.label, adjoin_set(s.left, v), s.right)

"""
If we adjoin values in an ordered set to a balanced search tree, we will make the tree unbalanced.
However if we adjoin the set in some arbitrary order, we will get a new balanced search tree.
So the key is that we must keep the balance search tree balanced when we adjoin values.  
"""




# Linked List Class:
class Link:
        """A linked list with a first element and the rest.
        >>> s = Link.empty
        >>> s
        ()
        >>> s = Link(3, Link(4, Link(5)))
        >>> len(s)
        3
        >>> s[1]
        4
        >>> s
        Link(3, Link(4, Link(5)))
        >>> s_first = Link(s, Link(6))
        >>> s_first
        Link(Link(3, Link(4, Link(5))), Link(6))
        >>> len(s_first)
        2
        >>> len(s_first[0])
        3
        >>> s + s
        Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
        >>> square = lambda x: x*x
        >>> map_link(square, s)
        Link(9, Link(16, Link(25)))
        >>> odd = lambda x: x % 2 == 1
        >>> map_link(square, filter_link(odd, s))
        Link(9, Link(25))
        >>> join_link(s, ", ")
        '3, 4, 5'
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
        empty = ()
        def __init__(self, first, rest=()):        # the default value of the rest of last linked list is (), which can also be Link.empty
            assert rest is Link.empty or isinstance(rest, Link)  # Using isinstance allow we pass in s, whose rest is a subclass of Link.
            self.first = first
            self.rest = rest
        def __getitem__(self, i):      # This is a recursive way to get index i item.
            if i == 0:             # The base case.
                return self.first
            else:
                return self.rest[i-1]
        def __len__(self):            # The base case is: len(empty) -> len(()) -> 0
            return 1 + len(self.rest)

        def __repr__(self):
            if self.rest is Link.empty:    # base case: the last linked list. Attention: self is not Link.empty now!
                return 'Link({})'.format(repr(self.first))
            return 'Link({0}, {1})'.format(repr(self.first), repr(self.rest))    # This is a recursive call of __repr__ method.
