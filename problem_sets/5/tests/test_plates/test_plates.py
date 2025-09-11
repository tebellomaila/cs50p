import pytest
from plates import is_valid

def test_valid_plates():
    """ Test plates for valid plates """
    assert is_valid("AB2") == True
    assert is_valid("AB20") == True
    assert is_valid("AAA222") == True
    assert is_valid("AB") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AB2000") == True

def test_invalid_plates():
    """ Test plates for invalid plates """
    assert is_valid("A0") == False
    assert is_valid("0A") == False
    assert is_valid("AB02BC") == False
    assert is_valid("AB012") == False
    assert is_valid("AB-20") == False
    assert is_valid("ABC201 GP") == False

def test_invalid_length():
    """ Test plates with invalid length """
    assert is_valid("A") == False
    assert is_valid("AAAAAAAA") == False
    assert is_valid("AB201BCE") == False
    assert is_valid("") == False

def test_first_two_letters():
    """ Test plates with first two characters """
    assert is_valid("A0") == False
    assert is_valid("0A") == False
    assert is_valid("A1") == False

def test_alphanumeric_plates():
    """ Test plates with special characters and punctuations """
    assert is_valid("AB 25DD") == False
    assert is_valid("ABC12_GP") == False
    assert is_valid("ABC-123") == False

def test_number_placement():
    """ Test plates with invalid number placement """
    assert is_valid("AB20CD") == False
    assert is_valid("A20CC") == False
    assert is_valid("20CC01") == False

def test_zero_as_first_number():
    """ Test plates with zero as the first number """
    assert is_valid("AB0") == False
    assert is_valid("0AB0") == False
    assert is_valid("AB0000") == False

