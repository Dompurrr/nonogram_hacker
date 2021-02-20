#Начало блока ввода из файла
f = open('input.txt', 'r')
a = f.readline()
#Количество столбцов
ylines = int((a.split())[1])
#количество строк
xlines = int((a.split())[0])
#Листы со значениями столбиков и столбцов, где индекс (начиная с 0) соответствует строке/столбцу
x_list = []
y_list = []
for i in range(xlines):
    x_list.append([])
for i in range(ylines):
    y_list.append([])
for i in range(ylines):
    y_list[i] = (f.readline()).split()
for i in range(xlines):
    x_list[i] = (f.readline()).split()
#Конец блока ввода из файла
#Начало блока вычислений
