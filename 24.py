# f = open('24.txt', 'w')
# # работа с файлом
# f.close()

# чтение файла в строки
s = open('24_1.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
s = s.split()
print(len(max(s, key = len)))

# чтение, создание списка, в целочисленный вид
# a = [int(x) for x in open('17.txt')]

# длина строки
a = open('24_demo.txt').readline()
m = 0
k = 1
for i in range(len(a)):
    if a[i] != a[i - 1]:
        k += 1
    else:
        m = max(k, m)
        k = 1
m = max(k, m)
print(m)
