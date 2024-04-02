import timer

timer_1 = timer.Timer()

def test_timer_initialize():
    assert timer_1.seconds == 0

def test_timer_time_string():
    assert timer_1.time_string() == "00:00:00"

def test_timer_time_string_12():
    timer_1.seconds = 12
    assert timer_1.time_string() == "00:00:12"

def test_timer_time_string_66():
    timer_1.seconds = 66
    assert timer_1.time_string() == "00:01:06"

def test_timer_time_string_4000():
    timer_1.seconds = 4000
    assert timer_1.time_string() == "01:06:40"
    