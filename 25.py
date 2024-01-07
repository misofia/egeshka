# 4987
'''for c1 in '0123456789':
    for c2 in '0123456789':
        a = int(f'1{c1}34567{c2}9')
        if a % 17 == 0:
            print(a, a // 17) # это легко, параша, едем дальше'''

# 4988
'''from fnmatch import *
for x in range(0, 10 ** 9 + 1, 169):
    if fnmatch(str(x), '123*4?5'):
        print(x, x // 169)''' # передать Максимке !!!!

# простой алгоритм для нахождения делителей числа

'''a = int(input())
b = []
for i in range(1, a + 1):
    if a % i == 0:
        b.append(i)
print(b)'''

# усовершенствованный алгоритм для нахождения делителей числа

'''def div(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


print(div(36))'''

# Номер 2926 Поляков

'''def div(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(209834, 209857 + 1):
    if len(div(i)) == 4:
        print(div(i))'''

# Номер 2858 Поляков

'''def div(x):
    d = set()
    for i in range(2, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(135790, 163228 + 1):
    if sum(div(i)) >= 460000:
        print(len(div(i)), sum(div(i)))'''


# Номер 2905 Поляков

'''def div(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(248015, 251575 + 1, 2):
    if len(div(i)) % 2 != 0:
        print(i, div(i))'''

# Номер 2562 Поляков
'''def f(x):
    d = set()
    for i in range(2, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(174457, 174505 + 1):
    if len(f(x)) == 2:
        print(f(x))'''

# Номер 2572 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                d.add(i)
            if (x // i) % 2 == 0:
                d.add(x // i)
    return sorted(d)


for x in range(190201, 190260 + 1):
    if len(f(x)) == 4:
        print(f(x)[-1], f(x)[-2])'''

# Номер 2574 Поляков
'''def f(x):
    d = set()
    for i in range(2, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for x in range(...):
    if len(f(x)) == 3:
        print(f(x))'''

# Номер 2575 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for x in range(int(244143  0.25), int(1367821  0.25) + 1):
    if len(f(x)) == 2:
        print(x  2, x  3)'''

# Номер 2897 Поляков Простые числа
'''def f(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

k = 0

for x in range(2358827, 2358891 + 1):
    if len(f(x)) == 2:
        k += 1
        print(k,x)'''

# Номер 3440 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
summ = 0

for x in range(33333, 55555):
    summ = int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) + int(str(x)[4])
    if len(f(x)) == 2 and summ > 35:
        print(x, summ)'''

# функция, которая опеделяет пстые числа
'''def p(x):


    return (x > 1) and all(x % 1 for i in range(2, int(x  0.5) +1))'''


# Номер 5957 Поляков

'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

# дз
# 1
for x in range(1, 10 ** 9 + 1):
    if len(f(x)) == 117 and (str(x)[:2] == str(x)[-2:]):
        print(f(x)[-2:])'''
'''def f(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 != 0:
                d.add(i)
            if x // i != i and x // i % 2 != 0:
                d.add(x // i)
    return sorted(d)


for x in range(95632, 95650 + 1):
    if len(f(x)) == 6:
        print(f(x))'''
# 2
'''def f(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


n = 0
for x in range(245690, 245756 + 1):
    if len(f(x)) == 2:
        n = x - 245689
        print(n, f(x))'''
# 3
'''def f(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i != 1 and i != x:
                d.add(i)
                d.add(x // i)
    return sorted(d)


for x in range(123456789, 223456789 + 1):
    if len(f(x)) == 3:
        print(f(x))'''
# 5
'''from fnmatch import *
for x in range(0, 10 ** 9 + 1, 23):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x // 23)'''
# 3
'''import math

for i in range(123456789, 223456789):
    if int(math.sqrt(i)) ** 2 == i:
        a = []
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                a.append(j)
                b = i // j
                if j != b:
                    a.append(b)
        if len(a) == 3:
            a.sort()
            print(i, max(a))'''
