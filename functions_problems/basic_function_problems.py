# ===================== Function Problems ==========================

# Create a Function with Parameters---------------------------

def demo(name,age):
    print(f'name : {name} age : {age}')

demo('Farhan',23)


# Variable Length of Arguments (*args) ---------------------

def func1(*number):
    print(number)

func1(20,50.60,45)    
func1(50.60,90)   


# Return Multiple Values from a Function -------------------

def calculation(num1 , num2):
    sum = num1 + num2
    sub = num1 - num2
    return sum,sub

addition,substraction = calculation(30,20)
print(addition,substraction)



# Function with Default Argument ------------------------

def show_employee(name,salary = 9000):
    print(f'Name : {name} Salary : {salary}')

show_employee('Sania' , 12000)
show_employee('Farhan' )


#  Create an Inner Function ------------------------

def outer_function(a,b):
    def inner_function(a,b):
        return a+b
    final_result = inner_function(a,b)
    return final_result

result = outer_function(700,300)
print(result)


# Generate a List of Even Numbers (Range Function)----------------

def even_generation(starting = 0, ending = 20):
    start = starting
    end = ending
    even = []
    
    for i in range(start , end + 1):
        if i % 2 == 0 :
          even.append(i)

    return even      

output = even_generation(5,25)
print(output)


# Find the Largest Item in a List ----------------

def largest_num(num_list):
    maximum = max(num_list)
    return maximum

x = [4, 6, 8, 24, 12, 2]
answer = largest_num(x)
print(answer)


# Call Function using Positional and Keyword Arguments ----------------------

def describe_pet(animal_type, pet_name):
    print(animal_type,pet_name)

describe_pet('hamster','Harry')    
describe_pet(animal_type = 'dog',pet_name ='Willie')    


# Create a Function with Keyword Arguments ------------------

def print_info(**kwargs):
    for  key ,value in kwargs.items():
        print(f"{key} : {value}")


print_info(name="Alice", age=30, city="New York")        



# Modifying Global Variables -----------------------------------

global_var = 10

def value_changing(value):
    global global_var
    global_var = value

print(f'Initaial : {global_var}')   
value_changing(30) 
print(f'Modified : {global_var}')    


#  Recursive Factorial (Non-Negative Integers) --------------------

def rec_factorial(n):
    if n <= 1:
        return 1
    else :
        return n * rec_factorial(n - 1)
    
num =  int(input("Enter a number to find it's factorial : "))
factorial = rec_factorial(num)
print(factorial)



# Create a Recursive Function ----------------------------

def addition(n):
    if(n <= 1):
        return 1
    else:
        return n + addition(n-1)
    
num =  int(input("Enter a number to find it's factoial addition : "))
sum = addition(num)
print(sum)    