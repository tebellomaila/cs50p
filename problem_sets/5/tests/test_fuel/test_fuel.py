import pytest
from fuel import convert,gauge

def test_convert_valid_fractions():
    assert convert(0/100) == 0
    assert convert("1/100") == 1
    assert convert(99/100) == 99
    assert convert("1/2") == 50
    assert convert(1/4) == 25
    assert convert(3/4) == 75

def test_convert_invalid_fractions():
    assert convert()
