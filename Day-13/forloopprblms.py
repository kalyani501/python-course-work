#factors of n
n=int(input("Emnter a number: "))
res=[]
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(f"factors of {n} {res}")