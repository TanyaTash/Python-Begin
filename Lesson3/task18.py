# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

# Функция для поиска ближайшего элемента к заданному числу
def find_closest_element(array, target):
    closest_element = None
    min_difference = float('inf')

    for num in array:
        difference = abs(num - target)
        if difference < min_difference:
            min_difference = difference
            closest_element = num

    return closest_element

# Ввод количества элементов в массиве
num_elements = int(input("Введите число элементов в массиве: "))

# Ввод массива чисел
array = list(map(int, input("Введите элементы массива через пробел: ").split()))

# Проверка, что количество элементов в массиве array равно num_elements
if len(array) != num_elements:
    print("Количество элементов в массиве не соответствует заданному числу количества элементов массива")
else:
    # Ввод числа target
    target = int(input("Введите число для поиска ближайшего числа: "))

    # Поиск ближайшего элемента к числу target
    closest_element = find_closest_element(array, target)

    # Вывод результата
    print("Ближайшее число к " + str(target) + " в массиве = " + str(closest_element))
