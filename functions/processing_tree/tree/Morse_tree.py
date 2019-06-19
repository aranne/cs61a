# Morse tree
# Morse code is a signaling protocol that transmits messages by sequences of signals.

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
    """Return a tree representing the code. Each internal (non-leaf) node
    of the tree other than its root is a signal. Each leaf node
    is a letter encoded by the path from the root.

    >>> pretty(morse(abcde))
       None
     /    \
     .    -
    / \   |
    - e   .
    |    /  \
    a    .  -
        / \ |
        . d .
        |   |
        b   c
    """
    whole = Tree(None)
    for letter, signals in sorted(code.items()):          # Build a pair of (letter, signals)
        t = whole
        for s in signals:
            if s in [b.label for b in t.branches]:        # if t has already had the signal s, we move the tree t pointer to the first branch that has the signal s.
                t = [b for b in t.branches if b.label == s][0]
            else:                                         # if t doesn't has the s branch, we create a new branch append to the tree t.
                b = Tree(s)                               # And move the tree t pointer to the new branch.
                t.branches.append(b)
                t = b
        t.branches.append(Tree(letter))  # After go through all signal in signals, tree t pointer is pointed to the branch corresponding to the last signal in signals.
    return whole                         # Then append the letter to the tree t pointer. The letter is a leaf.

def decode(signals, tree):
    """Decode signals into a letter according to tree, assuming signals
    correctly represents a letter.  tree has the format returned by
    morse().

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.label == signal][0]      # Go through the tree until the last signal.
    leaves = [b for b in tree.branches if b.is_leaf()]   # get all leaves under the tree corresponding to the last signal.
    assert len(leaves) == 1
    return leaves[0].label                              # the tree has only one leaf corresponding to the letter.

class Tree:
    """A tree with label as its label value."""
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

def height(tree):
    """The height of a tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])
def width(tree):
    """Returns the printed width of this tree."""
    label_width = len(str(tree.label))
    w = max(label_width,
            sum([width(t) for t in tree.branches]) + len(tree.branches) - 1)
    extra = (w - label_width) % 2
    return w + extra
def pretty(tree):
    """Print a tree laid out horizontally rather than vertically."""

    def gen_levels(tr):
        w = width(tr)
        label = str(tr.label)
        label_pad = " " * ((w - len(label)) // 2)
        yield w
        print(label_pad, file=out, end="")
        print(label, file=out, end="")
        print(label_pad, file=out, end="")
        yield

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

out = StringIO()
h = height(tree)
g = gen_levels(tree)
next(g)
for i in range(2*h + 1):
    next(g)
    print(file=out)
print(out.getvalue(), end="")
