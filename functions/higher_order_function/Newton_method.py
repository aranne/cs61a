#Using Newton's method to solve the mathematical problem
#To compute the arbitrary degree n root of a
#which means to solve the equation: x^n - a = 0
#use Newton's method to solve this equation

def power(x, n):
    product, k = 1, 1
    while k <= n:
        product = product * x
        k = k + 1
    return product

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess                        #get the final answer

def newton_update(f, df):               #to compose the update function
    def h(x):
        return x - f(x) / df(x)
    return h

def approx_eq(a, b, tolerance=1e-5):
    return abs(a - b) < tolerance       #return True if a == b

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def nth_root_a(n, a):                   #to get the nth root of a
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
