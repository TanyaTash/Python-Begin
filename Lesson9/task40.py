# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd

# Считываем файл CSV с помощью pandas
data = pd.read_csv('california_housing_train.csv')

# Фильтруем записи, где количество людей (population) находится в диапазоне от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисляем среднюю стоимость дома (medianHouseValue) для отфильтрованных записей
average_house_value = filtered_data['medianHouseValue'].mean()

# Выводим результат
print(f"Средняя стоимость дома для количества людей от 0 до 500: {average_house_value}")
