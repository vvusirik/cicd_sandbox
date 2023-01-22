from mymod.addition import add, add3


def test_add():
    assert add(1, 2) == 3


def test_add3():
    assert add3(1, 2, 3) == 6
