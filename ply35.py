n=input()
f={}
r=[]
for i in n:
    if(i in f):
        f[i]+=1
    else:
        f[i]=1
r=min(f,key=f.get)
print(f[r])
for i in f:
    if(f[i]==f[r])and(i!=" "):
        print(i,end=" ")
