"""from fnmatch import *

for x in range(0, 10 ** 8 + 1, 1991):
    if fnmatch(str(x), '3?1*57'):
        print(x, x // 1991)"""
# 30117857 15127
# 31113357 15627
# 32108857 16127
# 33104357 16627

'''f = open('26.txt')
a, b = f.readline().split()
d = []
s = 0
count = 0
for i in f:
    if 210 <= int(i) <= 220:
        s += int(i)
        count += 1
    else:
        d.append(int(i))
d.sort()
d2 = []
i = 0
while sum(d2) + d[i] <= int(b) - s:
    count += 1
    d2.append(d[i])
    i += 1
k = len(d) - 1
while i > 0:
    while k >= 0:
        if sum(d2) - d2[i-1] + d[k] <= int(b) - s and d[k] != 0:
            d2[i-1] = d[k]
            d[k] = 0
            i -= 1
            break
        else:
            k -= 1
s += sum(d2)
print(count, s)'''
# 122 10000
"""f = open('1_24.txt')
s = f.readline()
minimal = 10 ** 10
cnt = 0
pos = []
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'TT':
        pos.append(i)
for j in range(0, len(pos) - 149):
    cnt = pos[j + 149] - pos[j] + 2
    if cnt < minimal:
        minimal = cnt
print(minimal)"""
# 195560
f = open("107_27_B.txt")
n = int(f.readline())
elems = [0 for i in range(n)]
answers = [0 for i in range(n)]
sum = 0
rightSum = 0
leftSum = 0
for i in range(0, n):
    elems[i] = int(f.readline())
for i in range(0, n):
    elems[i] = elems[i] * 3
for i in range(1, n // 2):
    sum = sum + elems[i] * i + elems[n - i] * i
    rightSum = rightSum + elems[i]
    leftSum = leftSum + elems[n - i]
sum = sum + elems[n // 2] * n // 2
answers[0] = sum
for i in range(1, n):
    answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + (n // 2) - 1) % n]
    rightSum = rightSum - elems[i] + elems[(i + (n // 2) - 1) % n]
    leftSum = leftSum - elems[(i + (n // 2)) % n] + elems[i - 1]
print(min(answers))