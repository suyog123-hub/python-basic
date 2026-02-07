# qw no 1
# Task: Sum All Numbers in a List
# input=[10, 20, 30, 40, 50]
# Expected output : Sum of numbers: 150

'''ab=[10, 20, 30, 40, 50]
a=0
for i in ab:
    a=a+i

print(a)'''

# qw no 2

# Write a Python program that accepts a string and counts the number of upper and lower case letters. 
# Sample String : 'My Name is Sujan' 
# Expected Output : No. of Upper case characters : 3 No. of Lower case Characters : 10

'''sentence=" My Name is Suyog"
upper_sen=0
lower_sen=0

for i in sentence:
    if i.isupper():
        upper_sen+=1
    if i.islower():
        lower_sen +=1
print("total word that is in upper is",upper_sen)
print("total word that is in lower is",lower_sen)'''

#qw no 3

# Write a Python program that takes a string and returns a dictionary where:

# Keys are the unique characters in the string

# Values are the counts of each character

# input="aabbssssdka"
# expected Output
# {"a": 3, "b": 2, "s": 4, "d": 1, "k": 1}

'''word="aabbssssdka"
output={}
for i in word:
    if i in output:
        output[i]+=1
    else:
        output[i]=1

print(output)
    '''
#qw no 4 
# Write a Python program to generate and print the first n numbers
# in the Fibonacci sequence, where each number is the sum of the two
# preceding ones, starting from 0 and 1.
# 0,1,0+1=1,1+1=2,2+1=3,3+2=5,5+3=8,8+5=13

'''num=int(input("enter the number"))
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c'''


#qw no 5 
# Python program to check the validity of password input by users
# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character
# note: Clearly indicate which specific requirements were not met

'''password=input("enter the password")
special_character = "@#$%^&*!?"
if len(password)>=8 and \
    any(ch.isupper() for ch in password) and\
          any(ch.islower() for ch in password) and\
                any(ch.isdigit() for ch in password) and \
                    any(ch in special_character for ch in password):
        print("valid password")
else:
    print("specific requirements were not meet")'''
 
# qw no 6
# find the prime numebr
'''num1=int(input("enter the  stating number of the prime number"))
num2=int(input("enter the  ending number of the prime number"))
print("Prime numbers between", num1, "and", num2, "are")
for num in range(num1, num2):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
'''
# qw no 7
# print the element of the following list using a loop 
'''n=int(input("enter the starting number"))

n1=int(input("enter the ending number"))
b=[]
for i in range(n,n1+1):
    ab=(i*i)
    b.append(ab)
print(b)'''

# search the number in the tuple 
'''a=[1,2,344,5,6,7,8,9,0,2343,33]
for i in a:
    if i==5:
        print("found the number at index")
        break
    else:
        print("number not found")'''

#wap to find the ssum of the first n number

number=int(input("enter the numebr"))
s=1
for i in range(1,number+1):
   s=s*i

print("sum=",s)



