# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def recurs(num, step):
    if step == 0:
        return 1
    elif step > 0:
        return int(num * recurs(num, step - 1))
    else:
        return int(1 / (num * recurs(num, -step - 1)))

# Ввод чисел пользователем
base_number = float(input("Введите основание числа: "))
exponent_number = int(input("Введите показатель степени: "))

result = recurs(base_number, exponent_number)
print(result)
