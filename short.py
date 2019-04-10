n=[str(i) for i in input()]
c=0
s=""
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
for i in d:
   if(i[0]!=1):
      s=s+str(i[0])+"*"+i[1]
   else:
      s=s+i[1]
print(s)
