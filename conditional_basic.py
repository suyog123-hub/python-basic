#conditional statement---> making decision basen on variable 

# if statement 
#syntax :
  # if condition(true/false):
    #   body of code
# else : there is no syntax if if condition is false then the block of code in else will be print 
'''price = 50
if price >= 100:
    print("i will buy bag") 

print("sorry yr")

age=int(input("enter the number"))
if age>=18 :
    print("you are eligible for voting ")

print("not eligible1")'''

#short handed if statement : or ternary operator 
'''age=4
print("you can vote") if age>=18 else("print you cannot vote ")'''

# nested condition 
# syntax 
''' if condition 
      block of code 
      
else condition 
     block of condiyion 
     '''

'''age=int(input("enter the age "))

if age<=10:
    print("you bus fare is waved")
elif age>10 and age<=25:
    if age == 30:
        print("you are lucky today")
    else:
        print("you bus fare is 100")
else:
    print("your bus fare is 150")'''



