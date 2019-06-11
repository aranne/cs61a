# Define the function add_trees, which takes in two trees and returns a new tree where each corresponding node from the first tree is added with the node from the second tree.
# If a node at any particular position is present in one tree but not the other, it should be present in the new tree as well.
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
    
