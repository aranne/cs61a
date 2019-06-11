# The mutable account data type below is implemented as a dictionary.
# It has a constructor account and selector check_balance, as well as functions to deposit or withdraw funds
# We implement passing message not use conditions but use dicitonary.
# the value in the dictionary is also mutable
def account(initial_balance):
    def deposit(amount):
	    dispatch['balance'] += amount
	    return dispatch['balance']
    def withdraw(amount):
	    if amount > dispatch['balance']:
	        return 'Insufficient funds'          # End the function with error
	    dispatch['balance'] -= amount
	    return dispatch['balance']
    dispatch = {'deposit':   deposit,
	            'withdraw':  withdraw,
	            'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):            # account now is a dispatch for passing message
	return account['withdraw'](amount)
def deposit(account, amount):
	return account['deposit'](amount)
def check_balance(account):
	return account['balance']

"""
a = account(20)                 # to set up a new account, the next three operations are base on this account.
deposit(a, 5)
withdraw(a, 17)
check_balance(a)
"""
