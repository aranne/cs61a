# To implement Generic Function, which is a function that can accept values of multiple different types--- Object Abstraction,

######################################
###### Complex Number ################
######################################

"""
We implement a munipulating complex numbers in two representation --- rectangular form (real and imaginary) and polar form (magnitude and angle).
"""

"""
Step 1: Implement Class Number.        (The highest level of abstraction)

A Complex number is a Number, and numbers can be added or multiplied together.
The operator '+' or '*' will call __add__ or __mul__ when we munipulate two numbers using "+" or '*'
And how numbers can be added or multiplied (using __add__ and __mul__) is abstracted by the method names add and mul.
"""
class Number:
        def __add__(self, other):
            return self.add(other)
        def __mul__(self, other):
            return self.mul(other)
"""
After we implement Number Class, we can abstract '+' or '*' operator into add or mul attributes.
"""

"""
Step 2: Implement Class Complex.      (This class is a subclass of Number)

In Complex Class, we need to implement add and mul method for complex numbers specially.
The Complex class inherits from Number and describes arithmetic for complex numbers.

When adding complex numbers, we usually use rectangular form to represent the answer.
When multiplying complex numbers, we naturally use polar form to represent the answer.
"""

class Complex(Number):
        def add(self, other):
            return ComplexRI(self.real + other.real, self.imag + other.imag)
        def mul(self, other):
            magnitude = self.magnitude * other.magnitude
            return ComplexMA(magnitude, self.angle + other.angle)

"""
This implementation assumes that two classes exist for complex numbers, corresponding to their two natural representations:
1. ComplexRI constructs a complex number from real and imaginary parts.
2. ComplexMA constructs a complex number from a magnitude and angle.

In order to implement arithmetic of complex number, we introduced four Interface: real, imag, magnitude, angle.
"""

"""
Step 3: Implement ComplexRI and ComplexMA.                 (two class of complex numbers corresponding to two representation)

For complex arithmetic to be correct, these attributes must be consistent.
That is, the rectangular coordinates (real, imag) and the polar coordinates (magnitude, angle) must describe the same point on the complex plane.
In order to make these attribute values to maintain a fixed relationship with each other,
we store attribute values for only one representation and compute the other representation whenever it is needed.
"""

"""
The ComplexRI class stores real and imag attributes and computes magnitude and angle on demand.
"""
from math import atan2
class ComplexRI(Complex):
        def __init__(self, real, imag):
            self.real = real
            self.imag = imag
        @property                     # Python has a simple feature for computing attributes on the fly from zero-argument functions.
        def magnitude(self):          # The @property decorator allows functions to be called without call expression syntax (parentheses following an expression).
            return (self.real ** 2 + self.imag ** 2) ** 0.5
        @property
        def angle(self):
            return atan2(self.imag, self.real)
        def __repr__(self):
            return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)   # When we try to display a ComplexRI, the interpreter will call __repr__ to display it.
"""
>>> ri = ComplexRI(5, 12)
>>> ri.real
5
>>> ri.magnitude
13.0
>>> ri.real = 9
>>> ri.real
9
>>> ri.magnitude
15.0
"""

"""
Similarly, the ComplexMA class stores magnitude and angle, but computes real and imag whenever those attributes are looked up.
"""
from math import sin, cos, pi
class ComplexMA(Complex):
        def __init__(self, magnitude, angle):
            self.magnitude = magnitude
            self.angle = angle
        @property
        def real(self):
            return self.magnitude * cos(self.angle)
        @property
        def imag(self):
            return self.magnitude * sin(self.angle)
        def __repr__(self):
            return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
"""
>>> ma = ComplexMA(2, pi/2)
>>> ma.imag
2.0
>>> ma.angle = pi
>>> ma.real
-2.0
"""

"""
Our implementation of complex numbers is now complete.
Either class implementing complex numbers can be used for either argument in either arithmetic function in Complex.
"""

"""
Last step: Test case.
"""
from math import pi
"""
>>> ComplexRI(1, 2) + ComplexMA(2, pi/2)
ComplexRI(1, 4)
>>> ComplexRI(0, 1) * ComplexRI(0, 1)
ComplexMA(1, 1 * pi)
"""

###############################
###### Rational Number ########
###############################

"""
Rational number Class is also a subclass of Number Class.
"""
from fractions import gcd
class Rational(Number):
        def __init__(self, numer, denom):
            g = gcd(numer, denom)
            self.numer = numer // g
            self.denom = denom // g
        def __repr__(self):
            return 'Rational({0}, {1})'.format(self.numer, self.denom)
        def add(self, other):
            nx, dx = self.numer, self.denom
            ny, dy = other.numer, other.denom
            return Rational(nx * dy + ny * dx, dx * dy)
        def mul(self, other):
            numer = self.numer * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
"""
Test case.
"""

>>> Rational(2, 5) + Rational(1, 10)
Rational(1, 2)
>>> Rational(1, 4) * Rational(2, 3)
Rational(1, 6)


"""
Now, we want to add a rational number to a complex number.
We would like to introduce this cross-type operation in some carefully controlled way, so that we can support it without seriously violating our abstraction barriers.
There are two ways to implement this goal.
"""

"""
The first way is: Type Dispatching.

write functions that inspect the type of arguments they receive, then execute code that is appropriate for those types.
"""
"""
First we should add type tags to Complex and Rational Class.
"""
Rational.type_tag = 'rat'
Complex.type_tag = 'com'

"""
To combine complex and rational numbers, we write functions that rely on both of their representations simultaneously
"""
def add_complex_and_rational(c, r):
        return ComplexRI(c.real + r.numer/r.denom, c.imag)
def mul_complex_and_rational(c, r):
        r_magnitude, r_angle = r.numer/r.denom, 0
        if r_magnitude < 0:
            r_magnitude, r_angle = -r_magnitude, pi
        return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
        return add_complex_and_rational(c, r)
def mul_rational_and_complex(r, c):
        return mul_complex_and_rational(c, r)
"""
The role of type dispatching is to ensure that these cross-type operations are used at appropriate times.
Below, we rewrite the Number superclass to use type dispatching for its __add__ and __mul__ methods.
"""
class Number:
        def __add__(self, other):
            if self.type_tag == other.type_tag:
                return self.add(other)
            elif (self.type_tag, other.type_tag) in self.adders:  # self.adders is a dictionary.
                return self.cross_apply(other, self.adders)
        def __mul__(self, other):
            if self.type_tag == other.type_tag:
                return self.mul(other)
            elif (self.type_tag, other.type_tag) in self.multipliers:
                return self.cross_apply(other, self.multipliers)
        def cross_apply(self, other, cross_fns):
            cross_fn = cross_fns[(self.type_tag, other.type_tag)]
            return cross_fn(self, other)
        adders = {("com", "rat"): add_complex_and_rational,
                  ("rat", "com"): add_rational_and_complex}
        multipliers = {("com", "rat"): mul_complex_and_rational,
                       ("rat", "com"): mul_rational_and_complex}
"""
Test case:
"""
>>> ComplexRI(1.5, 0) + Rational(3, 2)
ComplexRI(3, 0)
>>> Rational(-1, 2) * ComplexMA(4, pi/2)
ComplexMA(2, 1.5 * pi)

"""
The second way is: Coercion

Often the different data types are not completely independent, and there may be ways by which objects of one type may be viewed as being of another type.
"""
"""
If we want to add complex number with rational number, we could view the rational number as a complex number whose imaginary part is zero.
In general, we can implement this idea by designing coercion functions that transform an object of one type into an equivalent object of another type.
"""
def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom, 0)

"""
The coerce method returns two values with the same type tag.
It inspects the type tags of its arguments, compares them to entries in the coercions dictionary, and converts one argument to the type of the other using coerce_to.
"""
class Number:
        def __add__(self, other):
            x, y = self.coerce(other)
            return x.add(y)
        def __mul__(self, other):
            x, y = self.coerce(other)
            return x.mul(y)
        def coerce(self, other):
            if self.type_tag == other.type_tag:
                return self, other
            elif (self.type_tag, other.type_tag) in self.coercions:
                return (self.coerce_to(other.type_tag), other)
            elif (other.type_tag, self.type_tag) in self.coercions:
                return (self, other.coerce_to(self.type_tag))
        def coerce_to(self, other_tag):
            coercion_fn = self.coercions[(self.type_tag, other_tag)]
            return coercion_fn(self)
        coercions = {('rat', 'com'): rational_to_complex}
