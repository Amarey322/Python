# -*- coding: utf-8 -*-

import pandas as pd

# Исходный код
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца 'whoAmI', если нужно
data = data.drop('whoAmI', axis=1)

# Вывод результата
print(data.head())