n,p,q,r=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
ma=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            m=p*a[i]+q*a[j]+r*a[k]
            if m>ma:
                ma=m
print(m)
