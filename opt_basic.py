# operator ---> operator  is a symbol that is used to perform some specific operation between two operand 
    # a=20
    # b=40
# here a and b is operator
# + and = is operand 

# precedence rule 
# first it follow paranthesis  ()
# then exponential ** (it follow  left to right)
# divide(/) multiply(*)  % // it has all same power ( it follow the left to right)
# then + and - (it also follow the left to right )



#0) ternary operator : shortcut for the if-else statement that fits in the one line
  #syntax:
    #value_if_true if condition else value_if_false
    #Return thsi if condtion else return that 
'''
# Ternary operator (1 line)
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
'''
#1) arthemetic operator ---> it gives either integer or flaot 
'''
print(a+b) addition
print(a-b) subtraction
print(a*b) multiplication
print(a**b) exponential
print(a//b) Floor---> it gives only integer value 
print(a%b) modulus---> it gives the reminder 
'''
 
 # relative operator (comparision)(<,>,<=,>=)---> it return either true or false 
'''
a=20
b=40
print(a == b)
print(a != b)
print(a> b)
print(a<b)
print(a>=b)
print(a<=b)
'''
# assignment operator : (it is used in all arthemetic operator)
#increatment or decreament operator 
'''
a= 20
a+= 5
print(a)
'''
 
#logical operator : and,or,not ---> 

# and: both value must be true
# or : at least one value should be true 
# not : it change the value form true to false and false to true 
'''a=20
     b=30
    print(a>10 and b<50)
    print(a<10 or b<100)
    print ( not True) '''


# membership operator : in , not in

'''a= " my name is sujan "
print("sujan " not in a)
print("sujan "  in a)'''

# identity operator : is , is not  # it uses the momory address of the value 

'''a=20
b=30
print(a is b) # it check the address 
print(a ==b ) # it check the value 
print(a is not b) # IT CHECK THE MEMORY ADDRESS '''

#bitwise operator : & | ~ 

'''a=12
b=13
print(a&b)
print(a|b)
print(~a)'''

# eqn=3x**2 -5x -8=0

# a=3
# b=-5
# c=-8
# x=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
# x1=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
# print(x)
# print(x1)

# print(3*1+5-8)

# a=1
# b=2
# c=2
# res1=(a+b+c)**2
# res2=(a**2)+(**2)+(c**2)+(2*a*b)+(2*b*c)+(2*a*c)
# print(res1)
# print(res2)
