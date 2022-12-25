for n in range(1, 1000):
    n2 = bin(n)[2:]
    s = int(n2.count('1')) % 2
    r = n2 + str(s)
    s2 = int(r.count('1')) % 2
    r2 = r + str(s2)
    if int(r2, 2) > 43:
        print(int(r2, 2))
        break