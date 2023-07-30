
#Write a function that checks whether an element occurs in a list.
def element_in_list(element, my_list):
    return element in my_list

my_list = [1, 2, 3, 4, 5]
element_to_check = 3
result = element_in_list(element_to_check, my_list)
print(result)  
#returns a boolean value

