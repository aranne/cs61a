# we know that the relationship between Fahrenheit and Celsius temperatures is:
# 9 * c = 5 * (f - 32)
# Such an equation is not one-directional.
# Given any four of the quantities, we can use this equation to compute the fifth.
# We define primitive constraints that hold between quantities, such as an adder(a, b, c) constraint that enforces the mathematical relationship a + b = c.
# We combine constraints by constructing a network in which constraints are joined by connectors
# A connector is an object that "holds" a value and may participate in one or more constraints.
# 9 * c = 5 * (f - 32) This equation is a complex constraint between c and f.
# Such a constraint can be thought of as a network consisting of primitive adder, multiplier, and constant constraints.
# this system which is used to compute such equation is called constraint-based system.
# the web link is http://composingprograms.com/pages/24-mutable-data.html in section 2.4.13 Propagating Constraints
from operator import add, sub
def adder(a, b, c):
        """The constraint that a + b = c."""
        return make_ternary_constraint(a, b, c, add, sub, sub)
def make_ternary_constraint(a, b, c, ab, ca, cb):      # This function is to build a dictionary, and build up the connection between the a,b,c and the constraint
        """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
        def new_value():
            av, bv, cv = [connector['has_val']() for connector in (a, b, c)]     # a, b, c are connectors.
            if av and bv:
                c['set_val'](constraint, ab(a['val'], b['val']))               # if a and b both have values, then set up value of c. the constraint is the dictionary
            elif av and cv:                                                    # in different constrant, a,b,c are different,so the dictionary is different.
                b['set_val'](constraint, ca(c['val'], a['val']))               # when we setup a value, the constrant will be passed as message, which means the dictionary will be recorded.
            elif bv and cv:
                a['set_val'](constraint, cb(c['val'], b['val']))
        def forget_value():               # when we seed 'forget' message to a,b,c connectors, among which two connectors' informant are either 'user' or {},
            for connector in (a, b, c):    # so only the connector, of which the informant is dictionary, will forget its value.
                connector['forget'](constraint)
        constraint = {'new_val': new_value, 'forget': forget_value}     # constraint is a dictionary.
        for connector in (a, b, c):
            connector['connect'](constraint)                 # To pass the constraint message--dictionary to a,b,c connector.
        return constraint
# The dictionary called constraint is a dispatch dictionary, but also the constraint object itself.
#  It responds to the two messages that constraints receive, but is also passed as the source argument in calls to its connectors.
from operator import mul, truediv
def multiplier(a, b, c):
        """The constraint that a * b = c."""
        return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def connector(name=None):
        """A connector between constraints."""
        informant = None                           # informant is to record the source of the connector. Because no matter when we setup a connector, we write the
        constraints = []                           # source into the informant. the source can be a string like'user', or it can be a constraint(dictionary).
        def set_value(source, value):              # Because informant is a nonlocal value, so it just record the last source.
            nonlocal informant
            val = connector['val']
            if val is None:                   # if val is None, then we will write the value into the connector and record the source into informant.
                informant, connector['val'] = source, value
                if name is not None:          # if name is not None, that means this connector is variable(celsius or fahrenheit), then print it.
                    print(name, '=', value)
                inform_all_except(source, 'new_val', constraints)  # when we finish setup a connector, we need to inform other connectors. so we send message to
            else:                                                  # all the constraints relate to this connector except for the source one(last setup one).
                if val != value:      # if this connector already has a value, and the value is not equal, this will return a Error.
                    print('Contradiction detected:', val, 'vs', value)
        def forget_value(source):
            nonlocal informant
            if informant == source:    # when we forget the celsius or fahrenheit, which informant is 'user' or a dictionary. if we setup celsius and get fahrenheit.
                informant, connector['val'] = None, None # then the informant of celsius is 'user', informant of fahrenheit is a dictionary.
                if name is not None:                    # so if informant == source, that means we can only forget the value, which we setup. we cannot forget the value that we get.
                    print(name, 'is forgotten')       # if name is not None, that means the connector is celsius or fahrenheit, so we print.
                inform_all_except(source, 'forget', constraints)  # when we already forget value of a connector, we send message to other constraints except for the source to update other connector's value.
        def connect(source):
            constraints.append(source)                 # constraints will record all the constraints(dictionaries) that relate to the connector.
        connector = {'val': None,
                     'set_val': set_value,
                     'forget': forget_value,
                     'has_val': lambda: connector['val'] is not None,
                     'connect': connect}
        return connector
def inform_all_except(source, message, constraints):           # send message to all the constraints relate to the connector except for the source one (last setup one)
        """Inform all constraints of the message, except source."""  # if the other constraint recieve the message, it will change the value of other connectors.
        for c in constraints:
            if c != source:
                c[message]()

def constant(connector, value):               # constant is used to setup the constant connector. it won't send 'connect' message, so its constrant won't be record into the constant connector's constraints.
        """The constraint that connector = value."""
        constraint = {}                        # this constraint is a blank dictionary.
        connector['set_val'](constraint, value)
        return constraint

def converter(c, f):                           # converter function will build up all the constraints of the system.
        """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
        u, v, w, x, y = [connector() for _ in range(5)]
        multiplier(c, w, u)
        multiplier(v, x, u)
        adder(v, y, f)
        constant(w, 9)
        constant(x, 5)
        constant(y, 32)

celsius = connector('Celsius')            # To setup the celsius and fahrenheit connector and build the whole system.
fahrenheit = connector('Fahrenheit')
converter(celsius, fahrenheit)

# Test case:
def test(message, temperature, value=None):
    """
    To test the constraint-based system.
    message: 'setup' or 'forget'
    temperature: celsius or fahrenheit
    value: the value of the temperature
    >>> test('setup','celsius', 25)
    Celsius = 25
    Fahrenheit = 77.0
    >>> test('setup', 'fahrenheit', 212)
    Contradiction detected: 77.0 vs 212
    >>> test('forget', 'celsius')
    Celsius is forgotten
    Fahrenheit is forgotten
    >>> test('setup', 'fahrenheit', 212)
    Fahrenheit = 212
    Celsius = 100.0
    """
    if message == 'setup':
        if temperature == 'celsius':
            celsius['set_val']('user', value)
        if temperature == 'fahrenheit':
            fahrenheit['set_val']('user',value)
    if message == 'forget':
        if temperature == 'celsius':
            celsius['forget']('user')
        if temperature == 'fahrenheit':
            fahrenheit['forget']('user')
