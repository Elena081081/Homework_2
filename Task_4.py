# 4. Реализуйте алгоритм перемешивания списка, без использования встроеных
# методов (особенно SHUFFLE, без него)
# можно (нужно) использовать библиотеку Random

import random
from tempfile import tempdir

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = list1[:]
for i in range(len(list2)):
    index = random.randint(0, len(list2) - 1)
    temp = list2[i]
    list2[i] = list2[index]
    list2[index] = temp
print('Исходный список:', list1)
print('Новый список:', list2)
