# -------Take input from user name,age, and address from use and print it in new line------

name  = input('Enter your name : ')
age  = int(input('Enter your age : '))
address  = input('Enter your address : ')

print(f'Hello!Farhan{name}, I know you are  {age} years old, and lived in {address}')



# -------Swapping variables values---------

# program 1

brother1 = 'Sulman Kareem'
brother2 = 'Rehman Kareem'
temp = brother1
brother1 = brother2
brother2 = temp
print(brother1)
print(brother2)

# program 2

num1 = 23
num2 = 20
num1,num2 = num2,num1
print(num1)
print(num2)


# -------Type Casting------

# float to int or then int to float 

float_num = 123.005
print('before conversion : ', type(float_num),float_num)
after_conversion = int(float_num)
print('After conversion type : ', type(after_conversion),after_conversion)
reverse_conversion = float(after_conversion)
print('Now convert back to float : ',type(reverse_conversion),reverse_conversion)


# int to string 
num = 1235
print('before conversion : ', type(num),num)
StringTypeConversion = str(num)
print('after conversion : ',type(StringTypeConversion),StringTypeConversion)



# ------Arithmatic Operator problems----------

# For two integer numbers

intNum1 = 23456
intNum2 = 87060
print(intNum1 + intNum2)
print(intNum1 - intNum2)
print(intNum1 * intNum2)
print(intNum1 / intNum2)

# For two float numbers

floatNum1 = 2345.0055
floatNum2 = 596845.33332
sum = floatNum1 + floatNum2
sub = floatNum1 - floatNum2
multiplication = floatNum1 * floatNum2
division = floatNum1 / floatNum2
print(sum)
print(sub)
print(multiplication)
print(division)

# Addition of String

firstName = 'Muhammad'
middleName = 'Farhan'
lastName = 'Kareem'
fullName = firstName + " " + middleName + " " + lastName
print(fullName)



# -----------KiloMeter to Meter Converter--------------

KiloMeter = int(input("Enter the Kilometers to convert it into meters : "))
meter = KiloMeter *1000
print(f'There are {meter}m in {KiloMeter}KM.')


# ---------- Fahrenheit to celcius temp conversion ----------

fahrenheit = float(input('Enter the temprature in fahrenheit : '))
celcius = 5/9 * (fahrenheit - 32)
print(celcius)


# -----------Escape characters practice ---------------

print('Muhammad\nFarhan\nKareem')
print('Abdull\tKareem')
print('Abdull \bKareem')
print('\'Abdull\',\'Kareem\'')