from return_largest import return_larger_number

def test_gets_6():
    assert 6 == return_larger_number(6, 2)

def test_gets_327():
    assert 327 == return_larger_number(47, 327)
