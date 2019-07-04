m=[]
f=0
def find_dist(a,b):
    k=(a[0]-b[0])**2
    l=(a[1]-b[1])**2
    d=(k+l)**0.5
    m.append(d)
n=[]
for i in range(4):
    r=[int(s) for s in input().split()]
    n.append(r)
for i in range(4):
    if(i!=3):
        find_dist(n[i],n[i+1])
    else:
        find_dist(n[i],n[0])
for i in range(1,4):
    if(m[0]!=m[i]):
        f=1
        break
if(f==1):
    print("no")
else:
    print("yes")
