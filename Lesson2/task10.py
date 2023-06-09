# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Enter the number of coins (n): "))  # Ввод количества монеток
count_tail = 0  # Счетчик монеток решкой вниз
count_head = 0  # Счетчик монеток гербом вниз

for i in range(n):
    x = None
    while x not in (0, 1):  # Проверка, что вводится только 0 или 1
        x = int(input("Enter the state of the coin " + str(i + 1) + " (0 - tail, 1 - head): "))  # Ввод состояния монетки (0 - решка, 1 - герб)
    if x == 0:
        count_tail += 1  # Увеличение счетчика монеток решкой вниз
    else:
        count_head += 1  # Увеличение счетчика монеток гербом вниз

if count_head > count_tail:
    print("Minimum number of coins to flip: " + str(count_tail))  # Вывод минимального количества монеток, которые нужно перевернуть (решка)
else:
    print("Minimum number of coins to flip: " + str(count_head))  # Вывод минимального количества монеток, которые нужно перевернуть (герб)
