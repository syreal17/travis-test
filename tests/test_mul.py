from calculator import Calculator


def test_multiplication():
    c = Calculator()
    result = c.mul(5, 5)
    assert 25 == result
