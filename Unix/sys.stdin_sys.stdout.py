import sys

for line in sys.stdin:                  # read from standard input.
    sys.stdout.write(' '.join(line))    # write lines with ' ' separated the characters.
    sys.exit()
