# Write a version of the make_withdraw function that returns password-protected withdraw functions.
# make_withdraw should take two arguments --- a password (a string) and balance.
# The returned function should take two arguments: an amount to withdraw and a password.
# A password-protected withdraw function should only process withdrawals that include a password that matches the original.
# Upon receiving an incorrect password, the function should:
# Store that incorrect password in a list, and return the string 'Incorrect password'.
# If a withdraw function has been called three times with incorrect passwords p1, p2, and p3, then it is locked. The incorrect passwords may be the same or different.
# All subsequent calls to the function should return:
# "Your account is locked. Attempts: [<p1>, <p2>, <p3>]"
def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance          # We need a nonlocal statement because we need rebind balance in nonlocal frame.
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
def make_withdraw_list(balance):
    b = [balance]               # Here we don't need a nonlocal statement any more, because we don't need to rebind b to a new list, but we just change the value in mutabal list.
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    a = []
    def withdraw(amount, putin_password):# Why should we define a new function? Because we need to compare amount with balance and putin_password with original_password
        nonlocal balance
        if len(a) >= 3:                                      # We should first check if this account is locked.
            return "Your account is locked. Attempts: %s" % a   # How to return this string. Using %s , % argument
        if putin_password == password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        a.append(putin_password)
        return 'Incorrect password'
    return withdraw

######################################################
########### Joint account ############################
######################################################
# Suppose that our banking system requires the ability to make joint accounts. Define a function make_joint that takes three arguments.
# 1. A password-protected withdraw function,
# 2. The password with which that withdraw function was defined, and
# 3. A new password that can also access the original account.
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')   # first time to joint two account to get a new account j.
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')   # joint new account j with another account to get a new account j2.
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    test = withdraw(0, old_password)  # !!! if the old_password is right, there's nothing happened. But if old_password is wrong, return 'Incorrect password'!!!!!
    if type(test) == str:       # This is a test case: to test whether old_password is right. If the return is a string, considing the amount is 0,
        return test            # so the ruturn 'Insufficient funds' is impossible. If old_password is wrong or the withdraw account is locked, return the string.
    def joint(amount, putin_password):
        if putin_password == old_password or putin_password == new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, putin_password)
    return joint
