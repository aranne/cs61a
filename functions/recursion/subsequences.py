def insert_into_all(item, nested_list):
    """Assuming that nested_list is a list of lists, return a new list
    consisting of all the lists in nested_list, but with item added to
    the front of each.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    return  [[item] + lst for lst in nested_list]

def subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists). The subsequences can appear in any order.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    "*** YOUR CODE HERE ***"
    if s == []:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return insert_into_all(s[0], subset) + subset

"""
Now we only want the subsequences which are nondecreasing.
"""
def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    "*** YOUR CODE HERE ***"
    if not s:
        return [[]]
    a = [x for x in inc_subseqs(s[1:]) if x == [] or s[0] <= x[0]]       # in the inc_subseqs(s[1:]) there's a [], so we need to consider x == [].
    return insert_into_all(s[0], a) + inc_subseqs(s[1:])# Only the list x in inc_subseqs(s[1:]) satisfy that s[0] < x[0] can we insert s[0] to all the x in inc_subseqs[1:].
    # official answer:
    "*** YOUR CODE HERE ***"
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)  # continue to Find in s[1:] in order to get s[0] >= prev
        else:
            a = subseq_helper(s[1:], s[0])    # with s[0]: decide to add s[0], then loop up in s[1:] to find lists whose first element >= s[0].
            b = subseq_helper(s[1:], prev)    # without s[0]: turn to look up in s[1:] to find lists whose first element >= prev.
            return insert_into_all(s[0], a) + b   # Everytime we insert a s[0], we have to guarantee that a[0] of a is greater than s[0].
    return subseq_helper(s, 0)
