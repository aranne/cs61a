"""
These functions has a order of growth in time of theta log(n).
"""
def zap(n):
    i, count = 1, 0
    while i <= n:
        while i <= 5 * n:
            count += i
            print(i / 6)
            i *= 3             # Everytime i is 3 times than before.
    return count
