class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value


    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            next_fib = Fib(1)
        else:
            next_fib= Fib(self.value + self.prev)       # We use self.prev to get the previous fib vaule, where self is bound to the previous Fib().
        next_fib.prev = self.value                    # We create an attribute of return value(next_fib) to store the previous value.
        return next_fib

    def __repr__(self):
        return str(self.value)
