#Linked List Abstraction
empty = 'empty'
def is_link(s):
        """s is a linked list if it is empty or a (first, rest) pair."""
        return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
        """Construct a linked list from its first element and the rest."""
        assert is_link(rest), "rest must be a linked list."
        return [first, rest]
def first(s):
        """Return the first element of a linked list s."""
        assert is_link(s), "first only applies to linked lists."
        assert s != empty, "empty linked list has no first element."
        return s[0]
def rest(s):
        """Return the rest of the elements of a linked list s."""
        assert is_link(s), "rest only applies to linked lists."
        assert s != empty, "empty linked list has no rest."
        return s[1]
def len_link(s):
        """Return the length of linked list s."""
        length = 0
        while s != empty:
            s, length = rest(s), length + 1
        return length
def getitem_link(s, i):
        """Return the element at index i of linked list s."""
        while i > 0:
            s, i = rest(s), i - 1
        return first(s)
def join_link(s, separator):
        """Return a string of all elements in s separated by separator."""
        if s == empty:
            return ""
        elif rest(s) == empty:
            return str(first(s))
        else:
            return str(first(s)) + separator + join_link(rest(s), separator)

# We will represent a mutable linked list by a function that has a linked list as its local state
# Our mutable linked list will respond to five different messages:
# len, getitem, push_first, pop_first, and str.
# The first two implement the behaviors of the sequence abstraction.
# The next two add or remove the first element of the list
# The final message returns a string representation of the whole linked list.
def mutable_link():
        """Return a functional implementation of a mutable linked list."""
        contents = empty
        def dispatch(message, value=None):
            nonlocal contents     # To declare the contents will preserve the mutable value -- contents
            if message == 'len':
                return len_link(contents)
            elif message == 'getitem':
                return getitem_link(contents, value)
            elif message == 'push_first':      # To push the inputs value into the mutable value
                contents = link(value, contents)
            elif message == 'pop_first':
                f = first(contents)
                contents = rest(contents)
                return f
            elif message == 'str':
                return join_link(contents, ", ")
        return dispatch
def to_mutable_link(source):
        """Return a functional list with the same contents as source.
        >>> suits = ['heart','diamond','spade','club']
        >>> s = to_mutable_link(suits)
        >>> print(s('str'))
        heart, diamond, spade, club
        >>> s('pop_first')
        'heart'
        >>> print(s('str'))
        diamond, spade, club
        """
        s = mutable_link()
        for element in reversed(source):   # 每次把元素放在第一个，故需将source先倒序
            s('push_first', element)       # To push the inputs value -- element into the mutable value
        return s                           # With for statement, we can construct a mutable linked list.
