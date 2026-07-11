# ============================= For loops Problems ===========================

# sequence printing probmes -------------------

num = int(input('Enter the number : '))
step = int(input('Enter the number for steps  : '))
i = 0

while(i <= num):
    print(i)
    i = i+step


# Even number generating problems ------------

num_range = int(input('Enter the of even number printing : '))
i = 0

while(i <= num_range):
    print(i)
    i = i+2


# Odd number generating problems --------------

num_range = int(input('Enter the of even number printing : '))
i = 1

while(i <= num_range):
    print(i)
    i += 2


# Prime number checking problems -----------------

num_for_checking = int(input('Enter the number you want to check: '))

isPrime = True
i = 2

if num_for_checking <= 1:
    print(f'{num_for_checking} is not prime number.')
else:
    while i < num_for_checking:
        if num_for_checking % i == 0:
            isPrime = False
            break
        i += 1

    if isPrime:
        print(f'{num_for_checking} is prime number.')
    else:
        print(f'{num_for_checking} is not prime number.')   
       



#  find the sum of all even numbers--------------------

num_range = int(input('Enter the of even number printing : '))
even_sum = 0
i = 0

while i <= num_range:
    even_sum += i
    i += 2

print(even_sum)



# find the sum of all odd numbers ------------------------------

num_range = int(input('Enter the of odd number printing : '))
odd_sum = 0
i = 1

while i <= num_range:
    odd_sum += i
    i += 2

print(odd_sum)



#  find the square of number --------------------------------

num_range = int(input('Enter the of number as a range for printing square : '))
i = 1

while(i <= num_range):
     print(i , i**2)
     i += 1




# checking number is divisible by 8 or 12 between 100 numbers --------------------

i = 1 
while(i <= 100):
    if(i % 8 == 0 or i % 12 == 0):
        print(i)
    i += 1










