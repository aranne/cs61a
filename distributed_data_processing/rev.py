#!/usr/bin/env python        

import sys

for line in sys.stdin:
    """ writes each line of its input to its output in reverse."""
    print(line.strip('\n')[::-1])
