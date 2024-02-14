# №19 - 21 (одна куча)
'''def f(s, c, m): # s - знчение, с - номер хода, m - выигрышный ход
    if s >= 129: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)] # ходы
    return any(h) if (c + 1) % 2 == m % 2 else all(h) # №19 после ЛЮБОГО хода Пети


for s in range(1, 128 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m) == 1:
            print(s, m)
# отбор корней: для №19 второе число - 2, для №20 второе число - 3, для №21 второе число - 4

# №19 - 21 (две кучи)
def f(s1, s2, c, m): # s - знчение, с - номер хода, m - выигрышный ход
    if (s1 + s2) >= 77: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s1 + 1, s2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 + 1, c + 1, m), f(s1, s2 * 2, c + 1, m)] # ходы
    return any(h) if (c + 1) % 2 == m % 2 else any(h) # №19 после НЕУДАЧНОГО хода Пети


for s2 in range(1, 69 + 1):
    for m in range(1, 4 + 1):
        if f(7, s2, 0, m) == 1: # and m == 3
            print(s2, m)

# Нельзя повторять предыдущий ход (Поляков 4825)
def f(s, p, c, m):
    if s >= 43: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if p != '+1': h += [f(s + 1, '+1', c + 1, m)]
    if p != '+2': h += [f(s + 2, '+2', c + 1, m)]
    if p != '*2': h += [f(s * 2, '*2', c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 43):
    for m in range(1, 5):
        if f(s, '', 0, m) == 1:
            print(s, m)
            break

# Поляков 4827
def f(s, p, c, m):
    if s >= 55: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if p != '+1': h += [f(s + 1, '+1', c + 1, m)]
    if p != '+3': h += [f(s + 3, '+3', c + 1, m)]
    if p != '*2': h += [f(s * 2, '*2', c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 55):
    for m in range(1, 5): # зависит от количества ходов
        if f(s, '', 0, m) == 1:
            print(s, m)
            break

# Поляков 5872
def f(s, p0, p1, c, m): # p0 - предыдущий ход противника, p1 - наш предыдущий ход
    if s >= 121: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if p1 != '+5': h += [f(s + 5, '+5', p0, c + 1, m)]
    if p1 != '+2': h += [f(s + 2, '+2', p0, c + 1, m)]
    if p1 != '+12': h += [f(s + 12, '+12', p0, c + 1, m)]
    if p1 != '*2': h += [f(s * 2, '*2', p0, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 121):
    for m in range(1, 7):
        if f(s, '', '', 0, m) == 1:
            print(s, m)
            break'''

# 5885 КЕГЭ (19)
'''def f(s, m): # s - знчение, m - выигрышный ход
    if s == 42: return m % 2 == 0
    if m == 0: return 0
    if s < 42:
        h = [f(s + 1, m - 1), f(s + 3, m - 1), f(s + 7, m - 1)]
    elif s > 42:
        h = [f(s - 1, m - 1), f(s - 3, m - 1), f(s - 7, m - 1)] # ходы
    return any(h) if (m - 1) % 2 == 0 else any(h)


for s in range(1, 10000):
    if f(s,2): # Петя может выиграть за свой 2 ход, но не может за 1: if f(s,3) and not f(s, 2)
        print(s)'''

# Поляков 6833 (21)
def f(s, m):
    if s >= 37: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


for s in range(1, 100):
    if f(s, 4) and not f(s, 2):
        print(s)