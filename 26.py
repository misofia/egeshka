'''a = [int(x) for x in open('26_5228.txt')][1:]
a = sorted(a, reverse = True)
b = int(a[0])k = 1
for i in range(1, len(a)):
    if b - a[i] >= 8:
        b = a[i]
        k += 1
print(k, b)'''

'''c = 0
f = open('26_2686 (1).txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
for i in range(k - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 1 == a[i + 1][1]:
        c += 1
        if c >= 5:
            print(a[i][0], a[i][1] + 1)
    else:
        c = 0'''

# 3
f = open('26.txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
ans = [0,0]
for i in range(k - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 3 == a[i + 1][1]:
        r = a[i][0]
        s = a[i][1] + 1
        if r > ans[0]:
            ans[0] = r
            ans[1] = s
print(ans)

# 4
a = [int(x) for x in open('26 (1).txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if sr in a:
                ans.append(sr)
print(len(ans), max(ans))