def greatest_common_divisor(m, n):
    """return the largest k that divides both m and n.
    k, m, n are all positive integers.
    >>> greatest_common_divisor(4, 8)
    4
    >>> greatest_common_divisor(12, 8)
    4
    >>> greatest_common_divisor(5, 5)
    5
    """
    if m % n == 0:
        return n
    elif m < n:
        return greatest_common_divisor(n, m)
    else:
        return greatest_common_divisor(m - n, n)
        
