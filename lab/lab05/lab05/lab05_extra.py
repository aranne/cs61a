""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev].append(word)
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result = result + ' ' + word
        word = random.choice(table[word])              # To random choice a word from a list in the table.
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines.
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)  # This will start with a random word which is a successor of '.' in the table

# Q6
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in vals])
    return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])

# Q7
def add_trees(t1, t2):
    """
    >>> numbers = tree(1, [tree(2,[tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1) + label(t2))
    elif is_leaf(t1):
        return tree(label(t1) + label(t2), branches(t2))
    elif is_leaf(t2):
        return tree(label(t1) + label(t2), branches(t1))
    else:
        b = []         # b is used to store the mutual branch of branches(tree1) and branches(tree2).
        b_left = []    # b_left is used to store surplus branches of tree1 or tree2. eg: if tree1 has 3 branches, tree2 has five branches. Then b_left is used to store the surplus two branches of tree2.
        len1, len2 = len(branches(t1)), len(branches(t2))
        if len1 < len2:
            b_left = branches(t2)[(len2-len1):]
        if len1 > len2:
            b_left = branches(t1)[(len1-len2):]
        branches_tuples = zip(branches(t1), branches(t2)) # Put the mutual branch of two branches together into a tuple iterator.
        for branch_tuple in list(branches_tuples):  # Using list(iterator) to get all the tuples in a list. and branch_tuple means a tuple of corresponding branch of tree1 and tree2.
            branch1, branch2 = branch_tuple   # branch1 and branch2 is correspond to two elements in the tuple respectively.
            branch = add_trees(branch1, branch2)  # add two corresponding branch together.
            b.append(branch)                    # Store the new branch into b.
        return tree(label(t1) + label(t2), b + b_left)  # the new branches are b + b_left.

    # Official answer:
    "*** YOUR CODE HERE ***"
    b1, b2 = branches(t1), branches(t2)
    if len(b1) > len(b2):
        b2 += [tree(0)] * (len(b1) - len(b2))  # pad the shorter tree's branches with tree(0), after pad the shorter tree, these two trees have exactly same number of branch.
    if len(b2) > len(b1):
        b1 += [tree(0)] * (len(b2) - len(b1))
    return tree(label(t1)+label(t2), [add_trees(b[0], b[1]) for b in zip(b1, b2)])



# Tree ADT
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

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
