import pytest
from twttr import shorten

def test_shorten_empty():
    assert shorten() == ""

def test_shorten_no_vowels():
    assert shorten("tbll") == "tbll"
    assert shorten("tb@123!") == "tb@123"
    assert shorten("123") == "123"

def test_shorten_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aeiouAEIOU") == ""

def test_shorten_mixed_characters():
    assert shorten("Hello World :)") == "Hll Wrld :)"
    assert shorten("I am Programming in Python!") == " m Prgrmmng n Pythn!"
    assert shorten("P@s$wOrD@123") == "P@sSwrD@123"

def test_shorten_case_sensitivity():
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("lowercase") == "lwrcs"
    assert shorten("UPPERCASElowercase") == "PPRCSlwrcs"

