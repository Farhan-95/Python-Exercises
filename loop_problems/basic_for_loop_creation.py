# ============================= For loops Problems ===========================

# sequence printing probmes -------------------

num = int(input('Enter the number : '))
step = int(input('Enter the number for steps  : '))

for i in range(0,num+1 , step):
    print(i)



# Even number generating problems ------------

num_range = int(input('Enter the of even number printing : '))

for i in range(0,num_range+1,2):
    print(i)




# Odd number generating problems --------------

num_range = int(input('Enter the of even number printing : '))

for i in range(1,num_range+1,2):
    print(i)



# Prime number checking problems -----------------

num_for_checking = int(input('Enter the number you wnant to check : '))
isPrime = True

for i in range(2 ,num_for_checking):
    if(num_for_checking % i == 0):
        isPrime = False
        break
if(isPrime):
     print(f'{num_for_checking} is prime number.') 
else:
    print(f'{num_for_checking} is not prime number.')       




#  find the sum of all even numbers--------------------

num_range = int(input('Enter the of even number printing : '))
sum = 0

for i in range(0,num_range+1,2):
      sum += i
print(sum)  



# find the sum of all odd numbers ------------------------------

num_range = int(input('Enter the of even number printing : '))
sum = 0

for i in range(1,num_range+1,2):
      sum += i
print(sum)      



#  find the square of number --------------------------------

num_range = int(input('Enter the of even number printing : '))

for i in range(0,num_range):
    print(i , i**2)



# checking number is divisible by 8 or 12 between 100 numbers --------------------

for i in range(1,101):
    if(i % 8 == 0 or i % 12 == 0):
        print(i)

