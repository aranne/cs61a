"""
Write a function make_fib that returns a function that returns the next Fibonacci number each time it is called.
"""
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    a, b = [-1], [1]
    def fib_num():                     # Why we should define a new function?
        last_a = a.pop()               # Because we can leave a, b in the global frame, so that everytime we call fib() is in the child frame.
        a.append(last_a)               # So the a, b can be mutable.
        last_b = b.pop()
        b.append(last_b)
        a.append(last_b)
        b.append(last_a + last_b)
        return last_a + last_b
    return fib_num
