# Эффективный перебор
# Из открытого курса Кабанова

# 1 (А)
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

# 2 (A)
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

# 3 (A)
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

# 4 (A)
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

# 5 (A)
f = open('27A_2723.txt')
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
print(k19 * (k19 - 1) * (k19 - 2) / (2 * 3))