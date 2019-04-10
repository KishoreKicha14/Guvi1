m=int(input())
n=[int(s) for s in input().split()]
a=n[0]
d=[]
for i in range(1,len(n)):
   if(a>n[i]):
      d.append(n[i])
   else:
      d.append(-1)
   a=n[i]
d.append(-1)
for i in range(m):
   d[i]=str(d[i])
print(" ".join(d))
