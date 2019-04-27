from calculator import Calculator


def test_addition():
    c = Calculator()
    result = c.add(2, 2)
    assert 4 == result


def test_subtraction():
    c = Calculator()
    result = c.sub(2, 2)
    assert 0 == result


def test_multiplication():
    c = Calculator()
    result = c.mul(5, 5)
    assert 25 == result


def test_division():
    c = Calculator()
    result = c.div(10, 2)
    assert 5 == result
