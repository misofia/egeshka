dict() #создание словаря из нескольких элементов
sp = [[1, 'яблоко'], [2, 'груша']] #1, 2, 3 - ключи
sp.append([3, 'апельсин'])
my_dict = dict(sp)

'''print(my_dict.get(2)) #вывод элемента
print(my_dict[2])'''

my_dict[3] = 'мандарин' #переприсвоение
my_dict[4] = 'слива' #добавление элемента
my_dict.pop(1) #удаление элемента по ключу
my_dict.keys() #вывод ключей словаря
my_dict.values() #вывод значений
3 in my_dict #проверка на вхождение ключа в словарь

dict = {1: 'яблоко', 2: 'груша', 3: 'апельсин'}
sq = {x: x * x for x in range(6)} #создание словаря квадратов чисел