# f = open('24.txt', 'w')
# # работа с файлом
# f.close()

# чтение файла в строки
'''s = open('24_1.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
s = s.split()
print(len(max(s, key = len)))

# чтение, создание списка, в целочисленный вид
# a = [int(x) for x in open('17.txt')]

# длина строки
a = open('24_demo.txt').readline()
m = 0
k = 1
for i in range(len(a)):
    if a[i] != a[i - 1]:
        k += 1
    else:
        m = max(k, m)
        k = 1
m = max(k, m)
print(m)

# поляков
s = open('24-253.txt').readline()
gl = 'AO'
sgl = 'CDF'
m = 0
k = 1
for i in range(2, len(s), 3):
    if s[i - 2] in sgl and s[i] in gl:
        k += 1
    else:
        m = max(k, m)
        k = 1
m = max(k, m)
print(m)'''

# не более одной "А"
'''a = open('24.txt').readline()
m = 0
c1 = c2 = 0
for i in a:
    if i != 'A':
        c2 += 1
    else:
        m = max(m, c1 + c2 + 1)
        c1 = c2
        c2 = 0
m = max(m, c1 + c2 + 1)
print(m)'''

# 7200
'''a = open('24-280.txt').readline()
s = a.replace('X', 'X ').replace('Y', 'Y ').split('A')
k = 1
m = 0
for i in range(0, len(s) - 1):
    k += len(s[i])
    m = max(m, k)
    k = 1
print(m)
if s[i].count('X') == 1 and s[i].count('Y') == 1:
        k += len(s[i])
    else:
        m = max(m, k)
        k = 1
print(m)'''

# 7200
a = open('24-280.txt').readline()
a = a.replace('X', 'X ').replace('Y', 'Y ').split(' ')
m = 0
for i in range(len(a)-2):
    c = a[i] + a[i+1] + a[i+2][:-1]
    if c.count('X') == 1 and c.count('Y') == 1 and c.count('A') == 0:
        m = max(m, len(c))
print(m)

# 7196
a = open('24-280.txt').readline()
c = 1
k = 0
m = 0
for i in range(len(a) - 1):
    c += 1
    if a[i] == 'X' or a[i] == 'Y':
        k += 1
    if k > 10:
        m = max(c, m)
        k = 0
        c = 1
print(m)

# 6058
a = open('24-247.txt').readlines()
m = -1
m_all = -1
k = 1
for s in a:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k += 1
            if k > m:
                m = k
                m_all = s.count(s[i])
            if k == m:
                m_all = max(s.count(s[i]), m_all)
        else:
            k = 1
print(m_all)
