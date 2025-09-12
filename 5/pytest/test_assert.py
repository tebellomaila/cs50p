def increment(n):
    return n + 1

def decrement(n):
    return n - 1

def test_increment():
    assert increment(0) == 1
    assert increment(1) == 2
    assert increment(2) == 3

def test_decrement():
    assert decrement(1) == 0
    assert decrement(2) == 1
    assert decrement(3) == 2
