# 4987
'''for c1 in '0123456789':
    for c2 in '0123456789':
        a = int(f'1{c1}34567{c2}9')
        if a % 17 == 0:
            print(a, a // 17) # это легко, параша, едем дальше'''

# 4988
from fnmatch import *
for x in range(0, 10 ** 9 + 1, 169):
    if fnmatch(str(x), '123*4?5'):
        print(x, x // 169) # передать Максимке !!!!

