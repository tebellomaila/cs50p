import pytest
from twttr import shorten

""" Test cases for the function shorten() """

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_no_vowels():
    assert shorten("tebello") == "tbll"
    assert shorten("jhb2025") == "jhb2025"
    assert shorten("123456") == "123456"

def test_shorten_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aeiouAEIOU") == ""

def test_shorten_mixed_characters():
    assert shorten("Hello World!") == "Hll Wrld!"
    assert shorten("I love programming in Python") == " lv prgrmmng n Pythn"
    assert shorten("Pa$Sword@123") == "P$Swrd@123"

def test_shorten_case_sensitivity():
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("lowercase") == "lwrcs"
    assert shorten("UPPERCASElowercase") == "PPRCSlwrcs"

