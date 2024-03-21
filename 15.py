# Универсальный код
'''def f(x, a):
    return (x % 25 != 0) <= ((x % 19 == 0) <= (x % a != 0))


for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 100)):
        print(a)'''

# ОТРЕЗКИ
'''def f(x, a1, a2):
    return (a1 <= x <= a2) <= (430 <= x <= 490) or (440 <= x <= 530)

m = 0
for a1 in range(400, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(400, 600)):
            m = max(m, a2 - a1)

print(m//10)'''  # всегда m//10

# треугольник
'''def t(n,m,k):
    return max(n,m,k) < n + m + k - max(n,m,k)
def f(A,x):
    return not (t(x,11,16) == ((not(max(x,5) > 10))) and  t(4,A,x))
for A in range(1000):
    if all (f(A,x) for x in range(1000)):
        print(A)'''

# ДЕЛЕНИЕ
'''for A in range(1, 500):
    flag = 0
    for x in range(1, 1000):
        if ((A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))) == 0:
            flag = 1
            break
    if flag == 0:
        print(A)'''

'''def d(n, m):
  return n % m == 0
for A in range(999, 0, -1):
  i = 0
  for x in range(1, 999):
    if ((not d(x,A)) <= (d(x,6) <= (not d(x,4)))):
      i = i + 1
  if (i == 998):
    print(A)'''

'''for A in range(1, 1000):
    i = 0
    for x in range(1, 1000):
        if (A % 3 == 0) and ((220 % x == 0) <= ((A % x != 0) <= (550 % x != 0))):
            i += 1
        if i == 999:
            print(A)'''

# КОНЬЮНКЦИЯ
'''for A in range(0,100,1):
  i = 0
  for x in range(0, 100):
    if ((x&25!=0) <= ((x&19 == 0) <= (x & A !=0))):
      i=  i  + 1
  if i == 100:
    print(A)'''

# ГРАФИКИ
'''for A in range(1000,-1,-1):
    i = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if ((2*x+y)!=70) or (x < y) or (A < x):
                i+=1
    if i == 10000:
        print(A, i)'''

# 22 Поляков
'''def f(x, a):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))


for a in range(0, 1000):
    if all(f(x, a) == 1 for x in range(0, 1000)):
        print(a)'''

# 370
'''def f(x, a):
    return (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

# 7267
'''def f(x, y, a):
    return (4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)


for a in range(-10, 1000):
    if any(f(x, y, a) == 0 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''

# 6222
'''def f(x, y, a):
    return (((x+y) - 73) <= 0) or ((37 - (x-y)) <= 0) or ((y - a) > 0)


for a in range(0, 1000):
    if all(f(x, y, a) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''

# 5921
'''def f(x, y, a):
    return (x + a >= 160) or ((x % 7 == 0) <= (x - 17 <= 0))


for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''

# 5920
'''def f(x, y, z, a):
    return ((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= ((x * y * z) % a == 0)


for a in range(1, 1000):
    if all(f(x, y, z, a) == 1 for x in range(0, 1000) for y in range(0, 1000) for z in range(0, 1000)):
        print(a)'''

# 7005 КЕГЭ
'''def f(x, a):
    return (37 + a + x + 45 == 180) == (a + x + 90 == 180) and (a + 23 >= 120)


for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

# 5905
'''def f(x, y, z, a):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > (a // 8))


for a in range(1, 100):
    if all(f(x, y, z, a) == 1 for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)'''

# 5880
'''def f(x, a):
    return ((x < (5 + a)) and (5 < (x + a)) and (a < (5 + x))) <= ((max(x, 11) <= 19) == (23 + 13 + x != 180))


for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

# 4881 Поляков (множества)
'''a = set()
p = {1, 12}
q = {12, 13, 14, 15, 16}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= (not P and not Q)


for x in range(-100, 1000):
    if f(x) == 0:
        a.add(x)
print(a)'''

# 3434
'''a = set(range(1000))
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) or ((not Q) <= (not A))


for x in range(1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))'''

# 2081 КЕГЭ
'''from itertools import *
b = [''.join(i) for i in product('01', repeat=8)]

a = set()
p = {i for i in b if i[0] == i[1] == '1'} # if i[:2] == '11'
q = {i for i in b if i[-1] == '0'}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= (P or (not Q))


for x in b:
    if f(x) == 0:
        a.add(x)
print(len(a))'''

# 4284
'''from itertools import *

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
q = {2, 4, 8, 10}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (Q <= A) and (A <= P)


k = 0
for i in range(1, 11):
    for a in combinations(p, i):
        if all(f(x) for x in p):
            k += 1
print(k)'''

# 1072
'''a = set(range(1000))
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not A))


for x in range(-100, 1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))'''

# 12924
'''a = set(range(1000))
p = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and ((not Q) <= (not A))


for x in range(-100, 1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))'''

# 4283
'''a = set()
p = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (P <= A) or ((not A) <= (not Q))


for x in range(-100, 1000):
    if f(x) == 0:
        a.add(x)
print(9 * 3 * 21 * 15)'''

# 3156
'''a = set(range(1000))
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not A))


for x in range(-100, 1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))'''

# 1409
'''a = set()
p = {2,4,6,8,10,12,14,16,18,20}
q = {3,6,9,12,15,18,21,24,27,30}
r = {12,24,36,48,60}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    R = x in r
    return (not A) <= ((P and Q) <= R)


for x in range(-100, 1000):
    if f(x) == 0:
        a.add(x)
print(18 * 6)'''

# ОТРЕЗКИ

# 4972 Поляков
'''from itertools import *
def f(x):
    P = 25 <= x <= 50
    Q = 54 <= x <= 75
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))


Ox = [i/4 for i in range(24 * 4, 76 * 4)]
ans = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        ans.append(a2 - a1)
print(min(ans))'''

# 4768
'''from itertools import *
def f(x):
    P = 1 <= x <= 98
    Q = 25 <= x <= 42
    A = a1 <= x <= a2
    return Q <= (((not P) and Q) <= A)


Ox = [i/4 for i in range(0 * 4, 99 * 4)]
ans = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        ans.append(a2 - a1)
print(min(ans))'''

# 6639
'''def f(x):
    P = 5 <= x <= 54
    Q = 50 <= x <= 93
    return ((not P) and Q) <= (x > A)


for A in range(-500, 500):
    k = 0
    for x in range(-500, 500):
        if f(x) == 0:
            k += 1
    if k == 20:
        print(A)'''

# 4137
'''def f(x):
    p = x in {48, 52, 56}
    q = 29 <= x <= 47
    return (((x % 3 != 0) and (not p)) <= ((abs(x - 50) <= 7) <= q)) or (x & a == 0)

for a in range(1, 500):
    if all(f(x) == 1 for x in range(500)):
        print(a)'''
