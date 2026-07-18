# ===================== Set problems ===========================

# adding or removing items from set -----------------------

fruits = {"apple", "banana", "cherry"}
fruits.add('mango')
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.discard('grapes')
print(fruits)


# clear all the items from set ----------------------

colors = {"red", "green", "blue"}
colors.clear()
print(colors)


# finding the length of set ------------------------

animals = {"cat", "dog", "bird", "fish"}
print(len(animals))


# empty checking of set -------------------

data = set()
if(len(data) == 0):
    print('Set is empty')
else:
    print('Set is not empty')    


#  Union of Sets---------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union = set_a.union(set_b)
print(union)


# Intersection of Sets -------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection = set_a.intersection(set_b)
print(intersection)


# Difference of Sets via method ------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
diff = set_a.difference(set_b)
print(diff)



#  Difference of Sets via symbol -------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
diff = set_a - set_b
print(diff)


#  Symmetric Difference ---------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)


# finding the minmum or maximum vlaues -----------------

numbers = {42, 7, 19, 85, 3, 56}
min = min(numbers)
max = max(numbers)
print('min : ', min ,"max : ", max)


#  finding the sum of set items -----------------------

numbers = {10, 20, 30, 40, 50}
sum = sum(numbers)
print(sum)


# add the items of list in set ----------------------

fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango","apple"]
fruits.update(new_fruits)
print(fruits)


# Check Subset and Superset

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
subset = set_a.issubset(set_b)
superset = set_a.issuperset(set_b)
print('subset : ',subset)
print('superset : ',superset)

