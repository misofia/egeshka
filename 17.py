# 4312
'''a = [int(x) for x in open('17-4.txt')]
c = 0
m = 10001
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        c += 1
        m = min(m, a[i])
print(c, m)

a = [int(x) for x in open('17-4.txt')]
ans = []
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        ans.append(a[i])
print(len(ans), min(ans))

# 4316
a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    s = sum(list(map(int, str(i))))
    if (s % 5 == 0) and (i % 3 ** 2 != 0):
        ans.append(i)
print(len(ans), max(ans))

# 4311
a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    if (i % 13 == 4) and (i % 8 == 1):
        ans.append(i)
print(max(ans), sum(ans))'''

# 4313
'''a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    if a[i] % 2 ** 4 == 1 and a[i] % 2 ** 3 == 0 and a[i] % 2 ** 2 == 0 and a[i] % 2 == 1 and a[i] % 5 ** 2 == 1 and a[i] % 5 == 1:
        ans.append(i)
print(max(ans))'''

# Номер 37348 РЕШУ ЕГЭ
'''a = [int(x) for x in open('17 (1).txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i]*a[j]) % 34 != 0:
            ans.append(a[i] + a[j])
print(len(ans), max(ans))'''

# Номер 37340 РЕШУ ЕГЭ
'''a = [int(x) for x in open('17 (2).txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i]-a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
            ans.append(a[i] + a[j])
print(len(ans), max(ans))'''

# Номер 37357 РЕШУ ЕГЭ
'''a = [int(x) for x in open('17 (3).txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i]+a[j] % 8 == 0:
            ans.append(a[i] + a[j])
print(len(ans), max(ans))'''

# 48465
'''a = [int(x) for x in open('17 (6).txt')]
ans = []
min6 = 10001
for i in range(len(a)):
    if abs(a[i]) % 10 == 6:
        min6 = min(min6, a[i])
for i in range(len(a)-1):
    if ((abs(a[i]) % 10 == 6 and abs(a[i+1]) % 10 != 6) or (abs(a[i]) % 10 != 6 and abs(a[i+1]) % 10 == 6)) and (a[i]2 + a[i+1]**2 < min6**2):
        ans.append(a[i]**2 + a[i+1]**2)
print(len(ans), max(ans))'''

# Номер 47221 РЕШУ ЕГЭ
'''a = [int(x) for x in open('17 (6).txt')]
ans = []
max6 = -10001
for i in range(len(a)):
    if abs(a[i]) % 10 == 3:
        max6 = max(max6, a[i])
for i in range(len(a)-1):
    if ((abs(a[i]) % 10 == 3 and abs(a[i+1]) % 10 != 3) or (abs(a[i]) % 10 != 3 and abs(a[i+1]) % 10 == 3)) and (a[i]**2 + a[i+1]**2 >= max6**2):
        ans.append(a[i]  2 + a[i + 1] ** 2)
print(len(ans), max(ans))'''

# Полкяков 4496
'''a = [int(x) for x in open('17-205.txt')]
ans = []
for i in range(len(a) - 1):
    if (abs(a[i]) - abs(a[i + 1])) % 74 == 0:
        ans.append(a[i] + a[i+1])
print(len(ans), max(ans))'''

# Поляков 5066
'''a = [int(x) for x in open('17-288.txt')]
ans = []
for i in range(len(a) - 2):
    if abs(a[i]) % 7 != abs(a[i + 1]) % 7 and abs(a[i + 1]) % 7 != abs(a[i + 2]) % 7 and abs(a[i]) % 7 != abs(a[i + 2]) % 7 and (a[i] < 0 or a[i+1] < 0 or a[i+2] < 0):
        ans.append((max(a[i], a[i+1], a[i+2])) - (min(a[i], a[i+1], a[i+2])))
print(len(ans), min(ans))'''

# Пояков 4693
'''a = [int(x) for x in open('17-243.txt')]
ans = []
m = []
for i in range(len(a) - 1):
    if a[i] % 119 == 0:
        m.append(a[i])
m1 = max(m)
for i in range(len(a) - 1):
    if ():
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))'''

# Пояков 4688
'''a = [int(x) for x in open('17-243.txt')]
ans = []
m = []
for i in range(len(a) - 1):
    if a[i] % 19 == 0:
        m.append(a[i])
m1 = max(m)
for i in range(len(a) - 1):
    if (a[i] > m1 or a[i+1] > m1):
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))'''
