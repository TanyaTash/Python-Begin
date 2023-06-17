# Задача 38: Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находитьсяв файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import os

def import_data(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                contact = line.strip().split(',')
                contacts.append(contact)
    return contacts

def export_data(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = [surname, name, patronymic, phone]
    contacts.append(contact)
    print("Контакт добавлен.")

def search_contact(contacts):
    search_term = input("Введите имя или фамилию для поиска: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in [c.lower() for c in contact[:3]]:
            found_contacts.append(contact)
    return found_contacts

def update_contact(contacts):
    found_contacts = search_contact(contacts)
    if len(found_contacts) == 0:
        print("Контакты не найдены.")
        return
    print("Найденные контакты:")
    for i, contact in enumerate(found_contacts):
        print(f"{i+1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")
    choice = input("Введите номер контакта, который нужно обновить: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(found_contacts):
        print("Некорректный выбор.")
        return
    contact = found_contacts[int(choice) - 1]
    print("Введите новые данные:")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    phone = input("Номер телефона: ")
    contact[0] = surname
    contact[1] = name
    contact[2] = patronymic
    contact[3] = phone
    print("Контакт обновлен.")

def delete_contact(contacts):
    found_contacts = search_contact(contacts)
    if len(found_contacts) == 0:
        print("Контакты не найдены.")
        return
    print("Найденные контакты:")
    for i, contact in enumerate(found_contacts):
        print(f"{i+1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")
    choice = input("Введите номер контакта, который нужно удалить: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(found_contacts):
        print("Некорректный выбор.")
        return
    contact = found_contacts[int(choice) - 1]
    contacts.remove(contact)
    print("Контакт удален.")

def display_contacts(contacts):
    if len(contacts) == 0:
        print("Справочник пуст.")
    else:
        print("Контакты:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")

def main():
    filename = 'contacts.txt'
    contacts = import_data(filename)

    while True:
        print("\nМеню:")
        print("1. Вывести контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Обновить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            found_contacts = search_contact(contacts)
            if len(found_contacts) == 0:
                print("Контакты не найдены.")
            else:
                print("Найденные контакты:")
                for i, contact in enumerate(found_contacts):
                    print(f"{i+1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            export_data(filename, contacts)
            print("Данные сохранены.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
