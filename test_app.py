from app import add, multiply,div

def test_add():
    assert add(10, 20) == 30

def test_multiply():
    assert multiply(5, 4) == 20

def test_div():
    assert div(10, 2) == 5