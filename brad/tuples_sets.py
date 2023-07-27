# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create a tuple
fruits = ('Apples','Oranges', 'Grapes')
fruits2 = tuple(('Apples','Oranges', 'Grapes'))

#single value needs a trailling comma
fruits2 = ('Apples',)

#get value
print(fruits[1])

#cant change value
#fruits[0] = 'Pears'

#delete tuple
del (fruits2)

#tuple length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#check if sometjing is in a set 

print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')

print(fruits_set)

#remove from set
fruits_set.remove('Grape')

#add something already there
fruits_set.add('Apples')

#clear set
#fruits_set.clear()

#delete set 
#del fruits_set

print(fruits_set)

