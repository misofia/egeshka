# Универсальный код
def f(x, a):
    return (x % 25 != 0) <= ((x % 19 == 0) <= (x % a != 0))


for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 100)):
        print(a)

# ОТРЕЗКИ
'''def f(x, a1, a2):
    return (a1 <= x <= a2) <= (430 <= x <= 490) or (440 <= x <= 530)

m = 0
for a1 in range(400, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(400, 600)):
            m = max(m, a2 - a1)

print(m//10)''' # всегда m//10

# треугольник
'''def t(n,m,k):
    return max(n,m,k) < n + m + k - max(n,m,k)
def f(A,x):
    return not (t(x,11,16) == ((not(max(x,5) > 10))) and  t(4,A,x))
for A in range(1000):
    if all (f(A,x) for x in range(1000)):
        print(A)'''
        
# ДЕЛЕНИЕ
for A in range(1, 500):
    flag = 0
    for x in range(1, 1000):
        if ((A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))) == 0:
            flag = 1
            break
    if flag == 0:
        print(A)

def d(n, m):
  return n % m == 0
for A in range(999, 0, -1):
  i = 0
  for x in range(1, 999):
    if ((not d(x,A)) <= (d(x,6) <= (not d(x,4)))):
      i = i + 1
  if (i == 998):
    print(A)

for A in range(1, 1000):
    i = 0
    for x in range(1, 1000):
        if (A % 3 == 0) and ((220 % x == 0) <= ((A % x != 0) <= (550 % x != 0))):
            i += 1
        if i == 999:
            print(A)

# КОНЬЮНКЦИЯ
for A in range(0,100,1):
  i = 0
  for x in range(0, 100):
    if ((x&25!=0) <= ((x&19 == 0) <= (x & A !=0))):
      i=  i  + 1
  if i == 100:
    print(A)

# ГРАФИКИ
for A in range(1000,-1,-1):
  i = 0
  for x in range(0, 100):
    for y in range(0, 100):
      if ((2*x+y)!=70) or (x < y) or (A < x):
        i+=1
  if i == 10000:
    print(A, i)
