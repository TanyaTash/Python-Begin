'''
Задание 44
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |

'''


import random
import pandas as pd

categories = ['robot'] * 10
categories += ['human'] * 10
random.shuffle(categories)
data = pd.DataFrame({'category': categories})

# Преобразуем столбец 'category' в one-hot вид
one_hot_data = pd.get_dummies(data['category'], prefix='category')

# Объединяем one-hot данные с исходным DataFrame
data = pd.concat([data, one_hot_data], axis=1)

data.head()
