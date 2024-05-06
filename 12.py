'''s = '8' * 68
while ('222' in s) or ('888' in s):
    if '222' in s:
        s = s.replace('222', '8', 1)
    elif '888' in s:
        s = s.replace('888', '2', 1)
print(s)

# задание с кореткой
s = '1' + '8' * 80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2')
    elif '288' in s:
        s = s.replace('288', '3')
    else:
        s = s.replace('3888', '1')
print(s)

# При какой наименьшей длине исходной строки будет содержать наибольшее возможное число единиц?
max_n = 0
for n in range(200, 300):
    s = '1' * n
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    if max_n < s.count('1'):
        max_n = s.count('1')
        index = n
print(index)

# Исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(x, y, z)

# Сумма
s = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    elif '>2' in s:
        s = s.replace('>2', '2>', 1)
    elif '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3)

# Статград
for z in range(1000):
    s = '>' + '1' * 15 + '2' * 35 + '3' * z
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        elif '>2' in s:
            s = s.replace('>2', '3>', 1)
        elif '>3' in s:
            s = s.replace('>3', '11>', 1)
    sum = s.count('1') + s.count('2') * 2 + s.count('3') * 3  #s1 = sum(list(map(int, s))) - сумма цифр в строке
    c = 0
    for i in range(1, sum + 1):
        if sum % i == 0 and i != 1 and i != sum:
            c += 1
    if c == 3:
        print(z)

# 2 способ
def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for m in range(1000):
    s = '>' + '1' * 15 + '2' * 35 + '3' * z
    while '>1' in s or '>2' in s or '>3' in s:
        s = s.replace('>1', '2>', 1)
        s = s.replace('>2', '3>', 1)
        s = s.replace('>3', '11>', 1)
    s = s[:-1]
    s1 = sum(list(map(int, s)))
    c = 0
    if len(div(int(s1))) == 5:
        print(m)

# Статград
for x in range(20):
    for y in range(20):
        for z in range(20):
            a = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in a:
                a = a.replace('01', '210', 1)
                a = a.replace('02', '3101', 1)
                a = a.replace('03', '2012', 1)
            if a.count('1') == 56 and a.count('2') == 44 and a.count('3') == 19:
                print(x + y + z + 2)'''

'''for x in range(50):
    a = '0' + '1' * x + '2' * x + '0'
    while '00' not in a:
        a = a.replace('011', '20', 1)
        a = a.replace('022', '10', 1)
        a = a.replace('01', '220', 1)
        a = a.replace('02', '110', 1)
        if a.count('1') == 40 and a.count('2') > 50:
            print(a.count('2'))'''

'''for n in range(3, 1001):
    s = '9' + '4' * n
    while '94' in s or '644' in s or '444' in s:
        s = s.replace('94', '4', 1)
        s = s.replace('644', '49', 1)
        s = s.replace('444', '6', 1)
    if s.count('4') != 0 and n // s.count('4') == 18:
        print(n)'''

# ЕГКР
maxs = 0
for n in range(3, 10000):
    a = '8' + '4' * n
    while '11' in a or '444' in a or '8888' in a:
        a = a.replace('11', '4', 1)
        a = a.replace('444', '88', 1)
        a = a.replace('8888', '1', 1)
    s = a.count('1') + a.count('4') * 4 + a.count('8') * 8
    maxs = max(s, maxs)
print(maxs)