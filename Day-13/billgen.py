#billgeneration
'''data={
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
for i in data:
    print(i.ljust(30),data[i])
pro=input("select the product: ").split()
print(pro)
bill=0
for i in pro:
    print(i.ljust(20),data[i])
    bill +=data[i]
print(f"total bill".ljust(20),bill)'''
#count repition of letter
'''s='python programming'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''

#compress
'''s='aaaaaabbbbbbbbbbyyyyssssssss'
c=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))'''




