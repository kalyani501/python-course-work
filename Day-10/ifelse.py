'''username=input("Enter Username: ")
Password=input("Enetr Password: ")
if username == 'admin' and Password == 'admin123':
    print("login succesuful")
else:
    print("invalid credentials")
    '''
'''products=["Laptop","Mobile","bag","bottle"]
searchproducts=input("Enter a product: ")
if searchproducts in products:
    print(f"{searchproducts} found")
else:
    print(f"{searchproducts} not found")'''
bill=int(input("Eneter the bill: "))
if bill>90:
    print(f"final bill amount  {bill}")
else:
    print(f"final bill + charges {bill+30}")