# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'brad'
age = 37

#concanate
#print('Hello, my name is ' + name + ' and i am ' + str(age)) 
# String Formatting

#arguments by position

#print('My name is {name} and i am {age}'.format(name=name, age=age))

#f-strings

#print(f'Hello my name is {name} and i am {age}')

# String Methods

s = 'hello world'

#capitalize string

print(s.capitalize())

#make all uppercase

print(s.upper())

#make all lowercase

print(s.lower())

#swap case

print(s.swapcase())

#get length

print(len(s))
 
# replace
print(s.replace('world', 'everyone'))

#count
sub = 'h'
print(s.count(sub))

#starts with
print(s.startswith('hello'))

#endswith
print(s.endswith('d'))

#split into a list
print(s.split())

#find position
print(s.find('r'))

#is all alphanumeric
print(s.isalnum())

#is all alphabetic
print(s.isalpha())


#is all numeric
print(s.isnumeric())