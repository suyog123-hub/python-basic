# factorial of the number using recursion 
'''def fact(n):
    if(n==0 or n==1):
        return 1
    return fact (n-1)* n
print(fact(5))
'''
# sum of frist natural number
'''def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))'''

# fibonacci number
'''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))'''

# print from n to 1
'''def num(n):
    if n==0:
        return 
    print(n)
    return num(n-1)

print(num(5))'''

# count digit 
'''def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(6775))'''

# reverse the string 
'''n=["sum","mom","non","nitin","malaalam","suyog"]
for i in n:
    if i==i[::-1]:
        print(i," is palindrome")
    else:
        print(i,"is","not palindrome")'''

'''def pal(s):
    if len(s)<=1:
        return True
    return s[0] == s[-1] and pal(s[1:-1])  # remove the last and first word and keeps the middle one 

print(pal("mom"))'''

