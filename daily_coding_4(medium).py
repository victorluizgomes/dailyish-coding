'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
the first and last element of that pair. For example, car(cons(3, 4))
returns 3, and cdr(cons(3, 4)) returns 4.

Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)


# TESTCASES:
print(car(cons(3, 4))) # Should print 3

print(cdr(cons(3, 4))) # Should print 4
