'''print('X Y Z W')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x <= y) == (y <= z)) and (y or w):
                    print(x, y, z, w)'''

'''from itertools import *


def f(x, y, z, w):
    return not(y <= x) or (z <= w) or not z


for a in product([0, 1], repeat = 7):
    table = [(a[0], 0, a[1], a[2]), # 1 строка
             (0, 1, a[3], a[4]),
             (1, a[5], a[6], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)'''

# f = и 0 и 1
'''print('X Y Z W F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = int((x == (not y)) <= ((z <= (not w)) and (w <= y)))
                print(x, y, z, w, f)'''

'''from itertools import *


def f1(x, y, z, w):
    return (x <= y) or ((not w) == z)


def f2(x, y, z, w):
    return (x <= y) == (w and (not z))


for a in product([0, 1], repeat=6):
    table = [(a[0], a[1], a[2], 0),  # 1 строка
             (a[3], a[4], 0, 0),
             (a[5], 0, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in table] == [f2(**dict(zip(p, r))) for r in table]:
                print(p)
'''

'''from itertools import *


def f1(x, y, z, w):
    return (w <= z) == (y <= x)


def f2(x, y, z, w):
    return (w <= z) and ((not x) == y)


for a in product([0, 1], repeat=3):
    table = [(a[0], 0, 0, 0),  # 1 строка
             (a[1], 0, 1, 1),
             (0, 0, a[2], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in table][0] == 0 and [f1( ** dict(zip(p, r))) for r in table][2] == 0 and [f2(**dict(zip(p, r))) for r in table][1] == 0 and [f2(**dict(zip(p, r))) for r in table][2] == 1:
                print(p)'''  # 6365

from itertools import *


print((a and b) == (not c)) and (b and d)
