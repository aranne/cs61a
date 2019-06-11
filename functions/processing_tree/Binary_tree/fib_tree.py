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
        
