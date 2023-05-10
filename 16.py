# Поляков 224
'''def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 == 0: return n * n + f(n - 1)
    if n > 1 and n % 2 != 0: return f(n - 1) + 2 * f(n - 2)


print(f(23))'''
# 8 800 5 5 5 3 5 3 5 лучше позвоните нам чем у кого то занимать

# Поляков 226
'''def f(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) - 2 * g(n - 1)


def g(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) + 2 * g(n - 1)


print(g(21))'''

# Поляков 5537
'''from sys import *
setrecursionlimit(10000)


def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1)


print(f(2023)/f(2020))'''
# 2021 * 2022 * 2023

# досрок 2023
'''def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n + 2)


print(f(2022) - f(2023))  # соня лучшая'''

# Номер 3691

'''def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return 3 + f((n / 2) - 1)
    if n > 1 and n % 2 != 0: return n + f(n + 2)
n = 2
while n < 1000:
    try:
        r = f(n)
        if r == 19:
            print(n)
            break
    except:
        pass
    n += 1'''