from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

# Pairs and Scheme lists

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:    # The second is still a number, so it's an ill-formed list.
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:             # When the while loop stopped, second is supposed to be a nil.
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):    # using k times the expression: y = y.second.
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))   # map fn over nil is still nil.
        else:
            raise TypeError("ill-formed list")    # Only two situations or Error.

class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):   # fn map nil returns nil.
        return self

nil = nil() # Assignment hides the nil class; there is only one instance


# Scheme list parser, without quotation or dotted lists.

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.

    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()              # each time you read just one value, and the index++ in the src.
    if val == 'nil':
        return nil
    elif val not in DELIMITERS:  # ( ) ' .  paranthesis or quotation or dot.
        return val              # get the numbers or symbols as the base case.
    elif val == "(":
        return read_tail(src)  # To find the tail ')'
    else:
        raise SyntaxError("unexpected token: {0}".format(val))

def read_tail(src):            # This is a Pair constructor.
    """Return the remainder of a list in src, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()             # Everytime we read src once, we need to pop() it, which means the index++, just like move one step of the pointer.
        return nil
    first = scheme_read(src)
    rest = read_tail(src)       # if in the self.current_line there's no ')', then the index will point to the last element in self.current_line. then go to src.pop(), go to self.current, then go to next(self.source), then go to next(tokenize_lines), go to next(input), finally go to the InputReader, input('next_line-->  ') means print('next_line-->  ) and then wait user to input.
    return Pair(first, rest)      # if there's '(', then calls read_tail, which returns a Pair(first, rest) constructor.


# Interactive loop

def buffer_input():
    return Buffer(tokenize_lines(InputReader('read> ')))   # 'read> ' is an initial prompt in InputReader Class, everytime we call buffer_input, we first print('> ') and then wait for user to input.

@main                              # This means the main function automatically run.
def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:                       # This is a while loop runs forever, even if we have an Error, we can get back to buffer_input() to input again, with a starter '> '
        try:
            src = buffer_input()    # src is a Buffer of an iterator-->[[line1], [line2],...]
            while src.more_on_line: # continue to read element in current_line.
                expression = scheme_read(src)   # each time read just one element in self.current_line.
                print(str(expression))
                print(repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return                              # this is the end of while True loop.
