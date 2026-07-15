# ======================== Tuples Problems ===============================

# tuple first and last item accessing with its length --------------------

fruits = ("apple", "banana", "cherry", "date")
print(fruits[0])
print(fruits[-1])
print(len(fruits))


# creating tuple with its type printing --------------------

tuple_creation = (50,)
print(type(tuple_creation))



# tuple repetation -------------------------------

colors = ("red", "green")
new_colors = colors * 3
print(new_colors)


# tuple concatination ---------------------------

a = (1, 2)
b = (3, 4)
c = (5, 6)
ans = a + b + c
print(ans)



# tuple slicing ------------------------------

numbers = (10, 20, 30, 40, 50, 60, 70)
print(numbers[2:5])


# tuple reversal ----------------------------

items = (1, 2, 3, 4, 5)
print(items[::-1])


# type casting in tuples ---------------------

my_list = [10, 20, 30, 40, 50]
tuple_conv = tuple(my_list)
print(type(tuple_conv))


# tuple  to string ---------------------

chars = ('a', 'b', 'c')
result = "".join(chars)
print(result)


# tuple membership testing -------------------------

fruits = ("apple", "banana", "cherry", "date")
print("banana" in fruits)
print("mango" in fruits)


# counting of tuple items ------------------------

votes = ("yes", "no", "yes", "yes", "no", "yes")
print(votes.count('yes'))
print(votes.count('no'))


# unpack the tuple --------------------------

person = ("Alice", 30, "Engineer", "Pune")
(name , age , job , city) = person
print(f'name : {name} job : {job} age : {age} city : {city}')


# nested tuple access ---------------------------

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(matrix[1][2])


# finding the statistics of tuple items ------------------

scores = (88, 95, 70, 62, 99, 74, 85)
sum = sum(scores)
min = min(scores)
max = max(scores)
avg = sum / len(scores)
print(sum , min , max , avg)


# sorting in tuple ---------------------

numbers = (3, 14, 7, 22, 9, 41, 18, 5)
sorted_list= []
for x in numbers:
    if x > 10:
        sorted_list.append(x)
sorted_tuple = tuple(sorted_list)
print(sorted_tuple , type(sorted_tuple))      


# the modification hack ------------------

colours = ("red", "green", "blue")
colours_list = list(colours)
colours_list[1] = 'yellow'
colours = tuple(colours_list)
print(colours)


# tuple mutability -----------------------

t = (1, 2, [3, 4, 5])
t[2].append(99)
print(t)



