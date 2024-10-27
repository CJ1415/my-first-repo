my_list = [15, 23, 32, 46]

print(my_list[0])  # prints the first number in the list
print(my_list[-1])  # prints the last number in the list
print(my_list[:2])  # prints the first two elements in the list

result = my_list[0] + my_list[-1]  # adds the first and last item and assign
# them to result
my_list.append(result)  # add result to the end of the list using append method
