'''a = [int(x) for x in open('26_5228.txt')][1:]
a = sorted(a, reverse = True) # по убыванию
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
'''f = open('26.txt')
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
print(ans)'''

# 4
'''a = [int(x) for x in open('26 (1).txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if sr in a:
                ans.append(sr)
print(len(ans), max(ans))'''

# 5228 КЕГЭ (1)
'''a = [int(x) for x in open('26_5228 (1).txt')][1:]
a = sorted(a) # по возрастанию
# b = a[0]
for j in range(0, 100):
    k = 1
    b = a[j]
    for i in range(1, len(a)):
        if a[i] - b >= 8:
            b = a[i]
            k += 1
print(k)'''

# (2)
'''a = [int(x) for x in open('26_5228 (1).txt')][1:]
a = sorted(a, reverse = True) # по убыванию
print(a)
b = a[0]
k = 1
for i in range(1, len(a)):
    if b - a[i] >= 8:
        b = a[i]
        k += 1
print(k, b)'''

# 10726 КЕГЭ
'''a = open('26_10726 (1).txt')
n = int(a.readline()) # 1 строка - количество пар
s = [list(map(int, x.split())) for x in a]
mn = [0] * 44641 # вообще максимальное значение числа
for i in range(n):
    a, b = s[i][0], s[i][1]
    for j in range(a, b):
        mn[j] = 1
print(sum(mn))
s1 = ''.join(map(str, mn)) # как в 24 задании искать максимальную последовательность единиц
s1 = s1.split('0')
print(len(max(s1, key = len)))'''

# КЕГЭ №12933
'''f = open('26_12933.txt')
n, k = [int(x) for x in f.readline().split()] # прочитали и разредали, получили 2 строчки состоящие из цифр
a = []
for i in range(1, n + 1): # n - кол-во иттераций; перебором захватываем всё
    ts, to = [int(x) for x in f.readline().split()] # ts - время шлифовки, to - время окрашивания
    a.append((ts, i, 's')) # делаем картежи s - шлифовка, o - окрашивание
    a.append((to, i, 'o'))
a.sort() # время по возврастанию
lenta = [0] * (n + 1) # метод для выведения по номеру места, создание ленты
ks = 0 # кол-во отшлифованных деталей
spo = set() # создаём множество окрашнных деталей
start, end = 1, n # start - первое место на ленте, end - последнее место на ленте
for t, id, op in a: # t - время , id - айди, op - операция
    if id not in spo: # проверили есть ли деталь
        spo.add(id) # добавляет окрашенные детали
        if op == 's': # если деталь для шлифовки
            lenta[start] = id # ставим этот элемент в начало ленты
            start += 1
            ks += 1
        else: # если деталь для окрашивания
            lenta[end] = id # ставим этот элемент в конец ленты
            end -= 1 # -= потому что идём с конца
print(ks, lenta[k])'''

# КЕГЭ №13101
'''f = open('26_13101.txt')
n = int(f.readline())
a = []
for i in f:
    st, t, o =  [int(x) for x in i.split()] # st - начало время обслуживания, t - время обслуживания, o - окно
    a.append((st, t, o)) # создаём картеж
a.sort()
okno1 = [] # первая очередь
okno2 = [] # вторая очередь
kn = 0 # счёчтик необслуженных
k2 = 0 # счётчик второго окна
for st, t, o in a:
    okno1 = [x for x in okno1 if x > st]
    okno2 = [x for x in okno2 if x > st]
    if o == 1 or (o == 0 and len(okno1) <= len(okno2)):
        if len(okno1) >= 14:
            kn += 1
            continue
        if len(okno1) == 0:
            okno1 += [st + t]
        else:
            okno1 += [max(okno1) + t]
    else:
        if len(okno2) >= 14:
            kn += 1
            continue
        k2 += 1
        if len(okno2) == 0:
            okno2 += [st + t]
        else:
            okno2 += [max(okno2) + t]
print(k2, kn)'''

# 12478 КЕГЭ
f = open('26_12478.txt')
n = f.readline()
st_ege = 1000
end_ege = 18000
rab = []
a = []
for i in f:
    st, end =  [int(x) for x in i.split()] # st - начало время обслуживания, end - окончание обслуживания
    a.append((st, end)) # создаём картеж
a.sort()
for i in range(len(a)):
    if a[i][1] <= st_ege:
        continue
    else:
        if a[i][0] <= st_ege and a[i + 1][0] <= a[i][1]:
            rab += [a[i][1] - a[i][0]]
print(len(rab))
