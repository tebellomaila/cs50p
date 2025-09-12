import pytest
from fuel import convert,gauge

# Test suite for the convert and fuel gauge functions

def test_convert_valid_fractions():
    """ Test convert function with valid values """
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("98/100") == 98
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_convert_invalid_fractions():
    """ Test convert function with invalid values """
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("110/4")
    with pytest.raises(ValueError):
        convert("4/120")
    with pytest.raises(ValueError):
        convert("110/90")


def test_convert_invalid_format():
    """ Test convert function with invalid format inputs """
    with pytest.raises(ValueError):
        convert("14")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("1/")
    with pytest.raises(ValueError):
        convert("/4")

def test_convert_rounding():
    """ Test that convert function properly rounds to the nearest integer """
    convert("2/3") == 67
    convert("3/5") == 60
    convert("33/99") == 33
    with pytest.raises(ValueError):
        convert("5/3")



def test_gauge_values():
    """ Test gauge function with distinct percentage values """
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(33) == "33%"
    assert gauge(66) == "66%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_threshold():
    """ Test gauge function with threshold values """
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
