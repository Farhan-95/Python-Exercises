# ----------------day state according to its temperataure----------------------

day = input('Enter the name of day : ')
temperature = int(input('Enter the temperature of today : '))
         
if   temperature > 30 and temperature < 50 :
     print(f'{day} is hot day.')
elif temperature > 20 and temperature < 30:
     print(f'{day} is a pleasant day.')
elif temperature > 10 and temperature < 20:
     print(f'{day} is cool day.')
elif temperature < 10 and temperature > -10:
     print(f'{day} is cold day.')
else:
     print('The enter temperature is very extreme which is not possible for now.')



# ------------------grade check for board exams---------------------

num = int(input('Enter your marks : '))
percentage = (num/1100)*100
if (percentage >= 80):
    print('Congratulation! you have A+ grade.')
elif (percentage >= 70 and percentage <80):
    print('Congratulation! you have A grade.')
elif (percentage >= 60 and percentage <70):
    print('Congratulation! you have B grade.')
elif (percentage >= 50 and percentage <60):
    print('Congratulation! you have C grade.')
elif (percentage >= 40 and percentage <50):
    print('Congratulation! you have D grade.')
elif (percentage >= 33 and percentage <40):
    print('Congratulation! you have E grade.')
else:
    print('Sorry! you are fail , Try again.')



#---------------vowels characters checking---------------------

char = input('Enter a character. : ')
if ( char == 'a' or char == 'A'):
    print ( char , 'is the vowel.')    
elif ( char == 'e' or char == 'E'):
    print ( char , 'is the vowel.')
elif ( char == 'i' or char == 'I'):
    print ( char , 'is the vowel.')
elif ( char == 'o' or char == 'O'):
    print ( char , 'is the vowel.')
elif ( char == 'u' or char == 'U'):
    print ( char , 'is the vowel.')
else:
    print ( char , 'is the constant.')



#-----------------   state telling    ------------------

state = input('Enter the state of telephone line \n press w for working or \n press d for dead : ')

if state == 'w' or state == 'W' :
    print('The state of telephone line is working.')
elif state == 'd' or state == 'D' :
    print('The state of telephone is dead.')
else :
    print('Invalid Entery! try again.')    


# ------------------ user choice problem -----------------------

choice = int(input(''' Enter 1 for addition 
2 for substraction
3 for multiplication
4 for division(elif you choose division then 1st
number is greater then 2nd number.'''))
num1 = int(input('Enter your first number. : '))
num2 = int(input('Enter your second number. : '))
if (choice == 1):
    print(f'{num1+num2} is the addition of your given values.')
elif (choice == 2):
    print(f'{num1-num2} is the substraction of your given values.')
elif (choice == 3):
    print(f'{num1*num2} is the multiplication of your given values.')
elif (choice == 4):
    if (num1 >num2):
      print(f'{num1/num2} is the division of your given values.')
    else:
        print('Wrong choice!')
else:
    print('You entered a wrong number.') 

