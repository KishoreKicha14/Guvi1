n=[str(s) for s in input()]
c=0
d=[]
for i in range(len(n)-1):
   if(n[i]==n[i+1]):
      c=c+1
      if(i==len(n)-2):
         c=c+1
         g=[c,n[i]]
         d.append(g)
   else:      
      c=c+1
      g=[c,n[i]]
      d.append(g)
      c=0
      if(i==len(n)-2):
         c=c+1
         g=[c,n[i+1]]
         d.append(g)
m=max(d)
n=[m[1],str(m[0])]
print(" ".join(n))
