import os
clear = lambda: os.system('clear')
clear()
import pandas as pd
import random

lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.get_dummies(data['whoAmI'])
data = data.join(one_hot_data)
data = data.drop('whoAmI', axis=1)
print(data.head())