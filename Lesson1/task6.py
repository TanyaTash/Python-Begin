# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket_number = input("Enter ticket number: ")

# Проверяем длину номера билета
if len(ticket_number) != 6:
    print("Incorrect ticket number")
else:
    # Разбиваем номер билета на цифры
    digits = [int(digit) for digit in ticket_number]

    # Вычисляем сумму первых трех цифр и сумму последних трех цифр
    sum_first_half = sum(digits[:3])
    sum_second_half = sum(digits[3:])

    # Проверяем счастливость билета
    if sum_first_half == sum_second_half:
        print("Yes! Congratulations! It's a lucky ticket!")
    else:
        print("No! You are out of luck, the ticket is not lucky")
