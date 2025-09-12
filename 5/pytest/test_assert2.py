import pytest

a, b, c = 1, 2, 3

def test_a():
    assert a % 2 == 0, "value is odd, should be even"
    
def test_b():
    assert b % 2 == 0, "value is even"

def test_c():
    assert c % 2 == 0, "value is odd, should be even"
