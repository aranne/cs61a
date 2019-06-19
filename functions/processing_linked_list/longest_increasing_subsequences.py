"""
This function takes in a list lst and returns the longest subsequence in which all the terms are increasing.
Note: the elements do not have to appear consecutively in the original list.
"""
def longest_increasing_subsequences(lst):
    """
    Returns the longest increasing subsequence of the list.

    >>> longest_increasing_subsequences(Link.empty)
    ()
    >>> longest_increasing_subsequences(Link(1))
    Link(1)
    >>> longest_increasing_subsequences(Link(1, Link(9, Link(2, Link(3)))))
    Link(1, Link(2, Link(3)))
    >>> longest_increasing_subsequences(Link(1, Link(9, Link(8, Link(4, Link(3, Link(2, Link(3))))))))
    Link(1, Link(2, Link(3)))
    >>> longest_increasing_subsequences(Link(1, Link(2, Link(3, Link(4, Link(9, Link(3, Link(4, Link(1, Link(10, Link(5)))))))))))
    Link(1, Link(2, Link(3, Link(4, Link(9, Link(10))))))
    """
    def larger_than_first(lst):
        """returns a list(doesn't contain the first element of list) with each element is larger than the first element in the list."""
        return filter_link((lambda x: lst.first < x), lst.rest)
    if lst is Link.empty:
        return Link.empty
    else:
        with_first = Link(lst.first, longest_increasing_subsequences(larger_than_first(lst)))   # with the first element
        without_first = longest_increasing_subsequences(lst.rest)                               # without the first element
        if len(with_first) > len(without_first):
            return with_first
        return without_first








class Link:
        """A linked list with a first element and the rest."""
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
                return 'Link({})'.format(self.first)
            return 'Link({0}, {1})'.format(self.first, self.rest)   

def filter_link(f, s):
    """ Returns a Link containing all the elements of linked list s for which f() returns a True."""
    if s is Link.empty:
        return s
    else:
        if f(s.first):
            return Link(s.first, filter_link(f, s.rest))
        return filter_link(f, s.rest)
