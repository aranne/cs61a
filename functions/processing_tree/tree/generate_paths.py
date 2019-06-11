# Define a generator function generate_paths which takes in a tree t, a value x,and yields each path from the root of t to a node that has label x.
# Each path should be represented as a list of the labels along that path in the tree.
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

# Solution two:
# Do not use generator
# This solution to create path from top down to the leaf, and use path.pop() to go back up to the last node.
path = []
c = 0
s = []
def generate_paths(t, x):
    path.append(label(t))
    if label(t) == x:
        n = path[:]     # Using n = path[:] to create a new list binding to n, otherwise s.append(path) will cause the value in s are mutable data --- path.
        s.append(n)     # To store all the paths in s.
    for b in branches(t):
        generate_paths(b, x)
        c = path.pop()   # everytime we call recursive generate_paths, we should clear the last value in path after we return from generate_paths
