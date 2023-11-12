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
