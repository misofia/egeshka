#bin
'''for n in range(1, 1000):
    n2 = bin(n)[2:]
    s = int(n2.count('1')) % 2
    r = n2 + str(s)
    s2 = int(r.count('1')) % 2
    r2 = r + str(s2)
    if int(r2, 2) > 43:
        print(int(r2, 2))
        break'''

'''for n in range(256):
    s = bin(n)[2:]  
    s = str(s)
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2) 
    if r - n == 133:
        print(n)'''

'''a = [] 
for x in range(100, 3001):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))'''

#10
'''for n in range(1000, 10000):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])
    max1 = max(s1, s2, s3)
    mi = min(s1, s2, s3)
    max2 = (s1 + s2 + s3) - int(max1) - int(mi)
    m = str(max2) + str(max1)
    if m == '1517':
        print(n)'''

'''for n in range(1000, 10000):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])
    ma = max(s1, s2, s3)
    sr = (s1 + s2 + s3) - int(ma) - int(min(s1, s2, s3))
    s = str(sr) + str(ma)
    if s == '613':
        print(n)'''

# троичная
def f(x):
    x3 = ''
    while x != 0:
        x3 += str(x % 3)
        x //= 3
    return x3[::-1]


for n in range(1, 1000):
    if n % 3 == 0:
        r = '1' + f(n) + '02'
    else:
        r = f(n) + f((n % 3) * 4)
    if int(r, 3) < 199:
        print(n)