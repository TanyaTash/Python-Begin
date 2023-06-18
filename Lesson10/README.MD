### Урок 10. Построение графиков ###
#### <span style="color:#8B0000">Задача 44:</span> В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies? ####

*__Пример:__*
import random  
lst = ['robot'] * 10  
lst += ['human'] * 10  
random.shuffle(lst)  
data = pd.DataFrame({'whoAmI'lst})  
data.head()   

