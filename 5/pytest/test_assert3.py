import pytest

def zero_division():
    return 2 / 0

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        zero_division()

    assert "result" in str(excinfo.value)
