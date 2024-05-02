#8
'''from itertools import product
c = 0
for x in product('ЛЕТО', repeat = 4):
    s = ''.join(x)
    if s[0] == 'Л' or s[0] == 'Т':
        c += 1
print(c)'''

'''from itertools import product
c = 0
for x in product('АКРУ', repeat = 5):
    s = ''.join(x)
    c += 1
    if c == 350:
        print(s)
        break'''

# ЕГКР
# 1
'''from itertools import *
k = 0
for i in product('0123456', repeat=6):
    s = ''.join(i)
    if s[0] != '0' and s.count('3') == 1:
        s = s.replace('3', '1').replace('5', '1')
        if '11' not in s:
            k += 1
print(k)'''

# 2
from itertools import *
k = 0
for i in product('0123456', repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('0') + s.count('2') + s.count('4') + s.count('6') == 2:
            k += 1
print(k)