from itertools import *
s = 'ABCD'
for x in permutations(s, 3):
    a = ''.join(x)
    print(a)
