# if else statement task 

#1--> write a program to input a n umber from the user and check whether it is even or odd
 
a=int(input("enter the number"))
if a % 2 == 0:
    print("it is even ")
else:
    print("it is odd") 

# 2--> write a program that ask the user for their age and print whether they are eligible  to vote 

age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote ")

#4 ---> write a program to input a character and check whether it is a vower or a consonant 

word=input("enter your single word")
if word in "aeiouAEIOU":
    print("it is a vowel")
else:
    print("it is a consonant")

#       # or 

word=input("enter your single word")
if word==a or word==e or word==i or word==o or word==u or word==A or word==E or word==I or word==O or word==U:
    print("it is a vowel")
else:
    print("it is a consonant")

# 5 ---> write a program to check to chefk if a number entered by the user is divisible by 5 or not 

a=int(input("enter the number"))
if a % 5 == 0:
    print("it is divisible by 5")
else:
    print("it is  not divisible by 5") 
 
#6 ---> write a program that input a student mark and print pass if marks are 40 or more otherwise print  fail 

marks=int(input("enter the student marks"))
if marks >=40 :
    print("studnet is pass ")
else:
    print("studnet is fail")

# 7 ---> write a program to check whether a number lies between 10 and 50 
num=int(input("enter your number to be checked"))
if num>=10 or num<=50:
    print("correct")
else:
    print("invaild number") 
      #or
num=int(input("enter your number to be checked"))
if num>=10 and num<=50:
    print("correct")
else:
    print("invaild number")

#8 --> Write a program to check whether a string entered by the user is a palindrome (same forwardand backward).

if word == word[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome") 

# 9 -->Write a program to validate whether an email ends with '@gmail.com' 

email = input("Enter your email: ")

if email.lower().endswith("@gmail.com"):
    print("Valid Gmail address")
else:
    print("Invalid email — it must end with '@gmail.com'")

#10---> Write a program to input two numbers and print which one is greater. If both are equal, print  thatthey are equal. 

num1=int(input("enter first number"))
num2=int(input("enter the second number"))
if num1>num2:
    print("num 1 is greater")
elif num1 == num2 :
    print("it is equal")
else:
    print("num 2 is greater") 

# 11 -->  Write a program to input a number and determine whether it is positive, negative, or zero.
num=int(input("enter the number to be checked"))
if num==0:
    print("number is 0")
elif num>0:
    print("it is positive")
else:
    print("it is negative")


#12---> Write a program where if the total shopping bill is greater than 1000, apply a 10% discount  andprint the final amount. 

bill=int(input("enter your total bill"))
if bill>1000:
    c=bill-(0.1*bill)
    print("you bill after the discount is:",c)

else:
    print("your total bill is:",bill) 

#13 --> Write a Python program to create a simple calculator that takes two numbers (num1 and num2) and an operator (+, -, *, /) as input from the user. Perform the corresponding operation based  on the given operator using elif statements 

num1=int(input("enter your first number in calcualtor"))
num2=int(input("enter your second number in calcualtor"))
operator=input("enter  valid operator +,-,*")
if operator == '+':
    print("your result is",num1+num2)
elif operator == '-':
    print("your result is",num1+num2)
elif operator == '*':
    print("your result is",num1+num2)
else:
    print("enter the valid operator")

# 14 --->  Write a program to input marks and assign grades based on the following conditions: 90+ =  A,80+ = B, 70+ = C, 60+ = D, else Fail.

marks=int(input("enter the student marks"))
if marks<0 and marks>100 :
    print("invalid marks enter marks from the range of 1 - 100")
elif marks>=90:
    print("congratulation you got A ")
elif marks>=80:
    print("congratulation you got B")
elif marks>=70:
    print("congratulation you got C")
elif marks>=60:
    print("congratulation you got D")
else:
    print("you are fail,work hard")

# 15--->  Write a program to input three numbers and print the largest among them. 

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2 & num1>num3:
    print("first is greater")

elif num2>num3:
    print("second is greater")

else:
    print(" third is greater") 

# 16--->  Write a program to validate a login system. If username is 'admin' and password is '1234', print'Login Successful', else print 'Invalid Credentials'. 

username=input("enter the username")
password=input("enter the password")
if username == "admin" and password == "1234":
    print("login sucessfull")

else:
    print("invalid credentials")

#17--->  Write a program that takes three sides of a triangle and checks whether the sides can form a  triangle (sum of any two sides > third). 

tri1=int(input("enter the first side of the tirangle"))
tri2=int(input("enter the second side of the tirangle"))
tri3=int(input("enter the third side of the tirangle"))
if tri1+tri2>tri3:
    print("it can form a trianlge")
if tri1+tri3>tri2:
    print("it can form a trianlge")

if tri1+tri2>tri3:
    print("it can form a trianlge")

else:
    print("it cannot form  a traingle ")

#18 -->  Write a program that calculates electricity bill: - If units ≤ 100: rate = 5 per unit - If units 101 200: rate = 7 per unit - If units > 200: rate = 10 per unit 
units = int(input("Enter the number of electricity units used: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Your electricity bill is:", bill, "rupees")

#19 --->  Write a program to check if a student gets a scholarship: Scholarship is granted if marks > 85 and attendance > 75%.

marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))
if marks > 85 and attendance > 75:
    print("Congratulations! You are eligible for the scholarship.")
else:
    print("Sorry, you are not eligible for the scholarship.")

#20 -->Write a program to input temperature and print: - Above 30 → Hot - Between 15 and 30 → Warm - Below 15 → Cold

temperature = float(input("Enter the temperature in °C:"))
if temperature > 30:
    print("It's Hot")
elif temperature>=15 or temperature <= 30:
    print("It's Warm")
else:
    print("It's Cold")

#21 --->  Write a program to check whether a given year is a century year (year ends with 00).

year = int(input("Enter a year: "))
if year % 100 == 0:
    print(year, "is a Century Year.")
else:
    print(year, "is NOT a Century Year.") 

#22---> Write a program to give movie ticket discount: If age is less than 12 or greater than 60 →  Discount applies, else no discount.

age = int(input("Enter your age: "))
if age < 12 or age > 60:
    print(" You are eligible for a discount on your movie ticket")
else:
    print(" regular ticket price applies.")

#23---> Write a program to determine employee bonus: Bonus is awarded only if experience is morethan 2 years and performance rating is greater than 7.

experience = float(input("Enter your years of experience: "))
rating = float(input("Enter your performance rating (out of 10): "))
if experience > 2 and rating > 7:
    print("Congratulations! You are eligible for a bonus.")
else:
    print("Sorry, you are not eligible for a bonus.")

#24 --> . Write a program to check whether a given year is a leap year. (Condition: divisible by 4 but not by100, except divisible by 400). 

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)

#25---->An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.  
# In the Gregorian calendar, three conditions are used to identify leap years:  
# ● The year can be evenly divided by 4, is a leap year, unless:  
# ■ The year can be evenly divided by 100, it is NOT a leap year, unless:  
# ● The year is also evenly divisible by 400. Then it is a leap year.  
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Given a year, 
# determine whether it is a leap year. If it is a leap year, return the Boolean True, 
# otherwise return False

# this is 
