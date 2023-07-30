
#Write a function that concatenates two lists. For example [a, b, c], [1, 2, 3] becomes – [a, b,c, 1, 2, 3]
def concatenate_lists(list1, list2):
    return list1 + list2

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = concatenate_lists(list1, list2)
print(result)  
