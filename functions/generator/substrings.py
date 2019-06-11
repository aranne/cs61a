def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])   # First yield prefixes from s[:-1], then yield the last one s.
        yield s
def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)   # Get all the substrings that contains the first letter.
        yield from substrings(s[1:])  # Slice the first letter of s, then get substrings of s[1:]
