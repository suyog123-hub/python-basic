# # map : dictionary ---> it is collection of data items that have key value pair which is mutable, order 
# #dict is the combination of key and value  
# a={}
# print(type(a))
# a={
#     "name":["suyog","shreya","akash"],
#     "age":20
# }
# # print(len(a)) # key and value make len 1 
# print(a["name"])
#  # imp 
# print(a.get("age","data is not found")) # if value is not found it  does not show the error 

# print(a.keys()) # it gives only key vlaue 
# print(a.values()) # it give only values side output
# # imp 
# print(a.items()) # it give both value and keys 

# a={
#     "name":["suyog","shreya","akash"],
#     "age":20
# }
# b={
#     "email":"ksuyog697@gmail.com",
#     "age":34
# }
# a.update(b)
# print(a)
# a.clear()
# print(type(a))
# del(a)

# a={
#     "name":["suyog","shreya","akash"],
#     "age":20
# }
# # a.popitem() #remove the last items ( key and value )
# # print(a)

# #imp
# a.setdefault("age",99)
# print(a)

# nested dictionary ---> a dictionary inside another dictionary

marks={
    "roll no 1": {
        "name":"sujan",
        "age": 23,
        "roll no": 2
    }
}
# print(marks["roll no 1"][0])
# print(len(marks))
print(marks["roll no 1"]["age"])