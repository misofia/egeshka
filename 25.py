# 4987
'''for c1 in '0123456789':
    for c2 in '0123456789':
        a = int(f'1{c1}34567{c2}9')
        if a % 17 == 0:
            print(a, a // 17) # это легко, параша, едем дальше'''

# 4988
from fnmatch import *
for x in range(0, 10 ** 9 + 1, 169):
    if fnmatch(str(x), '123*4?5'):
        print(x, x // 169) # передать Максимке !!!!

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

def div(x):
    d = set()
    for i in range(1, int(x  0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(248015, 251575 + 1, 2):
    if len(div(i)) % 2 != 0:
        print(i, div(i))