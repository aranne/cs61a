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

#################################
######## Using Tree Class #######
#################################
def leaves(t):
    """
    Put all the leaves in a tree into a list.
    """
    if t.is_leaf():
        return [t.label]
    return sum([leaves(b) for b in t.branches], [])

def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None.
    >>> sum_labels(fib_tree(4))
    10
    """
    return t.label + sum([sum_labels(b) for b in t.branches])

def fib_tree(n):
    """
    Returns a Tree that has the nth Fibonacci number as its label and a trace of all previously computed Fibonacci numbers within its branches.
    >>> fib_tree(4)
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, [left, right])
"""
We can also use memo() to remember the computed fib number.
"""
def memo(f):
        cache = {}
        def memorized(n):
            if n not in cache:
                cache[n] = f(n)
            return cache[n]
        return memorized
"""
>>> fib_tree = memo(fib_tree)
>>> big_fib_tree = fib_tree(35)      # If we don't use memo(), fib_tree(35) will be computed for a long time.
>>> big_fib_tree.label
9227465
>>> big_fib_tree.branches[0] is big_fib_tree.branches[1].branches[1]
True
>>> sum_labels = memo(sum_labels)
>>> sum_labels(big_fib_tree)
237387960
"""
def prune_repeats(t, seen=[]):
    """prune all the repeats node in a tree."""
    seen.append(t)
    t.branches = [b for b in t.branches if b not in seen]  # Skip branch which we has already known.
    for b in t.branches:
        prune_repeats(b, seen)
"""
>>> fib_tree = memo(fib_tree)
>>> big_fib_tree = fib_tree(35)
>>> prune_repeats(big_fib_tree)
>>> big_fib_tree
Tree(21, [Tree(8, [Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2)]), Tree(5)]), Tree(13)])
>>> print(big_fib_tree)
21
 8
  3
   1
    0
    1
   2
  5
 13
"""
