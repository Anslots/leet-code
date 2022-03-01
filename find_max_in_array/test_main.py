from main import findMax

def test_gets_maximum_8():
    assert findMax([1, 4, 2, 8]) == 8


def test_gets_maximum_6():
    assert findMax([1, 6, 2, 3]) == 6


def test_gets_maximum_2():
    assert findMax([1, 1, 1, 2, 1, 1, 1]) == 2

def test_gets_maximum_negative2():
    assert findMax([-3, -4, -2]) == -2

def test_gets_maximum_negative_large():
    assert findMax([-3456, -4423, -2687]) == -2687
