class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        # Alternatively:
        # return super().withdraw(amount + self.withdraw_fee)

class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.6
    >>> jack.balance
    5.05
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):                 # No arguements here
        self.accounts = []              # To look up all accounts.

    def open_account(self, holder, amount, account_type=Account):     # Open an account for a holder.
        """Open an account_type for holder and deposit amount."""
        account = account_type(holder)       # Instantiate an account.
        account.deposit(amount)
        self.accounts.append(account)       # To record this new account.
        return account

    def pay_interest(self):
        """Pay interest to all accounts."""
        for account in self.accounts:         # pay interest to all the accounts.
            account.deposit(account.balance * account.interest)

    def too_big_to_fail(self):            # Protect the bank.
        return len(self.accounts) > 1        
