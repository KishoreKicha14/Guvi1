n=int(input())
m=[int(s) for s in input().split()]
r=[int(s) for s in input().split()]
s=min(m)
f=max(r)
c=0
g=0
for i in range(s,f+1):
    if i in m:
        c=c+1
    if g<c:
        g=c
    if i in r:
        c=c-1
    
print(g)
