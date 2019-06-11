def repr(x):
    return type(x).__repr__(x)            # type(x) give you the class name of x.

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return t.__repr__(x)

def print(x):
    if type(x) == str:
        return x
    return str(x)


class Str:
    def __str__(self):
        return '{}'.format(self)
    def __repr__(self):
        return "'{}'".format(self)

class Int:
    def __str__(self):
        return '{}'.format(self)
    def __repr__(self):
        return '{}'.format(self)
