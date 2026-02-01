# question for pratice 
#1) cerate an empty list and add five number 
a=[]
a.append('suyog')
a.append('suyo')
a.append('suy')
a.append('su')
a.append('s')
print(a)

#2 start with a list of three fruits add two more using the method 
name=['salija','khadka','katwal']
name.extend(['suyog','khadka','katwal'])
print(name)

#3 insert a new coloe at index 2 in a list of color 
color=['red','black','gray','white']
color.insert(2,"blue")
print(color)

#4 remove a specific number from a list using method
num=[1,3,4,56,776,656]
num.remove(3)
print(num)

#5 delete teh last element from a lsit using method 

num=[1,2,3,3,4,4,4,4545,45]
num.pop(-1)
print(num)

#6 delete the element at index 3 using pop

num=[1,2,3,4,5,6]
num.pop(3)
print(num)

#7 sort a lsit of number in ascending order 

num=[9,65,634,64,645,645,64,5645,464,64,3]
num.sort(reverse=False)
print(num)

#8 sorrt a list of string in reverse alphabetical order using 
name=['suyog','akash','yuzu','giyan']
name.sort(reverse=False)
print(name)

#9 reverse the element of a list 
bike=["h2","bmws1000rr","hayabhusa",'r1']
bike.reverse()
print(bike)

#10 find the index of a given element 
name=['s','b','y','o']
print(name.index('b'))

#11 count how many times a specific appears in the list
num=[1,2,3,3,33,3,4,34,34,3,43,5,456,5,5,54,545454,54]
print(num.count(3))

#12 make a copy of a list and verfiy that the changing the orginal does not affect the copy 
num=[1,2,3,4,5,6]
num1=num.copy()
print(num1)

#13 clear all the element  from a list using clear
num = [1,2,3,4,5,6]
num.clear()
print(num)

#14 combine two list  then remove one element 

num1= [1,2,3]
numv = [4,5,6]
num1.extend(numv)
print(num1)
num1.remove(2)
print(num1)

#15 