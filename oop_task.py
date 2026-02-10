# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print(f"hi {self.name} your average is {(sum/3)}")

# s1=Student("suyog",[20,30,40])
# s1.get_avg()


""" bank system"""
# class account:

#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account=acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("rs" ,amount , "was debited")
#         return self.balance
    
#     def credit(self,amount):
#         self.balance += amount
#         print("rs" ,amount , "was creditied")
#         return self.balance
    
    
# acc1=account(10000,123245)
# acc1.debit(1000)
# acc1.credit(500)


#factorial of the numebr
#floor function and the celling function 
# custommath.py
# class custommath:

'''own module '''
#     def __init__(self):
#         self.pie=3.14
#         self.e=2.7

#     def fact_num(self, n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#     def floor_num(self,n):
#         return int(n)
#     def celling_num(self,n):
#         r=int(n)
#         return r+1

# c1=custommath()
# print(c1.fact_num(5))
# print(c1.floor_num(12.34))
# print(c1.celling_num(13.343))