# 4312
'''a = [int(x) for x in open('17-4.txt')]
c = 0
m = 10001
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        c += 1
        m = min(m, a[i])
print(c, m)

a = [int(x) for x in open('17-4.txt')]
ans = []
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        ans.append(a[i])
print(len(ans), min(ans))

# 4316
a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    s = sum(list(map(int, str(i))))
    if (s % 5 == 0) and (i % 3 ** 2 != 0):
        ans.append(i)
print(len(ans), max(ans))'''

# 4311
a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    if (i % 13 == 4) and (i % 8 == 1):
        ans.append(i)
print(max(ans), sum(ans))

