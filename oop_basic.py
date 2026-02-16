'''
1). class. : ---> blue print to create the object
                  syntax:
                      class classname: 
                      

2). object : ---> real world entities of the class/making using the blueprint
            syntax:
                obj_name=classname()
                  print(obj_name.value)


3). self :-->   self is used for the object
            if vlaue is diffrenet then use the self.
            if the value is same then declare it outside the constructor


4). attribute
              (properties of class): ---> variable inside the class 
                    ----> class and obj attribute is diff
                     ---> it is different 
                     ---> class.attribute()
                     ---> object attribute is higher then class attribute



5). method--> how it works
    method
          (function of attributes): ----> function of the class 
                        it can be same or not 



6). static method ---> it does not use the self as the parameter (work at the class level)
                        syntax:
                        class Student:
                        @staticmethod:
                         def colllege:

7). abstraction ---> hiding the implementation details of a class and only showing the essential feature to the user


8). encapsulation --> wrapping data and function into a single unit(obj) 


9).  constructor 
---> types of constructor
                1) default constructor
                2) parameterized construxtor
--> special fucntion which invoked itself when obj is created

--> all class have a function called __init__() which is always executed when the class is being initiated

        syntax:
         def __init__(self): 
            block of code

--> constructor always takes the argument which is self(it is parameter)
--> data stored is called attributs 
                         
                         

'''
'''default constructor '''

# class Student:

#     def __init__(self):
#         print("defalut constructor")
# s=Student()

# class Student:

#     def __init__(self):
#         print(id(self))
# s=Student()
# s2=Student()
# print(id(s2))
# print(id(s))

'''parameterized constructor '''

# class student:

#     def __init__(self,naam,umer,location):
#         self.name=naam
#         self.age=umer
#         self.thau=location
#         self.show_info()
#     def show_info(self):
#         print(f'{self.name},{self.age},{self.thau}')

# s=student('naam',20,'kathmandu')

#factorial of the numebr
#floor function and the celling function 

# class Student:

#     def get_info(self):
#         self.name=input("enter the name")
#         elf.age=int(input("enter the age"))
        
#         self.location=input("enter your location")
    

#     def show_info(self):
#         print(f'my name is {self.name} i am {self.age} i live in {self.location}')



# class student:
#     name='suyog'

# s1=student()
# print(s1.name)

# class car:
#     color="blue"

# c1=car
# print(c1.color)


# class Student:

#     def get_info(self):
#         self.name=input("enter the name")
#         self.age=int(input("enter the age"))
        
#         self.location=input("enter your location")
    

#     def show_info(self):
#         print(f'my name is {self.name} i am {self.age} i live in {self.location}')

# s1=Student()
# s2=Student()

# s1.get_info()
# s1.show_info()



'''class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):               # Override parent method
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Usage
dog = Dog("Buddy")
print(dog.speak())   # Buddy barks.
cat = Cat("Kitty")
print(cat.speak())   # Kitty meows.'''

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner                # public
#         self._balance = balance            # protected (convention)
#         self.__pin = "1234"                 # private (name mangling)

#     # Getter method for balance (controlled access)
#     def get_balance(self):
#         return self._balance

#     # Method to deposit money (with validation)
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount}. New balance: {self._balance}")
#         else:
#             print("Invalid amount")

#     # Method to withdraw money (with validation)
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew {amount}. New balance: {self._balance}")
#         else:
#             print("Insufficient funds or invalid amount")

# # Usage
# acc = BankAccount("Alice", 1000)
# print(acc.owner)               # Alice (public)
# print(acc.get_balance())        # 1000 (via getter)
# acc.deposit(500)                # Deposited 500. New balance: 1500
# acc.withdraw(200)               # Withdrew 200. New balance: 1300

# # Trying to access private members
# # print(acc.__pin)               # AttributeError: 'BankAccount' object has no attribute '__pin'
# print(acc._BankAccount__pin)     # "1234" (name mangling still allows access, but it's discouraged)


'''import math

num = 25
sqrt_num = math.sqrt(num)
print(f"The square root of {num} is {sqrt_num}")


import random

rand_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {rand_num}")

from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now}")
print(f"Today's date: {now.date()}")
print(f"Current time: {now.time()}")'''


# class ConnectionError(Exception): pass
# class QueryError(Exception): pass
# class CommitError(Exception): pass
# class RollbackError(Exception): pass

# class DatabaseConnection:
#     def connect(self):
#         print("Connecting...")
#         # Simulate success
#         # raise ConnectionError("Network unreachable")

#     def execute_query(self, query):
#         print(f"Executing: {query}")
#         # Simulate success
#         # raise QueryError(f"Syntax error in {query}")

#     def commit(self):
#         print("Committing...")
#         # raise CommitError("Commit failed")

#     def rollback(self):
#         print("Rolling back...")
#         # raise RollbackError("Rollback failed")

#     def close(self):
#         print("Closing connection.")

# def safe_transaction(connection, queries):
#     try:
#         connection.connect()
#     except ConnectionError as e:
#         print(f"Connection failed: {e}")
#         return False
#     else:
#         # Connection succeeded
#         try:
#             for q in queries:
#                 connection.execute_query(q)
#         except QueryError as e:
#             print(f"Query failed: {e}")
#             try:
#                 connection.rollback()
#             except RollbackError as rb_e:
#                 print(f"Rollback also failed: {rb_e}")
#             return False
#         else:
#             try:
#                 connection.commit()
#             except CommitError as e:
#                 print(f"Commit failed: {e}")
#                 return False
#             else:
#                 print("Transaction committed successfully.")
#                 return True
#         finally:

#             pass
#     finally:

#         connection.close()
import json
json_string = '{"products": [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}]}'
data = json.loads(json_string)

# Get the list of products
products = data["products"]

# Loop through each product
for product in products:
    print(product["id"], product["name"])