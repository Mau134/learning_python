# A List is a collection which is ordered and changeable. Allows duplicate members.


# create a list

numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
#we can also use a constractor

#numbers2 = list((1,2,3,4,5))

# Get a specific item from a list of arrays
print(fruits[1])

#length of the list

print(len(fruits))

#append/add to list

fruits.append('Mangos')

#remove

fruits.remove('Grapes')

#insert into position

fruits.insert(2, 'Strawberries')
#change value

fruits[0] = 'Blueberries'

#remove with pop 
fruits.pop(2)

#fruits.reverse
fruits.reverse()
numbers.reverse()

#sort list
fruits.sort()

#sort in  reverse
fruits.sort(reverse=True)

print(fruits)
print(numbers)