# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(array, min_value, max_value):
    indexes = []
    for index, element in enumerate(array):
        if min_value <= element <= max_value:
            indexes.append(index)
    return indexes

# Ввод данных пользователем
input_array = input("Введите элементы массива через пробел: ").split()
array = [int(element) for element in input_array]
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

result = find_indexes(array, min_value, max_value)
print(result)
