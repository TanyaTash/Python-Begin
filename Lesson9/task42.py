# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

# Считываем файл CSV с помощью pandas
data = pd.read_csv('california_housing_train.csv')

# Находим минимальное значение population
min_population = data['population'].min()

# Фильтруем записи, где population равно минимальному значению
filtered_data = data[data['population'] == min_population]

# Находим максимальное количество households в отфильтрованных записях
max_households = filtered_data['households'].max()

# Выводим результат
print(f"Максимальное количество households в зоне с минимальным значением population: {max_households}")
