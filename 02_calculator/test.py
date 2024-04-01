import calculator

def test_add_0_0():
    assert calculator.add(0,0) == 0

def test_add_2_2():
    assert calculator.add(2,2) == 4

def test_add_2_6():
    assert calculator.add(2,6) == 8

def test_subtract_10_4():
    assert calculator.subtract(10,4) == 6

def test_sum_seven():
    assert calculator.sum([7]) == 7

def test_sum_7_11():
    assert calculator.sum([7,11]) == 18

def test_sum_array():
    assert calculator.sum([1,3,5,7,9]) == 25

def test_multiply_two():
    assert calculator.multiply([6,7]) == 42

def test_multiply_several():
    assert calculator.multiply([4,5,8]) == 160

def test_power():
    assert calculator.power(2,5) == 32

def test_factorial_0():
    assert calculator.factorial(0) == 1

def test_factorial_10():
    assert calculator.factorial(10) == 3628800