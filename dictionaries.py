# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create a dictionary 

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30 
}

#get a value

print(person['first_name'])
print(person.get('last_name'))

#Add key/value

person['phone'] = "555-555-555"

#get dict keys
print(person.keys())

print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

#remove item
del (person['age'])
person.pop('phone')

#clear
person.clear()

#get length
print(len(person2))

#list of dict

people = [
    {'name': 'Maurice', 'age': 30},
    {'name': 'Kelvin', 'age': 25}
]

print(people[1]['name'])