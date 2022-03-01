from ..is_even import is_even

def test_is_even_two():
    assert is_even(2)

def test_is_even_377():
    assert not is_even(377)

def test_is_even_18():
    assert is_even(18)
