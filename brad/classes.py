# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#creata a class

class user:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age} years old.'
    def has_birthday(self):
        self.age +=1


#extend class

class Customer(user):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and i am {self.age} years old and my balance is {self.balance}'

#intialize user object
maurice = user('Maurice Molande', 'molande.mau@gmail.com', 56)
#init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 45)
 
janet.set_balance (500)
print(janet.greeting())
 
maurice.has_birthday()
print(maurice.greeting()) 