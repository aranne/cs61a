"""
To measure time efficiency：Using count(f) function.
"""
def count(f):
    """ Compute how many times a function f is called."""

    def counted(*args):
        counted.call_count += 1         # This .call_count attribute is bound to the function name, it's a funciton attribute.
        return f(*args)
    counted.call_count = 0
    return counted

def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-2) + fib(n-1)

>>> fib = count(fib)
"""
This assignment is equal to:
@count
def fib(n):
    ...
"""
>>> fib(19)
4181
>>> fib.call_count
13529

"""
Why this function will count how many times f is called?
Because of this fib = count(fib) assignment!
When we evaluate fib = count(fib) assignment, we bound fib(n) function to f, and bound counted(*args) function to fib.
So we compute fib(19), we compute counted(19) and return f(19), then we compute f(19) in fib(n) function, and return fib(18) + fib(17).
Attention! Here fib(18) means counted(18), fib(17) means counted(17), so we will go back into counted(*args) function to get f(18) + f(17).
In this progress, counted.call_count will record how many times we use f function.
"""

"""
To measure space efficiency: Using count_frames(f) function.
"""
"""
The higher-order count_frames function tracks open_count, the number of calls to the function f that have not yet returned.
The max_count attribute is the maximum value ever attained by open_count,
and it corresponds to the maximum number of frames that are ever simultaneously active during the course of computation.
"""
def count_frames(f):
        def counted(*args):
            counted.open_count += 1
            counted.max_count = max(counted.max_count, counted.open_count)
            result = f(*args)
            counted.open_count -= 1    # Once we have computed the return value --- result, we reclaim the space of memory, which means the open_count - 1.
            return result
        counted.open_count = 0
        counted.max_count = 0
        return counted

>>> fib = count_frames(fib)
>>> fib(19)
4181
>>> fib.open_count
0
>>> fib.max_count
19
>>> fib(24)
46368
>>> fib.max_count
24

"""
To summarize, the space requirement of the fib function, measured in active frames, is one less than the input, which tends to be small.
The time requirement measured in total recursive calls is larger than the output, which tends to be huge.
"""

"""
We can use memorization to increase time efficiency using memo(f) function:
"""
def memo(f):
        cache = {}
        def memorized(n):
            if n not in cache:
                cache[n] = f(n)
            return cache[n]
        return memorized

"""
In this case, we first count the times we call fib() using counted_fib, then we memorize the value we have computed.
Besides, we should not count the times we look up from cache dictionary using memorized(n) function,
so we should memo(count(fib)) rather than count(memo(fib)).
"""

>>> counted_fib = count(fib)             # To count how many times we use fib()
>>> memorized_fib = memo(counted_fib)
>>> fib = count(memorized_fib)            # To count how many times we reached memo() to look up in a dictionary.
>>> fib(19)
4181
>>> counted_fib.call_count
20
>>> fib.call_count
37
