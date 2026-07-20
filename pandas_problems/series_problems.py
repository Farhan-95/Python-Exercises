# ========================= Series Problems =======================

import pandas as pd

# creating a series from list ----------------

list_num = [10,40,70,30,20]
series_num = pd.Series(list_num)
print(series_num[2])

# creating series from mixed list ----------------

mixed_list = [10, 'apple', 20, 'banana']
mixed_series = pd.Series(mixed_list,index = ['num1','fruit1','num2','fruit2'])
print(mixed_series['num2'])



# 