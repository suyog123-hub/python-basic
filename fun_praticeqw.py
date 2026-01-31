'''# wtite the fun to print the length of teh list '''
# '''a=[1,2,3,4,65,7,8]
# def aa():
#     bb=len(a)
#     print(bb)

# # aa()'''
# '''n=int(input("enter the number"))
# def a(n):
   
#     if n==0 or n==1:
#             print("the factorial is 0")

#     else:
#         b=1
#         while n>1:
#          b=b*n
#          n-=1
#     print(b)
# '''



'''# input the function if odd the output odd is even then output is even '''

# n=int(input("enter the number"))
# def num_check(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")

# num_check(n)

'''greater of two number'''

# def greater():
#     num1=int(input("enter the frist number"))
#     num2=int(input("enter the second number"))

#     if num1>num2:
#         print("num1 is greater")
#     else:
#         print("num 2 is greater")

# greater()

'''find the greatest among 4 number'''

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# num1=int(input("enter the first number"))
# num2=int(input("enter the second numebr"))
# num3=int(input("enter the third number"))
# num4=int(input("enter the fourth numebr"))
# gre_of_1and2=greater(num1,num2)
# gre_of_2and3=greater(num3,num4)
# gre=greater(gre_of_1and2,gre_of_2and3)
# print(gre)

'''Write a function total_sales(sales_list) that takes a list of daily sales numbers and returns
the total sales.
Example: total_sales([100, 200, 300]) # Output: 600'''

# def total():
#     total_sales = []
#     total_sum = 0

#     user = int(input("Enter the total number of sales item in the day: "))

#     for i in range(user):
#         amount = int(input(f"Enter the amount of sale of  {i+1} item: "))
#         total_sales.append(amount)

#     for i in total_sales:
#         total_sum = total_sum+i
#     print("your total  sales of the day is",total_sales)
#     print("The total sales is", total_sum)

# total()

# def total( total_sales):
#     total_sum = 0
#     for i in total_sales:
#         total_sum = total_sum+i
#     print(total_sales)
#     print("The total sales is", total_sum)

# total([100,200,300])

'''Write a function max_sale_day(sales_dict) that returns the day with the highest sale.
Example: max_sale_day({'Mon': 100, 'Tue': 500, 'Wed': 300}) # Output: 'Tue' '''

# def max_sale_day(sales_dict):
#     max_day = None
#     max_amount = 0

#     for day, amount in sales_dict.items():
#         if amount > max_amount:
#             max_amount = amount
#             max_day = day
#     print("the maximum sale is on ",max_day,"and the total sales is",max_amount)


# max_sale_day({'Mon': 100, 'Tue': 500, 'Wed': 300})

'''Write a function sales_growth(last_month, this_month) to calculate the growth
percentage.
Hint: Growth% = ((This Month - Last Month) / Last Month) * 100
Example: sales_growth(2000, 2500) # Output: 25.0'''

# def sales_growth(last_month,this_month):
#     growth=((this_month - last_month) / last_month) * 100
#     return growth

# print(sales_growth(2000, 2500))


'''Filter High-Value Transactions
Write a function high_value_transactions(transactions, threshold) to return transactions above a threshold.
Example: high_value_transactions([100, 500, 2000], 1000) # Output: [2000]'''

 
    
