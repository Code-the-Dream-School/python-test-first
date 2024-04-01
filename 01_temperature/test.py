import temperature

def test_freezing_to_c():
    assert temperature.ftoc(32) == 0

def test_boiling_to_c():
    assert temperature.ftoc(212) == 100

def test_body_temp_to_c():
    assert temperature.ftoc(98.6) == 37

def test_f68_to_c():
    assert temperature.ftoc(68) == 20

def test_freezing_to_f():
    assert temperature.ctof(0) == 32

def test_boiling_to_f():
    assert temperature.ctof(100) == 212

def test_body_temp_to_f():
    assert temperature.ctof(37) == 98.6

def test_c20_to_f():
    assert temperature.ctof(20) == 68