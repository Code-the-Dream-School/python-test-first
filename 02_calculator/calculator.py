# write your code here
import functools

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def sum(a):
    return functools.reduce(lambda x, y: x+y, a)

def multiply(a):
    return functools.reduce(lambda x, y: x*y, a)

def power(a,b):
    return a ** b

def factorial(a):
    f = 1
    while (a > 0):
        f = f * a
        a -= 1
    return f

       