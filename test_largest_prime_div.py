from divisor_master import largest_prime_div

def test_simple_1():
    assert largest_prime_div(4) == None

def test_simple_2():
    assert largest_prime_div(40) == 20

def test_simple_3(): # специально сделал ошибку
    assert largest_prime_div(25) == [5, 5]

def test_simple_4():
    assert largest_prime_div(458) == [2, 229]


def test_simple_5():
    assert largest_prime_div(25784) == [2, 2, 2, 11, 293]