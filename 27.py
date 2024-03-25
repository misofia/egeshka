# Эффективный перебор
# Из открытого курса Кабанова

# 1 сумма чётна
# (А)
'''k = 0
f = open('27A_2719.txt')
n = int(f.readline())
a = [int(x) for x in f]
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            k += 1
print(k)

# (B) невероятно быстрый перебор
f = open('27B_2719.txt')
n = int(f.readline())
k0 = k1 = 0
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0: k0 += 1
    else: k1 += 1
print(k0 * (k0 - 1) // 2 + k1 * (k1 - 1) // 2)'''

# 2 произведение кратно 7
# (A)
'''f = open('27A_2720.txt')
n = int(f.readline())
k7 = k = 0
for i in range(n):
    x = int(f.readline())
    if x % 7 == 0: k7 += 1
    else: k += 1
print(k7 * (k7 - 1) / 2 + k7 * k) # делить на 2 не надо тк разные множества

# (B)
f = open('27B_2720.txt')
n = int(f.readline())
k7 = k = 0
for i in range(n):
    x = int(f.readline())
    if x % 7 == 0: k7 += 1
    else: k += 1
print(k7 * (k7 - 1) / 2 + k7 * k)'''

# 3 произведение кратно 65
# (A)
'''f = open('27A_2721.txt')
n = int(f.readline())
k65 = k13 = k5 = k = 0 # 65 = 13 * 5
for i in range(n):
    x = int(f.readline())
    if x % 65 == 0: k65 += 1
    elif x % 13 == 0: k13 += 1
    elif x % 5 == 0: k5 += 1
    else: k += 1
print(k65 * (k65 - 1) / 2 + k65 * (k13 + k5 + k) + k13 * k5)

# (B)
f = open('27B_2721.txt')
n = int(f.readline())
k65 = k13 = k5 = k = 0 # 65 = 13 * 5
for i in range(n):
    x = int(f.readline())
    if x % 65 == 0: k65 += 1
    elif x % 13 == 0: k13 += 1
    elif x % 5 == 0: k5 += 1
    else: k += 1
print(k65 * (k65 - 1) / 2 + k65 * (k13 + k5 + k) + k13 * k5)'''

# 4 произведение кратно 5 и сумма нечётная
# (A)
'''f = open('27A_2722.txt')
n = int(f.readline())
k5_1 = k1 = k0 = k5_0= 0
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0 and x % 2 == 0: k5_1 += 1
    elif x % 5 == 0 and x % 2 != 0: k5_0 += 1
    elif x % 5 != 0 and x % 2 == 0: k1 += 1
    elif x % 5 != 0 and x % 2 != 0: k0 += 1
print(k5_1 * k5_0 + k5_1 * k0 + k5_0 * k1)

# (B)
f = open('27B_2722.txt')
n = int(f.readline())
k5_1 = k1 = k0 = k5_0= 0
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0 and x % 2 == 0: k5_1 += 1
    elif x % 5 == 0 and x % 2 != 0: k5_0 += 1
    elif x % 5 != 0 and x % 2 == 0: k1 += 1
    elif x % 5 != 0 and x % 2 != 0: k0 += 1
print(k5_1 * k5_0 + k5_1 * k0 + k5_0 * k1)'''

# 5 тройки чисел кратны 19
# (A)
'''f = open('27A_2723.txt')
n = int(f.readline())
k19 = 0
for i in range(n):
    x = int(f.readline())
    if x % 19 == 0: k19 += 1
print(k19 * (k19 - 1) * (k19 - 2) / (2 * 3))

# (B)
f = open('27B_2723.txt')
n = int(f.readline())
k19 = 0
for i in range(n):
    x = int(f.readline())
    if x % 19 == 0: k19 += 1
print(k19 * (k19 - 1) * (k19 - 2) / (2 * 3))'''

# 6 сумма кратна 131
# (A)
'''f = open('27A_2724.txt')
n = int(f.readline())
k = [0] * 131
for i in range(n):
    x = int(f.readline())
    k[x % 131] += 1
count = k[0] * (k[0] - 1) // 2
for i in range(1, 65 + 1):
    count += k[i] * k[131 - i] # умножаем тк количество пар
print(count)


# (B)
f = open('27B_2724.txt')
n = int(f.readline())
k = [0] * 131
for i in range(n):
    x = int(f.readline())
    k[x % 131] += 1
count = k[0] * (k[0] - 1) // 2
for i in range(1, 65 + 1):
    count += k[i] * k[131 - i]
print(count)'''

# 7 разность кратна 69
# (A)
'''f = open('27A_2725.txt')
n = int(f.readline())
k = [0] * 69
for i in range(n):
    x = int(f.readline())
    k[x % 69] += 1
count = 0
for i in range(0, 69):
    count += k[i] * (k[i] - 1) // 2
print(count)

# (B)
f = open('27B_2725.txt')
n = int(f.readline())
k = [0] * 69
for i in range(n):
    x = int(f.readline())
    k[x % 69] += 1
count = 0
for i in range(0, 69):
    count += k[i] * (k[i] - 1) // 2
print(count)'''

# 8 сумма кратна 80 и хотя бы одно число больше 50000
# (A)
'''f = open('27A_2733.txt')
n = int(f.readline())
k5 = [0] * 80
k0 = [0] * 80
for i in range(n):
    x = int(f.readline())
    if x > 50000: k5[x % 80] += 1
    else: k0[x % 80] += 1
count = 0

count += k5[0] * (k5[0] - 1) // 2 + k5[40] * (k5[40] - 1) // 2 # когда оба больше 50000
for i in range(1, 40):
    count += k5[i] * k5[80 - i]

count += k5[0] * k0[0] + k5[40] * k0[40] # когда одно больше 50000
for i in range(1, 40):
    count += k5[i] * k0[80 - i]
    count += k0[i] * k5[80 - i]
print(count)

# (B)
f = open('27B_2733.txt')
n = int(f.readline())
k5 = [0] * 80
k0 = [0] * 80
for i in range(n):
    x = int(f.readline())
    if x > 50000: k5[x % 80] += 1
    else: k0[x % 80] += 1
count = 0

count += k5[0] * (k5[0] - 1) // 2 + k5[40] * (k5[40] - 1) // 2 # когда оба больше 50000
for i in range(1, 40):
    count += k5[i] * k5[80 - i]

count += k5[0] * k0[0] + k5[40] * k0[40] # когда одно больше 50000
for i in range(1, 40):
    count += k5[i] * k0[80 - i]
    count += k0[i] * k5[80 - i]
print(count)'''

# 9
# (A)
'''f = open('27A_2737.txt')
n = int(f.readline())
k = [0] * 2000
for i in range(n):
    x = int(f.readline())
    if x < 2000: k[x] += 1

c = k[1000] * (k[1000] - 1) // 2
for i in range(1, 1000):
    c += k[i] * k[2000 - i]
print(c)

# (B)
f = open('27B_2737.txt')
n = int(f.readline())
k = [0] * 2000
for i in range(n):
    x = int(f.readline())
    if x < 2000: k[x] += 1

c = k[1000] * (k[1000] - 1) // 2
for i in range(1, 1000):
    c += k[i] * k[2000 - i]
print(c)'''

# 10 максимальную нечётную пару
# (A)
'''f = open('27A_2726.txt')
n = int(f.readline())
k1 = []
k0 = []
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0: k1 += [x]
    else: k0 += [x]
k1.sort()
k0.sort()
print(k1[-1] + k0[-1])

# (B)
f = open('27B_2726.txt')
n = int(f.readline())
k1 = []
k0 = []
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0: k1 += [x]
    else: k0 += [x]
k1.sort()
k0.sort()
print(k1[-1] + k0[-1])'''

# 11
# (A)
'''f = open('27A_2727.txt')
n = int(f.readline())
k31 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 31 == 0: k31 += [x]
    else: k += [x]
k31.sort()
k.sort()
print(min(k) * min(k31))

# (B)
f = open('27B_2727.txt')
n = int(f.readline())
k31 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 31 == 0: k31 += [x]
    else: k += [x]
k31.sort()
k.sort()
print(min(k[0] * k31[0], k31[0] * k31[1]))'''

# 12
# (A)
'''f = open('27A_2728.txt')
n = int(f.readline())
k23 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 23 == 0: k23 += [x]
    else: k += [x]
k23.sort()
k.sort()
print(max(k[-2] + k23[-1], k23[-1] + k23[-2]))

# (B)
f = open('27B_2728.txt')
n = int(f.readline())
k23 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 23 == 0: k23 += [x]
    else: k += [x]
k23.sort()
k.sort()
print(max(k23[-3] + k23[-1], k23[-1] + k[-2]))'''

# 13
# (A)
'''f = open('27A_2729.txt')
n = int(f.readline())
k11 = []
k = []'''


# РЕШУ ЕГЭ 48448
f = open('27-B.txt')
n = int(f.readline())
k = [0] * 3
for i in range(n):
    x = int(f.readline())
    k[x % 3] += 1