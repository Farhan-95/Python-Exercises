# =============== LIst Intermediate problems ==================

# extract middle elements -----------------------

List = [10, 20, 30, 40, 50, 60, 70]
middle_elements = List[2:5]
print(middle_elements)


#  swapping two elements in list -----------------

List = [23, 65, 19, 90]
print('before swapping : ',List)
List[0],List[2] = List[2],List[0]
print(List)


#  accessing the items from nested list -----------------------

nested_list = [[1, 2], [3, 4, 5], [6, 7]]
print(nested_list[1][2])


# checking list contain specific items -------------------------

Inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
print("Tablet" in Inventory)


#  count the occurance of item in a list and remove this item also ---------------------

List = [10, 20, 30, 10, 40, 10, 50]
print(List.count(10))
for x in List:
    if(x == 10):
        List.remove(x)
print(List)


