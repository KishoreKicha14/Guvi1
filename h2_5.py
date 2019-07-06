n=int(input())
m=[int(s) for s in input().split()]
r=[]
s=[]
for i in range(n-1):
    if(m[i]>m[i+1]):
        r.append(str(m[i]))
        if(m[i]>m[i-1])and(i!=0):
            s.append(str(m[i]))
r.append(str(m[n-1]))
print(" ".join(r))
print(" ".join(s))
    
