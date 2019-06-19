def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):                       #将变量 n 扩展为 n 和 term，提高代码的通用性
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    assert n > 0,'Must input natural numbers'
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers

    >>> sum_cubes(5)
    225
    """
    assert n > 0,'Must input natural numbers'
    return summation(n, cube)
