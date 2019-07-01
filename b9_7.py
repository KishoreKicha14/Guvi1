n=[int(s) for s in input().split()]
l=n[0]
m=n[1]
while(l%m!=0):
    r=l%m
    l=m
    m=r
print(m)  
