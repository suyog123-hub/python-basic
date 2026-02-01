import datetime
def get_current_time():
    t = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    return t

def add(num1,num2):
    res=f'{num1} + {num2} = {num1+num2}'
    gtime= get_current_time()
    print(res)
    return gtime+' | '+ res

def sub(num1,num2):
    res=f'{num1} - {num2} = {num1-num2}'
    gtime= get_current_time()
    print(res)
    return gtime+' | '+ res

def div(num1,num2):
    res=f'{num1} / {num2} = {round(num1/num2,2)}'
    gtime= get_current_time()
    print(res)
    return gtime+' | '+ res

def mul(num1,num2):
    res=f'{num1} X {num2} = {num1*num2}'
    gtime= get_current_time()
    print(res)
    return gtime+' | '+ res

def inp_num():
    num1=int(input("Enter Th eNumber 1 : "))
    num2=int(input("Enter Th eNumber 1 : "))
    return num1,num2

def write_f(string):
    with open(r'/Users/suyogkhadka/Desktop/untitled folder/file_h_python/file_h.txt','a') as file:
        file.write(string)
        file.write('\n')
        

while True:
    print(f'''
    1--> Add
    2--> Sub
    3--> Div
    4--> Mul
    5--> Exit
    ''')
    user_c=input("Enter your Choice : ")
    if user_c=='1':
        num1,num2=inp_num()
        write_f(add(num1,num2))
        
    elif user_c=='2':
        num1,num2=inp_num()
        write_f(sub(num1,num2))
        
    elif user_c=='3':
        num1,num2=inp_num()
        write_f(div(num1,num2))
        
    elif user_c=='4':
        num1,num2=inp_num()
        write_f(mul(num1,num2))
        
    elif user_c=='5':
        break
    else:
        print(" !!!!!! invalid User Input ")