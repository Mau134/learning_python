#Write a function that sorts a list of numbers in ascending order.

#The sorted() function returns a sorted list of the specified iterable object. 

def ascending_sort(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

numbers_list = [5, 2, 8, 1, 3]
sorted_numbers = ascending_sort(numbers_list)
print(sorted_numbers) 
