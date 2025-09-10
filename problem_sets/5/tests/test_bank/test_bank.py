import pytest
import bank

# Test greetings starting with `hello`
def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0

# Test greetings starting with `h` only
def test_h():
    assert bank.value("h") == 20
    assert bank.value("H") == 20

# Test greetings starting with `h` but not `hello`
def test_h_not_hello():
    assert bank.value("hi") == 20
    assert bank.value("Hi") == 20
    assert bank.value("hey") == 20
    assert bank.value("Hey") == 20

# Test greetings not starting with `h`
def test_other_greetings():
    assert bank.value("how are you doing?") == 20
    assert bank.value("Hola") == 20
    assert bank.value("What's up?") == 100
    assert bank.value("") == 100

# Test greetings with numbers and special symbols
def test_numeric_and_special_greetings():
    assert bank.value("H3llo") == 20
    assert bank.value("123hello") == 100
    assert bank.value("hello123") == 0
    assert bank.value("H@llo") == 20

# Test partial matches that starts with he
def test_partial_matches():
    assert bank.value("he") == 20
    assert bank.value("hell") == 20
    assert bank.value("hello, Newman") == 0
