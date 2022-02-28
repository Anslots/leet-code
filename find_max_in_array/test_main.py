from main import findMax

def test_gets_maximum_8():
    assert findMax([1, 4, 2, 8]) == 8


def test_gets_maximum_6():
    assert findMax([1, 6, 2, 3]) == 6
