s = '8' * 68
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
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(x)