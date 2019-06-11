#!/usr/bin/env python

import sys
from mr import emit        # MapReduce module

def count_vowels(line):
    """A map function that counts the vowels in a line."""
    for vowel in 'aeiou':           # for every type of vowel.
        count = line.count(vowel)    # count certain type of vowel in a line.
        if count > 0:
            emit(vowel, count)       # output a pair composed of (vowel, count)

for line in sys.stdin:
    count_vowels(line)      # count vowels over input from user, and emit pairs of (vowel, count)
