from calculator.sum import sum

def test_sum():
    assert sum(2,2) == 4

def test_sum():
    assert sum(-20, -20) == -40

def test_sum():
    assert sum(-20, 20) == 0
    