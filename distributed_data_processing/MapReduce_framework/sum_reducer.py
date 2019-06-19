#!/usr/bin/env python

import sys
from mr import values_by_key, emit     # MapReduce module.

for key, value_iterator in values_by_key(sys.stdin):  # group values by key into an iterator value_iterator
    emit(key, sum(value_iterator))        # emit pairs of each unique key and sum the related iterator to get pair (key, summation)
