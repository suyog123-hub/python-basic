#set---> set is the collection of items 
# it is mutable 
# it is in unorder
# it does not allow dublication 
# it is denoted by curly bracket 

# a={'suyog','khadka','shreya'}
# print(type(a))
# print(a.update({'mami'}))
# print(a)
# a.pop() # random delete 
# print(a)
# a.discard('milan') 
# print(a)

# method in the set 
'''
   a.add() #used to add 
   a.update({mami}) # used to update the set 
   a.clear # claear all the data 
   #a.pop() # used to clear the last element from the questrion 
   a.remove() # used to remove the specific data if value is not present we are trying to remove in the lsit then it show the error 
   a.discard() # it alse remove the specific data but if the given value fro deleting is not in the list it doesnot show the error
'''
# specific set method in the set 
# a={1,2,3,4,5,6}
# b={3,4,5,6,7,8}

# c=a.intersection(b)
# c=a.union(b)
# c=a.difference(b)
# c=b.difference(a)
# c=a.symmetric_difference(b)
# c=b.symmetric_difference(a)
# print(c)
 
# frozen set : immutable
a=frozenset({1,2,3,4})
b={1,4,}
c=a.intersection(b)
print(c)

a=set()
print(a)