n=input()
l=len(n)
r=[]
if(l%2==0):
    m=(l-1)//2
    for i in range(l):
        if(i==m)or(i==m+1):
            r.append("*")
        else:
            r.append(n[i])
else:
    m=l//2
    for i in range(l):
        if(i==m):
            r.append("*")
        else:
            r.append(n[i])
print("".join(r))
            
