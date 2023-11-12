# №1
'''print(hex(int(int('1011', 2) + 0.25 + int('24', 8) + 0.75)))''' # целая часть переводится кодом, дробная - вручную

# №2
'''def f(a, b, c):
    return a or not b and c


for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, int(f(a, b, c)))'''

# №4
'''for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        r1 = n2 + '10'
    else:
        r1 = n2 + '11'
    if r1.count('1') % 2 == 0:
        r = r1 + r1[-1]
    else:
        r = r1 + r1[-2]
    if int(r, 2) > 44:
        print(n, r)'''

# №8
'''p = 5
q = 7
e = 11
for d in range(40):
    f = (p - 1) * (q - 1)
    if (d * e) % f == 1:
        print(d)'''

# №10
'''print((~18 | (132 >> 2)) & (86 << 1))'''

# №11
'''def f(c, e):
    if c > e or c == 32: return 0
    if c == e: return 1
    if c < e: return f(c + 3, e) + f(c + 4, e) + f(c * 3, e)


print(f(4, 16) * f(16, 46))'''

# №12
'''k = 0
for i in range(0, 100, 2):
    s = i
    n = 120
    while s > 0:
        s = s // 6
        n = n - 6
    if n == 108:
        k += 1
print(k)'''

# №13
'''ans = []
a = [int(x) for x in open('13.txt')]
for i in range(len(a) - 1):
    if a[i] % 8 == 0 and a[i + 1] % 8 == 0:
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))'''

# №5
'''import struct
def float_to_bin(num):
   bits, = struct.unpack('!I', struct.pack('!f', num))
   return "{:032b}".format(bits)
print(hex(int(float_to_bin(-14.75),2)))'''
