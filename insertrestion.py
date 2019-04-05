n=[int(s) for s in input().split()]
m=set(int(s) for s in input().split())
for i in range(n[0]-1):
   r=set(int(s) for s in input().split())
   m=m.intersection(r)
m=list(m)
a=[str(s) for s in m]
print(" ".join(a))
