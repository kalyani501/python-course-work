#from 1 to 10
'''i=1
while i<=10:
    print(i)
    i+=1'''
#from 10 to 1
'''i=10
while i>0:
    print(i)
    i-=15'''
#factors of 5
'''i=5
while i<=20:
    print(i)
    i+=5'''
#print string(to iterate a string we are using indexing)
'''s="python programming"
i=0
while i<len(s):
    print(s[i])
    i+=1'''
#print reverse of a string
'''s='python whith dsa'
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1'''
#list
'''l=[23,789,456,678]
i=0
while i<len(l):
    print(l[i])
    i+=1'''
'''n=8765
sum=0
while  n>0:
    sum +=n%10
    n//=10
print(sum)'''
#product of digits
'''n=123
pro=1
while n>0:
    pro*=n%10
    n//=10
print(pro)'''
#reverse of a number
'''n=4546
res=0
while n>0:
    res=res*10+n%10
    n//=10
print(res)'''

#give sum for only even numbers
'''n=234568
res=0
while n>0:
    rem =n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)'''

#remove zeros
'''l=[3,4,0,9,8,0,4,0,2,9,0,8]
while 0 in l:
    l.remove(0)
print(l)'''
#addition of first and last
'''l=[2,3,6,76,12,4,1,5,61,4,5,2,23]
i,j=0,len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
        i+=1
        i-=1'''

data={
    'salt':20,
    'chilli powder':80,
    'oil':180,
    'sugar':45,
    'cofee':200,
    'dal':175,
    'milk':30,
    'peanuts':180,
    'rice':80,
    'wheatflour':79,
    'eggs':190,
}
print(data)
bill=0
while True:
        products=input("Enter product name or [E]xit: ")
        if products=='E' or products=='e':
            print("Thanks for shopping")
            print("Total bill",bill)
            break
        else:
            quantity=int(input("Enter quantity"))
            bill+=data[products]*quantity
            

