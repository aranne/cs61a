def invert(x):
    result = 1/x                    # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result

def invert_safe(x):
    """ A safe version of invert(x), which considers the zero division situation.

    >>> invert_safe(2)
    Never printed if x is 0
    0.5
    >>> invert_safe(0)
    'division by zero'
    """
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)              # Coercing the ZeroDivisionError e to a string gives the human-interpretable string
