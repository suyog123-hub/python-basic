#block of code that perform a specific task 
# it reduce the redendency
'''use (def) keyword to create a function '''

# function declare 
#function defiine 
#function call 

'''types of function '''
# built in function :
                #print()
                #len()
# user defined function :
                    #it is the function manipulated by the user according to the use


#default parameter  we should start giving default parameter from the backside of the code 

'''syntax for the function '''
# def function_name(argument 1 ,argument 2):
    # body of the code 
#function_name(argumnt 1) ----> function call 

''' function with ni argument'''
# def greet():
#     print("good morning sipalaya")

''' fun with argument'''

# def greet(name,age,salarly):
#     print(f"my name is {name} i am {age} years old my salarly is{salarly}")
# greet('suyog',20,20000)
# greet('su',20,20000)
# greet('g',0,300)


''' positional argument ---> position doesnt matter it print as it is ''' 

# def greet(name,age,salarly):
#     print(f"my name is {name} i am {age} years old my salarly is{salarly}")
# greet('suyog',20,20000)
# greet(34,20,'suyog')
# greet('g',0,300)

''' default argument '''

# def greet(name,age,salarly=0):
#     print(f"my name is {name} i am {age} years old my salarly is{salarly}")
# greet('suyog',2)
# greet('su',20,20000)
# greet('g',0,300)

'''return statement ---> it terminate the function and return the specific value ''' 
''' if return then use print if return not use simplu call function only  '''
def add(num1,num2):
    total=num1+num2
    print(total)
   
add(20,30)



# greet()
# greet()

'''global variable '''
# var='python' ---> this is global variable
# def func1():
#     var2='suyog' -> local variable
#     print(var) ---> excessing the global variable 

# func1()

'''(global variable) ---> it is used to make the global variable '''
