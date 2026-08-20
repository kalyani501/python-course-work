#looping statements are used to iterate or repete the sequence
#in python the looping statements are for and while when we konw the no of iterations we are using
# for loop
# while loop is when we dont kow the iteration
# in python the sequence are string,list,tuple,set and dictionary 
'''s='python programming'
for i in s:
    print(i)'''
'''l=[1,2,3,4,5]
for num in l:
    print(num)'''
'''t=('siva','kalyani','chinthamreddy')
for i in t:
    print(i)'''
'''se={123,78,4657.9876}
for num in se:
    print(num)'''
'''di={1:2,2:4,3:6,4:8,5:10,6:12}
for j in di:
    print(j,di[j])'''
#range is used to generate numeric values
#syntax for range is {for i in range(start,end+1,step)
'''for i in range(1,11,1):
    print(i)'''
'''for i in range(2,21,2):
    print(i)'''
'''for i in range(2,11,2):
    print(i)'''
'''for i in range(20,0,-1):
    print(i)'''
'''s='python programming'
for i in range(len(s)):
    print(i,s[i])'''
'''s=[67,98,567,9876,2345]
for i in range(len(s)):
    print(i,s[i])'''
'''s=('kalyani','siva','pavani')
for i in range(len(s)):
    print(i,s[i])'''
'''s=[234,456,789,567]
for i in enumerate(s):
    print(i[0],i[1],s[i[0]])'''
'''for i in range(1,11,1):
    if i==6:
        break
    print(i)'''
'''for j in range(1,16,2):
    if j==5:
        continue
    print(j)'''
'''for i in range(1,11):
    if i==4:
        continue
    print(i)'''
'''for i in range(1,11):
    if i==5:
        print(i)
else:
    print("End of the loop")'''
'''l=[1,2,3,4,5,67]
n=15
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")'''
'''pin=1234
for i in range(5):
    epin=int(input("Enter your pin: "))
    if epin==pin:
        print("login")
        break
else:
    print("try after 30 sec")
'''
n=int(input("Enter a number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
    


