# Strings are immutable

unit_name = "Level 4 Programming" # assigns variable
print("This unit is: ", unit_name)
print("The 1st character is:", unit_name[0]) # Access first character using index 0
print("The 4th character is:", unit_name[3]) # 4th character is of index 4 - 1 = 3
print("The 9th character is:", unit_name[8]) # 9th character is of index 9 - 1 = 8


greeting_string = "Welcome to Programming unit! This is a Level 4 unit :)"
print(greeting_string)
print("The 1st character is", greeting_string[1]) 
print("The 5th character is", greeting_string[5])
print("The 0th character is", greeting_string[0])
 
print(greeting_string[0:5])
print(greeting_string[-1])
print(greeting_string[-4:])