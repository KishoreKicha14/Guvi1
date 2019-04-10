n=[str(i) for i in input()]
f=0
d=[]
for i in range(len(n)-1):
   if(n[i]==n[i+1]):
      if(f==0):
         f=1
         g=[int(n[i]),i]
         d.append(g)
   else:
      f=0
p=min(d)
del n[p[1]]
print("".join(n)
