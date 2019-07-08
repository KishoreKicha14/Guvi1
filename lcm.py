n=[int(s) for s in input().split()]
l=n[0]
m=n[1]
p=l*m
while(l%m!=0):
    r=l%m
    l=m
    m=r
print(p//m)  
