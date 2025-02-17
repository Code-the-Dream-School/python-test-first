# write your code here
import functools

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def sum(a):
    return functools.reduce(lambda x, y: x+y, a)def test_multiply():
    assert calculator.multiply(6,7) == 42

# The following tests should be added to tests.py, not to calculator.py
# def test_power():
#     assert calculator.power(2,5) == 3

# def test_factorial_0():
#     assert calculator.factorial(0) == 1

# def test_factorial_10():
#     assert calculator.factorial(10) == 3628800

# def test_sum_b():
#     assert calculator.sum_b(5, 8, 9, 2) == 24


# The following methods should be added to calculator.py

def sum_b(*args):
    return functools.reduce(lambda x, y: x+y, args)

def multiply(a,b):
    return a*b

def power(a,b):
    return a ** b

def factorial(a):
    f = 1
    while (a > 0):
        f = f * a
        a -= 1
    return f

def make_dictionary(**kwargs):
    return kwargs

def ingredients(**kwargs):
    return set(kwargs.keys())

       