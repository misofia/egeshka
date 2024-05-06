from itertools import *
c = 0
for x in product('АОУ', repeat=5):
    s = ''.join(x)
    c += 1
    if c == 210:
        print(s)