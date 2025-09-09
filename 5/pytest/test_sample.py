# content of test_sample.py

def inc(n):
    return n + 1

def test_inc():
    assert inc(2) == 3
    assert inc(3) == 4
    assert inc(4) == 5
