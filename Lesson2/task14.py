# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter the number N: "))  # Ввод числа N
i = 0  # Инициализация счетчика степени двойки

print("All integer degrees of two not exceeding N:")
while 2 ** i <= n:  # Проверка условия, пока 2 в степени i не превосходит N
    print(2 ** i)  # Вывод текущей степени двойки
    i += 1  # Увеличение счетчика