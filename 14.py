'''a = 5 ** 36 + 5 ** 24 - 25
a5 = ''
while a != 0:
    a5 += str(a % 5)
    a //= 5
a5 = a5[::-1]
print(a5.count('4'))'''
#x y
'''for x in '012345678':
    for y in '012345678':
        a = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if a % 61 == 0:
            print(a // 61)
            break'''
'''for p in range(7, 50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y * (p ** 2) + 4 * p + y) + (y * (p ** 2) + 6 * p + 5) == (x * (p ** 3) + z * (p ** 2) + 2 * p + 3):
                    print((x * (p ** 2) + y * p + z))'''

'''def f(x, a1, a2):
    return not((56 <= x <= 79) <= (63 <= x <= 85)) <= (not(63 <= x <= 85) <= (a1 <= x <= a2))
m = 70
for a1 in range(50, 90):
    for a2 in range(a1 + 1, 90):
        if all(f(x, a1, a2) == 1 for x in range(50, 90)):
            m = min(m, a2 - a1)

print(m//10)'''

# 21-система, 12yx9,21 + 36y99,21, y = 5, делить на 18
for x in range(21):
    t = [(1 * 21**4 + 2 * 21**3 + y * 21**2 + x * 21 + 9 +
           3 * 21**4 + 6 * 21**3 + y * 21**2 + 9 * 21 + 9) % 18 == 0
            for y in range(21)]
    if all(t):
        print((1 * 21**4 + 2 * 21**3 + 5 * 21**2 + x * 21 + 9 +
           3 * 21**4 + 6 * 21**3 + 5 * 21**2 + 9 * 21 + 9) // 18)
        break