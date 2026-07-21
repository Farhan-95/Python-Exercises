# ========================= Series Problems =======================

import pandas as pd
import numpy as np

# creating a series from list ----------------

list_num = [10,40,70,30,20]
series_num = pd.Series(list_num)
print(series_num[2])

# creating series from mixed list ----------------

mixed_list = [10, 'apple', 20, 'banana']
mixed_series = pd.Series(mixed_list,index = ['num1','fruit1','num2','fruit2'])
print(mixed_series['num2'])



# Series to List Conversion ------------------

series_num = pd.Series([10,40,70,30,20])
print(type(series_num))
list_num = list(series_num)
print(type(list_num))
print(type(series_num.tolist()))


# Series Arithmetic ---------------------

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

print(type(series1))
print(type(series2))

add = series1 + series2
print(add)

sub = series1 - series2
print(sub)

mul = series1 * series2
print(mul)

div = series1 / series2
print(div)



#  Series Comparison ----------------

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

print('Equall')
print(series1 == series2)

print('Greater than')
print(series1 > series2)

print('Less than')
print(series1 < series2)

print('Not equall')
print(series1 != series2)



# Dict to Series --------------------

dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
series = pd.Series(dict , name = 'Dict 2 Series')
print(series)


#  Array to Series --------------------

list = [10,20,30,40,50]
array = np.array(list)
print(type(array))
series = pd.Series(array)
print(type(series))


# Change Series DataType -------------------

list = [100 , 200 ,300.12 ,400]
series = pd.Series(list,name = 'float_converted',dtype = 'float')
print(series)


# DF Column to Series ---------------- 

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)

series = pd.Series(df['col1'])
print(series)


# Series to Array -----------------

list = ['100','200','python','300.12','400']
series = pd.Series(list)
array = np.array(series)
print(type(array))
print(array)