# dict task

# q no 1)
# create a simple english to nepali dictionary using python dictionary 
# allow the user to enter english word and display their nepali translation 
# handle the case where the word is not found in the dictionary 

t = {
     "suyog":"सुयोग",
     "salija": "सालिजा"
}
a=input('enter the word')
print(t.get(a,"word is not found"))

# qn no 2)
data={
   "weather": [
      {
         "id": 501,
         "main": "Rain",
         "description": "moderate rain",
         "icon": "10d"
      }
   ],
   "main": {
      "temp": 284.2,
      "feels_like": 282.93,
      "temp_min": 283.06,
}
}
print(data["main"]["temp"])
print(data["weather"][0]["description"])

#q no 3)
# Task:
# Get day name from user number input (1-7), 
# where 1 = Sunday, 
# 2 = Monday, ..., 
# 7 = Saturday

week_days={
    "1":"sunday",
    "2":"monday",
    "2":"tuesday",
    "4":"wednesday",
    "5":"thrusday",
    "6":"friday",
    "7":"saturday"
}
value=input("enter the valid data 1 to 7")
print(week_days.get(value,"invalid date"))

# qw no 4)
# Given the dictionary person = {'name': 'sujan', 'age': 23, 'city': 'Kathmandu'}, 
# add a new key-value pair 'job': 'Developer' to the dictionary. 
# Then update the value of the 'name' key to 'Ram Bahadur' and 'age' to 29.

person = {
    'name': 'sujan', 
    'age': 23,
    'city': 'Kathmandu'
    }
person.setdefault('job','Developerto the dictionary')
print(person)
b={
    'name':"ram bahadur",
    'age':'29'
}
person.update(b)
print(person)

#qw no 5)
# Given a dictionary:
# my_details = {
#     'name':'sujan',
#     'grade': 0,
#     'address':'ktm',
#     'hobbies':{
#         'sports':'running',
#         'game':'pubg',
#         'novel':'xyz',
#         'anime':'one piece',
#     },
#     'email':'sujan@gmail.com'
# }
# Change the value of 'novel' key from 'xyz' to 'Harry Potter'

my_details = {
    'name':'sujan',
    'grade': 0,
    'address':'ktm',
    'hobbies':{
        'sports':'running',
        'game':'pubg',
        'novel':'xyz',
        'anime':'one piece',
    },
    'email':'sujan@gmail.com'
}
my_details['hobbies']['novel']='harry potter'
for key,value in my_details.items():
    print(f'{key}:{value}')
