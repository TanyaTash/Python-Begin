# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Запрашиваем число на вход
inputNumber = int(input("Enter a three-digit number: "))

# Разбиваем полученной число на отдельные числа
num1 = inputNumber // 100
num2 = (inputNumber // 10) % 10
num3 = inputNumber % 10

# Получаем сумму чисел
sum_of_digits = num1 + num2 + num3

print("The sum of digits of a three-digit number: ", sum_of_digits)
