# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value


    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            next_fib = Fib(1)
        else:
            next_fib= Fib(self.value + self.prev)       # We use self.prev to get the previous fib vaule, where self is bound to the previous Fib().
        next_fib.prev = self.value                    # We create an attribute of return value(next_fib) to store the previous value.
        return next_fib

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    input: the product's name and price.
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, kind, price):
        self.name = kind
        self.price = price
        self.balance = 0
        self.number = 0

    def restock(self, number):
        self.number += number
        return 'Current {0} stock: {1}'.format(self.name, self.number)

    def deposit(self, money):
        if self.number == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(money)
        self.balance += money
        return 'Current balance: ${}'.format(self.balance)

    def vend(self):
        if self.number == 0:
            return 'Machine is out of stock.'
        if self.balance < self.price:
            return 'You must deposit ${} more.'.format(self.price-self.balance)
        else:
            change = self.balance - self.price
            self.balance = 0
            self.number -= 1
            if not change:
                return 'Here is your {}.'.format(self.name)
            else:
                return 'Here is your {0} and ${1} change.'.format(self.name, change)
