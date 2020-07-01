from divisor_master import list_dividers

def test_simple_1():
    assert list_dividers(4) == [2, 4]

def test_simple_2():
    assert list_dividers(40) == [2, 4, 5, 8, 10, 20, 40]

def test_simple_3(): # специально сделал ошибку
    assert list_dividers(25) == [5, 24]

def test_simple_4():
    assert list_dividers(458) == [2, 229, 458]


def test_simple_5():
    assert list_dividers(25784) == [2, 4, 8, 11, 22, 44, 88, 293, 586, 1172, 2344, 3223, 6446, 12892, 25784]


