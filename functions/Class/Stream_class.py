class Stream:
     """A lazily computed linked list."""
     class empty:
         def __repr__(self):
             return 'Stream.empty'
     empty = empty()  # empty is an instance of empty Class.
     def __init__(self, first, compute_rest=lambda: empty): # compute_rest is a function which has no parameter, returns a Stream or Stream.empty.
         assert callable(compute_rest), 'compute_rest must be callable.'
         self.first = first
         self._compute_rest = compute_rest
     @property
     def rest(self):
         """Return the rest of the stream, computing it if necessary."""
         if self._compute_rest is not None:
             self._rest = self._compute_rest()   # self._compute_rest() is a function being called, which will return a new Stream Class and instantiate it. The new instance is self._rest.
             self._compute_rest = None         # Once you call the function (get a value from stream), you cannot get it twice, so it's discarded. This is the caching machanism in Stream.
         return self._rest
     def __repr__(self):
         return 'Stream({0}, <...>)'.format(repr(self.first))  # We cannot represent the rest of value in a Stream.

""" Now we can use Stream to represent infinite sequential datasets."""
def integer_stream(first):
    """ Represent integer streams, starting at any first value.
    This stream is infinite!!!

    >>> positives = integer_stream(1)
    >>> positives
    Stream(1, <...>)
    >>> positives.first
    1
    >>> positives.rest
    Stream(2, <...>)
    >>> positives.rest.first
    2
    """
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)  # The integer_stream is lazy, because the recursive call to integer_stream is called only if .rest method is requested.

""" We can also use stream to build the function map and filter to implement lazy computing built-in generator function map and filter"""
def map_stream(fn, s):
    """ map fn over stream s, returns a new stream.

    >>> s = map_stream(lambda x: x*x, Stream(2, lambda: Stream(3, lambda: Stream(4, lambda: Stream(5)))))
    >>> s.first
    4
    >>> s.rest.first
    9
    >>> s.rest.rest.first
    16
    """
    def compute_rest():
        return map_stream(fn, s.rest)
    if s is Stream.empty:
        return s
    return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
    """ Look up in a stream s until a filtered value is found, and returns the filtered stream.
    If the value in current stream is not sufficient, then will look up the next one in stream immediately.


    """
    def compute_rest():
        return filter_stream(fn, s.rest)
    if s is Stream.empty:
        return 'There is not matched value in this stream.'
    elif fn(s.first):
        return Stream(s.first, compute_rest)  # compute the rest stream whenever .rest method is called.
    else:
        return compute_rest()  # This will compute the rest stream immediately.

def first_k_as_list(s, k):
    """ coerce up to first k elements in stream s to a Python list.

    >>> s = integer_stream(3)
    >>> s
    Stream(3, <...>)
    >>> m = map_stream(lambda x: x*x, s)
    >>> m
    Stream(9, <...>)
    >>> first_k_as_list(m, 5)
    [9, 16, 25, 36, 49]
    """
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k

"""
Now we want to define a stream of prime numbers using the sieve of Eratosthenes,
which filters a stream of integers to remove all numbers that are multiples of its first element.
Make sure that we remove the multiples of each element for every prime we find.
"""
def primes(pos_stream):
    """ returns a stream of prime numbers.

    >>> prime_numbers = primes(integer_stream(2))   # sieve prime numbers in integer using sieve of Eratosthenes method.
    >>> first_k_as_list(prime_numbers, 7)
    [2, 3, 5, 7, 11, 13, 17]
    """
    def not_divible(x):
        return x % pos_stream.first != 0  # this is based on this pos_stream.first, everytime we call a new prime(), pos_stream.first will change, so not_divible() function will change.
    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))  # This filter_stream cieves all the values that are multiples of this pos_stream.first (e.g. 2)
    return Stream(pos_stream.first, compute_rest)                       #-> then we create a new stream sieved multiples of 2, then we sieve multiples of its pos_stream.first(e.g. 3) in this new stream
                                                                        #-> so we will sieve all the streams based on multiples of primes which have occurred before.
                                 # each time we get a prime, we create a new stream.
def prime_stream():
    """ Return a stream that output all the prime."""
    return primes(integer_stream(2))
