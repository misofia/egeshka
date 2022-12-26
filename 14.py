a = 5 ** 36 + 5 ** 24 - 25
a5 = ''
while a != 0:
    a5 += str(a % 5)
    a //= 5
a5 = a5[::-1]
print(a5.count('4'))