# ============================== DICTIONARY PROBLEMS ========================

# Basic Dictionary Operations-----------------------

student = {"name": "Alice", "age": 20, "grade": "B"}
student['city'] = 'New York'
student['age'] = '21'
print(f'{student} and Name : {student['name']}')


# Dictionary Operations -------------------------

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

car.pop('color')
print(car)
print(car.items())
print('brand' in car)
print('color' in car)


# Dictionary from Two Lists ---------------------

keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]

dictionary =dict(zip(keys,values))
print(dictionary)


# Clear Dictionary ------------------------

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

inventory.clear()
print(inventory)


# Merge Dictionaries ---------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)


# Access Nested Dictionary ------------------

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}

print(person['address']['city'])


# Access ‘history’ Key From a Nested Dictionary ----------------

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

print(student['grades']['history'])



#  Initialize Dictionary with Default Values -------------------

keys = ["math", "science", "english", "history"]
default = 0

dictionary = dict.fromkeys(keys,default)
print(dictionary)


# Rename a Key of Dictionary -----------------------

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee['first_name'] = employee.pop('fname')
print(employee)


#  Check Value Existence -------------------

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

print('editor' in roles.values())
print('manager' in roles.values())


#  Sum All Values--------------------

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

addition = sum(expenses.values())
print(addition)


# Map Two Lists (zip) ----------------

attributes = ["brand", "model", "year", "color"] ; details = ["Honda", "Civic", 2023, "silver"]

dictionary = dict(zip(attributes,details))
print(dictionary)