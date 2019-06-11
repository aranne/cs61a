########################################################
##################### String ###########################
########################################################

>>> s = 'Hello'
>>> s.upper()
'HELLO'
>>> s.lower()
'hello'
>>> s.swapcase()
'hELLO'
>>> s
'Hello'

a = 'A'
>>> ord(a) # This tells us the order in ASCII table is corresponde to 65
65
>>> hex(ord(a))  # Because the ASCII table is 8*16 table, which has 8 rows and 16 columns.
'0x41'           # So the hex() means change the order 65 to hexadecimal format--- 0x41, which means 'A' is 65th in order and is in 4th row 1st column.
>>> print('\n')  # '\n' will change to next line

>>> print('\a')  # '\a' will let us hear a bell from computer.

>>> from unicodedate import name, lookup   # name and lookup is used to change some strings to some characters based on unicode table.
>>> name('a')
'LATIN SMALL LETTER A'
>>> lookup('WHITE SMILING FACE')
'☺'
>>> lookup('SOCCER BALL')
'⚽'
>>> lookup('SOCCER BALL').encode()    # encoding it in bytes, the 'SOCCER BALL' is used 3 bytes to represent it.
b'\xe2\x9a\xbd'
>>> lookup('LATIN SMALL LETTER A').encode()
b'a'

#########################################################
################## List #################################
#########################################################

def list_demos():
    suits = ['coin', 'string', 'myriad']  # A list literal
    original_suits = suits  """these two name are bound to a same Object, NOT create a new Object! change a one will affect another."""
    suits.pop()             # Pop off one element: Removes and returns the final element
    suits.pop(index)        # Pop off the element referring to index and returns the element.
    suits.remove('string')  # Removes the first element that equals the argument
    suits.append('cup')              # Add an element to the end
    suits.extend(['sword', 'club'])  # Add all elements of a list to the end
    suits[2] = 'spade'  # Replace an elemen
    suits[0:2] = ['heart', 'diamond']  # Replace a slice
    suits.insert(2, 'Joker')         # Insert 'Joker' at Index 2.
    suits.index('Joker')             # Get the Index of 'Joker'
    suits.count('Joker')             # Return how many times 'Joker' appears in suits.
    [suit.upper() for suit in suits]
    [suit[1:4] for suit in suits if len(suit) == 5]
    suits.reverse()                  # reverse all the value in a list.
    suits[::-1]                      # returns a new suits which is reversed.

######################################################
##################### Dictionary #####################
######################################################

def dict_demos():
    numerals = {'I': 1.0, 'V': 5, 'X': 10}
    numerals['X']          # Loopup the value bound to the key
    numerals['I'] = 1      # Change the value bound to the key
    numerals['L'] = 50     # Make a new entry to the Dictionary
    numerals.pop('X')      # Get rid of the binding pair('X', 10)
    sum(numerals.values()) # Sum all the values in the Dictionary
    dict([(3, 9), (4, 16), (5, 25)])  # Create a Dictionary using these pairs.
    numerals.get('A', 0)   # Get the value refer to key 'A', if there doesn't exist the key, it returns the default value.
    numerals.get('V', 0)
    list(numerals.keys())  # Get all the keys in a List
    ['I', 'V', 'X']
    list(numerals.values())# Get all the values in a list
    [1.0, 5, 10]
    list(numerals.items()) # Get all the items(tuples) in a list
    [('one', 1), ('two', 2), ('three', 3)]
#####################################################
################# Tuple #############################
#####################################################

def tuple_demos():
    (3, 4, 5, 6)       # This is a tuple, which is a immutable data type.
    3, 4, 5, 6         # This can also represent a tuple.
    ()                 # An empty tuple
    tuple()            # Create an empty tuple.
    tuple([1, 2, 3])   # Create a tuple from a sequence.
    # tuple(2)
    (2,)               # A tuple which has only one element
    (3, 4) + (5, 6)    # Tuples can add together.
    (3, 4, 5) * 2
    5 in (3, 4, 5)     # Tuple has a membership of 5

    # {[1]: 2}        # Mutable data cannot be used as a key in a Dictionary, you will get an unhashable Error.
    {1: [2]}
    {(1, 2): 3}       # Tuple is immutable data type, so it can be used as a key in a Dictionary
    # {([1], 2): 3}   # This will also call an Error, Because there's a list in a tuple.
    {tuple([1, 2]): 3}

#####################################################
###################### Set ##########################
#####################################################
def set_demos():
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    s3 = {10}
    s1.isdisjoint(s2)   # Return True is s1 and s2 are disjoint.
    s1.issubset(s2)     # if s1 <= s2, return True.
    s1.issuperset(s2)   # if s1 >= s2, return True.
    s4 = s1.union(s2, s3)    # Return a new set with elements from s1 and all other sets. Attention: this will create a new set, s1 will not change.
    s5 = s1.intersection(s2, s4) # Return a new set with elements common to s1 and all other sets. Attention: this will create a new set, s1 will not change.
    s6 = s1.difference(s2)     # Return a new set with elements in s1 not in s2.
    # below are some manipulation to s1.
    s1.update(s2)        # update s1, adding elements from s2.
    s1.add(16)      # add an element to s1.
    s1.remove(16)   # remove an element from s1.Raises KeyError if elem is not contained in the set.
    s1.discard(14)  # Remove element 14 from the s1 if 14 is present.
    s1.pop()        # Remove and return an arbitrary element(the first element in python 3) from the set. Raises KeyError if the set is empty.
    s1.clear()      # clear all elements in s1.
