#   ================== List problems =================================

# print len , access the items or check list is empty or not ---------------------------

numbers = [10,20,30,40,50]
numbers1 = []
print(numbers[2])
print(len(numbers1))
print('Yes given list is empty') if (len(numbers1) == 0) else print('No the given list is not empty')


#  Performing list amnipulation ----------------------------

initial_list = [100,50,400,500]
initial_list[1] = 200
print(initial_list)
initial_list.append(600)
print(initial_list)
initial_list.insert(2,300)
print(initial_list)
initial_list.remove(600)
print(initial_list)
initial_list.pop(0)
print(initial_list)


# print the sum and average of list all items ---------------------

number_list = [10, 20, 30, 40, 50]
sum = 0

for x in number_list:
    sum += x
avg = sum / len(number_list)
print(f'sum : {sum}  average : {avg}')  



# sum with built-in function -----------------

number_list = [10, 20, 30, 40, 50]
sum = sum(number_list)
print(sum)



#  finding the min and max values from list -------------------------

Data = [45, 12, 89, 2, 67]
min = min(Data)
max = max(Data)
print(f'minimum : {min}  maximum : {max}')



# finding the product of list items ------------------

Factors = [2, 3, 5, 7]
mul = 1

for x in Factors:
    mul *= x
print(mul)   


#   finding the odd and even items from list -----------------------

Numbers = [10, 21, 4, 45, 66, 93, 11]
odd = 0
even = 0

for x in Numbers:
       if x % 2 == 0:
            even +=1
       else:
            odd += 1
print('even :',even,'odd : ',odd)        


#  reverse a list ----------------------
List = [100, 200, 300, 400, 500]

List.reverse()
print(List)
reverse = List[::-1]
print(reverse)



#  sort a list -----------------------------

Unsorted = [56, 12, 89, 3, 22]
Unsorted.sort()
print(Unsorted)
sorted = Unsorted.copy()
sorted.sort(reverse = True)
print(sorted)


# combine two lists ---------------------------

List_A = ["Physics", "Chemistry"]
List_B = ["Maths", "Biology"]
List_A.extend(List_B)
print(List_A)