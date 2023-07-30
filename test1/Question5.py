
#Write 2 functions that compute the sum of the numbers in a list: using a for-loop and a while-loop
#for loop
def sum_with_for_loop(my_list):
    total_sum = 0
    for num in my_list:
        total_sum += num
    return total_sum


my_list = [1, 2, 3, 4, 5]
result = sum_with_for_loop(my_list)
print(result)  

#while loop
def sum_with_while_loop(my_list):
    #decleration of variables
    total_sum = 0
    index = 0
    list_length = len(my_list)
    while index < list_length:
        total_sum += my_list[index]
        index += 1
    return total_sum


my_list = [1, 2, 3, 4, 5]
result = sum_with_while_loop(my_list)
print(result)  
