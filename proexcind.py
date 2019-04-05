a=[int(s) for s in input().split()]
d=[]
for i in range(len(a)):
   p=1
   for j in range(len(a)):
      if(a[i]==a[j]):
         pass
      else:
         p=p*a[j]
   d.append(p)
print(" ".join(d))
