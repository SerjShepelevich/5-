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
    list_d = map(lambda x:x if IsPrime(x) else 0,list_dividers(n))
    return max(list_d)

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
    return to_string(list_divs, n)

def to_string(list_divs, n):
    string_dic = str(n) + ' = '
    temp = ''
    for i in set(list_divs):
        temp += " * " + str(i) + '**' + str(list_divs.count(i))
    return string_dic + temp[2:]


#5)функция выводит самый большой делитель (не обязательно простой) числа.
def largest_div(n):
    list_divs = list_dividers(n)
    list_divs.reverse()
    if len(list_divs)>2:
        return list_divs[1]
    else: None



n = 144
print("Число является простым " , IsPrime(n))
print("список всех делителей числа: ", list_dividers(n))
print("самый большой простой делитель числа: ", largest_prime_div(n))
print("выводит самый большой делитель (не обязательно простой) числа: ", largest_div(n) )
print("каноническое разложение числа на простые множители ", canonical_decomposition(n))