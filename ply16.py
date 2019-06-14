m=input()
n=[int(i) for i in input().split()]
f={}
for i in n:
    if(i in f):
        f[i]+=1
    else:
        f[i]=1
r=min(f,key=f.get)
print(r)
