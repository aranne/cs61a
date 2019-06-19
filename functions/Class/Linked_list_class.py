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
                return 'Link({})'.format(self.first)
            return 'Link({0}, {1})'.format(self.first, self.rest)    # This is a recursive call of __repr__ method.

        @property# This makes second attribute a property, you don't need to call it. if you don't have this decorator, you need to write s.second() other than s.second
        def second(self):
            """ return the second element in a linked list.
            >>> s = Link(3,Link(4,Link(5)))
            >>> s.second
            4
            """
            return self.rest.first

        @second.setter  # a @<attribute>.setter decorator on a method designates that this method will be called whenever the <attribute> is assigned.
        def second(self, value):   # The method should also be second.
            """ Assign the s.second to the value.
            >>> s = Link(3,Link(4,Link(5)))
            >>> s.second
            4
            >>> s.second = 6
            6
            """
            self.rest.first = value

def extend_link(s, t):
    """ Extend two linked list together."""
    if s is Link.empty:
        return t
    return Link(s.first, extend_link(s.rest, t))

Link.__add__ = extend_link
Link.__radd__ = extend_link        # Using this assignment to make the Class Link can use '+' operator in the interpreter.

def map_link(f, s):
    """ Applies a function f() to each element of linked list s. """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """ Returns a Link containing all the elements of linked list s for which f() returns a True."""
    if s is Link.empty:
        return s
    else:
        if f(s.first):
            return Link(s.first, filter_link(f, s.rest))
        return filter_link(f, s.rest)

def join_link(s, separator):
    """ Construct a string that contains all the elements of the linked list s separated by some separator string."""
    if s is Link.empty:           # if s is an empty linked list.
        return ''
    if s.rest is Link.empty:      # Attention: s is not Link.empty now!
        return '{}'.format(s.first)
    return '{}'.format(s.first) + '{}'.format(separator) + join_link(s.rest, separator)

############################################
###### Using Linked List ###################
############################################
def partitions(n, m):
        """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
        """
        if n == 0:
            return Link(Link.empty) # A list containing the empty partition
        elif n < 0 or m == 0:
            return Link.empty
        else:
            using_m = partitions(n-m, m)
            with_m = map_link(lambda s: Link(m, s), using_m)  # The base case is that using_m only has one element -- (). using_m == Link(())
            without_m = partitions(n, m-1)
            return with_m + without_m

def print_partitions(n, m):
    """ Print partitons in a human-readable manner with appropriate separator."""
    lists = partitions(n, m)     # The structure of lists is: Link(Link(..m..), Link(Link(..m-1..), ...)))
    strings = map_link(lambda s: join_link(s, " + "), lists) # join_link here put all the elements in a same m partitions together into a string.
    print(join_link(strings, "\n"))    # Now strings is a link whose elements are string.
