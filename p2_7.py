x=[int(s) for s in input().split()]
n=[int(s) for s in input().split()]
m=[int(s) for s in input().split()]
s=0
v=0
k=0
for i in range(x[0]):
    s=s+n[i]
    v=v+m[i]
    if(s<=x[1]):
        k=v
print(k)
