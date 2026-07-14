# =====================  Strings practices ============================

#  finding the length of string ----------------

string = input('Enter the String : ')
print(len(string))

# by looping on string finding the length of string --------------------
count = 0
for x in string :
    count +=1
print(count)    


# finding the sub-string in main string ---------------------

sub_string = input('Enter the sub-string which you find from upper given string : ')

if(sub_string in string):
    print(f'Yes {sub_string} is available in string. And it occurs {string.count(sub_string)} times. ')



# string methods problems ------------------------------------

print('''We want to practice the some string methods 
      press 1 for conver text in upper case
      press 2 for convert text in lower case
      press 3 for removing white spaces from text
      press 4 for replace the word in string
      press 5 for splitting the a string''')

decision = int(input('Enter the number for selection : '))

if(decision ==1):
    string = input('Enter a string to convert it in upper case : ')
    print(string.upper())
elif(decision == 2):
    string = input('Enter a string to convert it in lower case : ')
    print(string.lower())
elif(decision == 3):
    string = input('Enter a string with white spaces at the begining or at the ending of string : ')
    print(string.strip())
elif(decision == 4):
    string = input('Enter a string : ')
    replacing_word = input('Enter a word which you want to replace : ')
    by_replacing_word = input('Enter a new word which will replaced at the old word  : ')
    print(string.replace(replacing_word,by_replacing_word))
elif(decision == 5):
    string = input('Enter a string forseparating the each word with comma : ')
    print(string.split())
else:
    print('You choose invalid number.')    




#   count vowels in a string -----------------------------

input_string = input('Enter a string : ')
vowels = 'aeiouAEIOU'
count = 0

for x in input_string :
        if(x in vowels): 
          count +=1
print(count)  





#  finding the upper-case , lower-case ,numeric alphabets or symbols in a string -------------------

string_input = input('Enter a string : ')
lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric_alphabets = '0123456789'
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
symbol_count = 0

for x in string_input :
    if x in uppercase_alphabets :
        uppercase_count += 1
    elif x in lowercase_alphabets :
        lowercase_count += 1
    elif x in numeric_alphabets :
        numeric_count += 1
    else :
        symbol_count += 1
print(f'uppercase : {uppercase_count} lowercase : {lowercase_count} numbers : {numeric_count} symbols : {symbol_count}') 


#  reverse a string ---------------------------------

input_str = input('Enter a string : ')
reverse_str = ""

for i in range(len(input_str)-1,-1,-1):
    reverse_str += input_str[i]
print(f'reverse string of {input_str} is {reverse_str}.')    

# string slicing problems -------------------------------

print(input_str[0:4])
print(input_str[0:])
print(input_str[0:4])
print(input_str[:4])
print(input_str[2:])
print(input_str[0::2])