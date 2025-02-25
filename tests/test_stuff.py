import pytest

from stuff.stuff import divide_it

print(divide_it(5, 5))


def test_divide_it():
    assert divide_it(5, 1) == 5.0


def test_divide_it_different_types_negative():
    with pytest.raises(ArithmeticError):
        divide_it(5.0, 1)


def test_divide_it_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide_it(5, 0)


if __name__ == '__main__':
    pytest.main([__file__])