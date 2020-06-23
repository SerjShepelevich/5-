#1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        return True
    else:
        return False
#2) выводит список всех делителей числа;
def list_dividers(n):
    d = 2
    list_d = []
    while d <= n:
        if n % d == 0:
            list_d.append(d)
        d += 1
    return list_d
#3) выводит самый большой простой делитель числа.
def largest_prime_div(n):
    if IsPrime(n) == True:
        return n
    else:
        list_divs = list_dividers(n)
        list_divs.reverse()
        for i in list_divs:
            if IsPrime(i) == True:
                return i
        return None
#4) функция выводит каноническое разложение числа на простые множители;
def canonical_decomposition(n):
    temp_number = n
    list_divs = []
    d = 2
    while temp_number > 1 and d <= n :
        if IsPrime(d):
            if  temp_number % d == 0:
                list_divs.append(d)
                temp_number = temp_number / d
                d = 2
            else:
                d += 1
        else:
            d += 1
    return list_divs

#5)функция выводит самый большой делитель (не обязательно простой) числа.
def largest_div(n):
    list_divs = list_dividers(n)
    list_divs.reverse()
    if len(list_divs)>2:
        return list_divs[1]
    else: None



n = 609840
print("Число является простым " , IsPrime(n))
print("список всех делителей числа: ", list_dividers(n))
print("самый большой простой делитель числа: ", largest_prime_div(n))
print("выводит самый большой делитель (не обязательно простой) числа: ", largest_div(n) )
print("каноническое разложение числа на простые множители ", canonical_decomposition(n))