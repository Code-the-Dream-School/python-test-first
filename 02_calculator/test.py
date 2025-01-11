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

def test_make_dictionary():
    assert calculator.make_dictionary(first=1, second=2, third="three") == \
    {"first": 1, "second":2, "third": "three"}

def test_ingredients():
    assert calculator.ingredients(eggs=2, cheese="1/2 cup", bacon="2 strips") == \
    {"eggs", "bacon", "cheese"}
