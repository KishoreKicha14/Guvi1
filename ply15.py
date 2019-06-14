n=input()
f={}
for i in n:
    if(i in f):
        f[i]+=1
    else:
        f[i]=1
r=max(f,key=f.get)
print(f[r])
