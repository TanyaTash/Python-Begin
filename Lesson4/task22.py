# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def find_common_elements(set1_size, set2_size):
    set1 = set()
    set2 = set()

    # Ввод элементов первого множества
    print("Введите элементы первого множества через пробел:")
    elements1 = input().split()
    if len(elements1) != set1_size:
        print("Количество элементов первого множества не соответствует заданному значению.")
        return

    for element in elements1:
        set1.add(int(element))

    # Ввод элементов второго множества
    print("Введите элементы второго множества через пробел:")
    elements2 = input().split()
    if len(elements2) != set2_size:
        print("Количество элементов второго множества не соответствует заданному значению.")
        return

    for element in elements2:
        set2.add(int(element))

    # Находим пересечение множеств
    common_elements = set1.intersection(set2)

    # Выводим отсортированные элементы без повторений
    sorted_common_elements = sorted(common_elements)
    for element in sorted_common_elements:
        print(element)

# Ввод количества элементов для двух множеств
set1_size = int(input("Введите количество элементов первого множества: "))
set2_size = int(input("Введите количество элементов второго множества: "))

# Вызов функции для нахождения общих элементов
find_common_elements(set1_size, set2_size)
