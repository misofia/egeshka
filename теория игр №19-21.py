# №19 - 21 (одна куча)
def f(s, c, m): # s - знчение, с - номер хода, m - выигрышный ход
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