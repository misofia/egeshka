s = '8' * 68
while ('222' in s) or ('888' in s):
    if '222' in s:
        s = s.replace('222', '8', 1)
    elif '888' in s:
        s = s.replace('888', '2', 1)
print(s)

# задание с кореткой
s = '1' + '8' * 80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2')
    elif '288' in s:
        s = s.replace('288', '3')
    else:
        s = s.replace('3888', '1')
print(s)