from square import square_number


def test_square_number():
    assert square_number(2) == 4
    assert square_number(-3) == 9
    assert square_number(0) == 0
    assert square_number(1.5) == 2.25