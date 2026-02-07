#loop ---> it is used to repeat the instruction 
# it is programming structure that repeat a block multiple time until some condition  it match or no of iteration 

# type of loop:
  # for loop   if we know the fixed time for repetation then use for loop
  # while loop  if we dont knpow how many time to repeat the code then use the while loop 

# it is used for sequeantial traversal : str,list,tuple,range,set,dict,etc;

#syntax 
# '''for items in iterable:
# block of code'''

# # loop in list

'''# a=['suyog','khadka','milan']
# for i in a:
#     print(i)'''
    

# # loop in string 
'''# a="suyog"
# for i in a:
#     print(i)  '''  

# loop in dict 

'''a={
    "name":'suyog',
    'age': 20
}
for i,j in a.items(): i is for key and j is for value 
    print(f"key{i} value {j}")
    print(j)'''

# loop in range (start,end,range) range(3,8,1)-->3,4,5,6,7

# for i in range(0,10):
#     print(i)
# for i in range(10,0,-1):
#     print("suyog")

#multiplication table 
'''for i in range (1,11,1):
    print('2 *',i ,'=',(2*i))'''

#if statement inside loop 
"""
a=[1,2,3,4,5,6,7,8]
op=[]
for i in a:
    if i%2==0:
      op.append(i)

print(op)"""

'''a=["sujan","ram","hari","shyam"]
op=[]
for i in a:
    if i.startswith("s"):
        op.append(i)

print(op)'''

# to print palindrome

a=["mom",'nitin','suyog','shreya']
ab=[]
for i in a:
    if i==i[::-1]:
        ab.append(i)

print(ab)