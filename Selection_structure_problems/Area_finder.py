#  This is the program to find the area of square , circle, rectangle or area of triangle

print('You have to enter a number to find the area \n 1 for area fo square \n 2 for area of circle \n 3 for area of rectangle \n area of triangle')
choosen_value = int(input('Enter a number : '))

if(choosen_value == 1):
    length = float(input('Enter the side length of square : '))
    area = length * length   # we can also write it like length ** 2
    print(f'The are of square is {area}')

elif(choosen_value == 2):
    radius = float(input('Enter the radius of circle : '))
    PI = 3.14
    area =  PI * radius**2   # we can also write it like radius * radius
    print(f'The are of circle is {area}')

elif(choosen_value == 3):
    length = float( input('Enter the length of rectangle : '))
    width = float( input('Enter the width of rectangle : '))
    area = length * width 
    print(f'The area of rectangle is {area}')

elif(choosen_value == 4):
    base = float(input('Enter the base of triagnle : '))
    height = float(input('Enter the height of trainagle : '))
    area  = 1/2 * (height * base)
    print(f'The area of traiangle is {area}')

else:
    print('Sorry! You enter a wrong number. ')    