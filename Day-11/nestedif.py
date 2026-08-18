'''fa=eval(input("follow account: "))
if fa:
    cf = eval(input("close friend"))
    if cf:
        print("story visible")
    else:
        print("not in close friend")
else:
    print("first follow the account")
    '''
'''reg=eval(input("registation: "))
if reg:
    fee=eval(input("fee paid: "))
    if fee:
        print("entry confirmed")
    else:
        print("entry fee is pending")
else:
    print("registation required")
    '''
'''ls=eval(input("link active: "))
if ls:
    pg=eval(input("permission granted: "))
    if pg:
        print("file opened successfully")
    else:
        print("access denied")
else:
    print("invalid link")
    '''
data = {
    "kalyani":{"status":True,"python":88,"mysql":82,"flask":89},
    "lakshmi":{"status":False,"python":None,"mysql":None,"flask":None},
    "vishnu":{"status":True,"python":90,"mysql":98,"flask":97},
    "priyanka":{"status":True,"python":99,"mysql":98,"flask":93},
    "siva":{"status":False,"python":None,"mysql":None,"flask":None}
}
name=input("enter you name: ")
if name in data:
   if data[name]["status"]:
       sum=data[name]["python"]+data[name]["mysql"]+data[name]["flask"]
       avg=sum/3
       print(f'hello {name}')
       print(f'your avg marks is {avg}')
       if avg>=90:
           print("outstanding performanence")
       elif avg>=80:
           print("very good")
       elif avg>=70:
           print("good,work hard")
       elif avg>=35:
           print("pass,better luck next time")
       else:
           print("you failed in exam")
else:
    print(f'{name} not found')
