from python_ref.timeframe_stack_reference import auto_stack


def test_auto_stack_15m():
    assert auto_stack("15", 15 * 60) == ("15", "60", "240")


def test_auto_stack_1h():
    assert auto_stack("60", 60 * 60) == ("60", "240", "1D")


def test_auto_stack_2h():
    assert auto_stack("120", 2 * 60 * 60) == ("120", "240", "1D")


def test_auto_stack_4h():
    assert auto_stack("240", 4 * 60 * 60) == ("240", "1D", "1W")


def test_auto_stack_1d():
    assert auto_stack("1D", 24 * 60 * 60) == ("1D", "1W", "1M")
