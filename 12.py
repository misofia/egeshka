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
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3)'''

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
    sum = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    c = 0
    for i in range(1, sum + 1):
        if sum % i == 0 and i != 1 and i != sum:
            c += 1
    if c == 3:
        print(z)