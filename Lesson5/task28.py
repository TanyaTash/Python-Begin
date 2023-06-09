# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def recurs(num1, num2):
    if num2 == 0:
        return num1
    elif num2 > 0:
        return recurs(num1 + 1, num2 - 1)
    else:
        return recurs(num1 - 1, num2 + 1)

# Ввод чисел пользователем
number1 = int(input("Введите первое неотрицательное число: "))
number2 = int(input("Введите второе неотрицательное число: "))

result = recurs(number1, number2)
print(result)
