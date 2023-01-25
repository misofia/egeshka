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