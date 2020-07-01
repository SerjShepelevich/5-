from divisor_master import canonical_decomposition

def test_simple_1():
    assert canonical_decomposition(4) == [2, 2]

def test_simple_2():
    assert canonical_decomposition(40) == [2, 2, 2, 5]

def test_simple_3(): # специально сделал ошибку
    assert canonical_decomposition(25) == [5, 5]

def test_simple_4():
    assert canonical_decomposition(458) == [2, 229]


def test_simple_5():
    assert canonical_decomposition(25784) == [2, 2, 2, 11, 293]
