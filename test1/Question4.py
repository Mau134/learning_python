#Write a function that returns the elements on odd positions in a list.
# i = odd #create an empty array as a placeholder for odd numbers
# for i in ages:
#     if i % 2 != 0:
#         odd.append(i)
# print(odd)

def odd_numbers(my_list):
    return [x for x in my_list if x % 2 != 0]

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = odd_numbers(my_list)
print(result) 
# The condition x % 2 != 0 checks whether the element x is odd
# and is not divisible by 2 and only those
# elements that satisfy this condition will be included in the result list.
