HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

# QUESTION: 1
def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

# QUESTION: 2
def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt
    return [round(sqrt(a)) for a in s if sqrt(a) == round(sqrt(a))]

# QUESTION: 3
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    first, second, last = 1, 2 ,3
    k = 3
    if n <= 3:
        return n
    while k < n:
        first, second, last = second, last, 3 * first + 2 * second + last
        k += 1
    return last

# QUESTION: 4
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    return count_parts(amount, max_power_of_two(amount))

def count_parts(n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m == 0:
        return 0
    else:
        return count_parts(n - m, m) + count_parts(n, max_power_of_two(m - 1))

def max_power_of_two(n):
    """ Find the largest power of two less than or equal n."""
    if n == 0:
        return 0
    k = n
    while k % 2 == 0:
        k = k / 2
    if k == 1:
        return n
    return max_power_of_two(n - 1)

# Official solution (which is apparently better)
# Because it's hard to find a power of two less than n,(in my answer, I used max_power_of_two function)
# but if we find the power of two from 1 and up to n in ascending order, like 1, 2, 4, 8...
# it will be easier to get all the power of two less than n
"""
def count_change(amount):
    return count_using(1, amount)

def count_using(min_coin, amount):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif min_coin > amount:
        return 0
    else:
        with_min = count_using(min_coin, amount - min_coin)
        without_min = count_using(2*min_coin, amount)
        return with_min + without_min
"""

# QUESTION: 5
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    # Find the middle rod
    middle = 1
    while  middle == start or middle == end:
        middle += 1

    if n == 1:
        print_move(start, end)
    else:                                 # The key is that, we must take the recursion leap of faith.
        move_stack((n - 1), start, middle)  # To believe the f(n - 1) is right.
        print_move(start, end)
        move_stack((n - 1), middle, end)
