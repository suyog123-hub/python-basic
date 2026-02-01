# mode in the file 
# r--> read
# w--> write
#a---> append 
#rb--> 
#reandline() --> used to read the line wise in the file 


''' read all the line '''
# file = open(r"/Volumes/USSS/python/file_handling/demo.txt", 'r')
# content = file.read()
# print(content)
# file.close()

''' write in the file '''
# with open(r'/Volumes/USSS/python/file_handling/demo1.txt','w') as file:
#     file.write("this is\n")
#     file.write("this is the next file\n")
#     file.write("this is the another next file\n")

'''append mode '''
# with open(r'/Volumes/USSS/python/file_handling/demo1.txt','a') as file:
#     file.write("this is\n")
#     file.write("this is the next file\n")
#     file.write("this is the another next file\n")

''' print the multiplication table and from 1 to 10 and store all the multiplication table in different txt file'''
# for i in range (1,11,1):
#     print('2 *',i ,'=',(2*i))
