"""
>>> a = 'a'
'This is a string: {}'.format(a)        # return a string that contains a variable.

import random
random.choice(list)   # random choice an element in a list.

eval('expression') # evaluate the expression and returns the result of it.
>>> x = 2
>>> eval('3 * x + 4')
10
>>> eval('"This is the number: "')
'This is the number'


repr(object)   # returns a canonical string of that object.
>>> a = {'A': 1, 'B': 2}
>>> repr(a)
"{'A': 1, 'B': 2}"


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n

def input(*args):      # *args means there will be arbitrary parameters in this input() function.
    for a in args:
        a += 1
        print(a)
