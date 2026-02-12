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



class Animal:
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
print(cat.speak())   # Kitty meows.