#list ---> collection of multiple data 
# it is mutable (value can be changed)
# # it is listed in big bracket 
# numbers=[23,"suyog","shreya"]

# print(numbers[-1]) #it helps to print the last vlaue and start with the -1 and increse respectively 
number =[ 1,1,1,34,5,4]
number[1]=100
print(number)

#METHOD OF LSIT 
# 1) .APPEND(used to add one element at the end) 
# for eg
name=['suyog','shreya','nabin','sumanta','binda']
# name.append('dhruba')
print(name)    
#2) .extend (used t oadd multiple element at the end)
name.extend([1,2,3,34])
print(name)
#3) .insert(help to inset the data in the required index)
name.insert(1,'milan')
print(name)
#4) .pop(used to remove the last value of the set)
name.pop()
print(name)
# remove (it is used to remove the specific value in the list )
name.remove('suyog')
print(name)
print(name.index(3))
#6) .count(it helps to count the number of repetation of  element )
print(name.count(34))
#7) len(it helps to count the length of the set of then umber of element in the set)
print(len(name))
print(name.clear()) #clear all the element in the set


number = [1,2,3,67,78,3445,4,5,0,6,7,8,90]
number.sort(reverse = False) # is reversed = true the it will print the decending order if reversed = false the it will print in ascending order 
print(number)

print(number[-1]) #display the last element of the list 

number.remove(3445) # remove the one element from the list 
print(number)
# python program to reverse the list 
number.reverse()
print(number)

#nested list ---> a list inside the another list is called the nested list 
a=[1,2,3,4]
print(sum(a))
print(max(a))
print(min(a))

