import os
clear = lambda: os.system('clear')
clear()
import pandas as pd
import random

lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data['human'] = (data['whoAmI'] == 'human').astype(int)
data['robot'] = (data['whoAmI'] != 'human').astype(int)
print(data.head())
