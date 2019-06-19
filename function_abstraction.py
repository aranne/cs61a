def improve(update, close, guess=1):          #improve function
    while not close(guess):
        guess = update(guess)
    return guess

def compose1(f, g):                          #to compose two function together
    def h(x):
        return f(g(x))
    return h

def close(x, y, tolerance=1e-15):            #to find if x and y are the same
        return abs(x - y) < tolerance


def summation(n, term):                                #sum function
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def curry2(f):                                 #currying function
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g

def uncurry2(g):                               #uncurrying function
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f

def compose1(f, g):                            #Lambda function
        return lambda x: f(g(x))

from operator import mul
def reduce(f, s, start):
    """ using f() functin to combine all the values in a list s with a start value start.
    This is a tail recursion, if f() uses only constant space, then reduce() is a constant space (theta 1).

    >>> reduce(mul, [3, 4, 5], 2)
    120
    >>> reduce(lambda x,y: [y, x], [3, 4, 5], 2)
    [5, [4, [3, 2]]]
    """
    if s == []:
        return start
    return reduce(f, s[1:], f(start, s[0]))


def map(f, s):
    """ map the function f() over all the elements in s, and then construct a new list containing them.
    This is not a tail recursion version.

    >>> map(lambda x: x*x, [1, 2, 3])
    [1, [4, 9]]
    """
    if len(s) == 1:
        return f(s[0])
    return [f(s[0]), map(f, s[1:])]
def map_tail(f, s):
    """ Below is a tail recursion version.
    >>> map(lambda x: x*x, [1, 2, 3])
    [1, [4, 9]]
    """
    def map_tail_call(s, m):
        if s == []:
            return m
        return map_tail_call(s[1:], [m, f(s[0])])
    return map_tail_call(s[1:], f(s[0]))
