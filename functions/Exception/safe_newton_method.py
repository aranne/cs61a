"""
Now we need to get the zero point of the objective function: f(x) = 2*x^2 + sqrt(x) using Newton method.
"""
from math import sqrt
def objective_f(x):
    return 2*x*x + sqrt(x)
def objective_df(x):
    return 4*x + 1/(2*sqrt(x))
############### Something changes:

def find_zero(f, df):
    def near_zero(x):                # To determine that is the anwser we want.
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def improve(update, close_to, guess=1.0):
    while not close_to(guess):
        guess = update(guess)
    return guess                        #get the final answer

def newton_update(f, df):               #to compose the update function
    def h(x):
        return x - f(x) / df(x)
    return h

def approx_eq(a, b, tolerance=1e-5):
    return abs(a - b) < tolerance       #return True if a == b

"""
We can try to run it:
>>> find_zero(objective_f,objective_df)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "safe_newton_method.py", line 59, in find_zero
    return improve(newton_update(f, df), near_zero)
  File "safe_newton_method.py", line 62, in improve
    while not close_to(guess):
  File "safe_newton_method.py", line 58, in near_zero
    return approx_eq(f(x), 0)
  File "safe_newton_method.py", line 51, in objective_f
    return 2*x*x + sqrt(x)
ValueError: math domain error

There's a ValueError, which means we culculate a root of negative number.

Now we need to improve this function with considering x < 0 situation.
In other word, if we imput x which is less than 0, will raise ValueError, however it will return the last guess value.
"""

"""First, we define a new class that inherits from Exception."""
class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess
    def __str__(self):
        return 'Error when iterating'

""" Next we define a version of improve, which handles ValueError by raising an IterImproveError."""
def improve(update, close_to, guess=1.0):
    try:
        while not close_to(guess):
            guess = update(guess)
        return guess
    except ValueError:
        raise IterImproveError(guess)   # Pass mostly recent guess value to IterImproveError.

""" Finally, we define safe_find_zero, which can handle an IterImproveError by returning its last guess."""
def safe_find_zero(f, df):
    """ To get the zero point of f function with considering ValueError situation in which it will return the most lastly guess value.

    >>> safe_find_zero(objective_f,objective_df)
    IterImproveError:  Error when iterating
    -0.030214676328644885
    """
    def near_zero(x):
        return approx_eq(f(x), 0)
    try:
        return improve(newton_update(f, df), near_zero)
    except IterImproveError as e:
        print('IterImproveError: ',str(e))
        return e.last_guess

"""Although this approximation is still far from the correct answer of 0, some applications would prefer this coarse approximation to a ValueError."""
