# ---------------check positive or negative number-----------------------

number = float(input('Enter the number to check positive or negative number : '))

print(f'{number} is positive.') if(number > 0) else print(f'{number} is negative.') if(number < 0) else print(f'{number} is zero.')



# ---------------check the number even or odd------------------------------

number = float(input('Enter the number to check it even or odd : '))

print(f'{number} is Even.') if(number % 2 == 0) else print(f'{number} is Odd.')




#--------------------greatest number prediction--------------------------------

first_Num = int(input('Enter the first number : '))
second_Num = int(input('Enter the second number : '))
third_Num = int(input('Enter the third number : '))

if first_Num > second_Num and first_Num > third_Num :
    print(f"{first_Num} is greatest number.")
elif second_Num > first_Num and second_Num > third_Num :
    print(f"{second_Num} is greatest number.")
else :
    print(f"{third_Num} is the greatest number.")  



# --------------------single number digit checking ----------------------------

number = int(input('Enter a number : '))

if(number >= 0 and number <= 9):
    print(f'{number} is single digit.')
else:
    print(f'{number} is not single digit.')    