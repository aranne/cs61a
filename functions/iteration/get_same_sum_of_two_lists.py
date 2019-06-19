def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    "*** YOUR CODE HERE ***"
    m, n = 0, 0
    def sum_lst(lst, x):        # sum the first x elements in lst.
        if x == 0:
            return lst[0]
        return lst[0] + sum_lst(lst[1:], x-1)
    k = 0
    while m < len(first) and k == 0:
        sum_first = sum_lst(first, m)
        n = 0
        while n < len(second) and k == 0:
            sum_second = sum_lst(second, n)
            if sum_first == sum_second:
                k = 1                      # Use k to determine whether we get the same summation.
            n += 1
        m += 1
    if k == 1:
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'
    # Official answer:
    "*** YOUR CODE HERE ***"
    m, n = 1, 1
    while m < len(first) and n < len(second) and sum(first[:m]) != sum(second[:n]):
        if sum(first[:m]) < sum(second[:n]):               # To compare one by one, and add new value to the smaller one.
            m += 1
        else:
            n += 1

    if sum(first[:m]) == sum(second[:n]):
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'
