m=int(input())
a=[int(s) for s in input().split()]
d=[]
for i in range(len(a)):
   p=1
   for j in range(len(a)):
      if(i==j):
         pass
      else:
         p=p*a[j]
   d.append(p)
for i in range(len(d)):
   d[i]=str(d[i])
print(" ".join(d))
      
      
      

