m=[int(s) for s in input().split()]
d=[]
a=[]
for i in range(m[0]):
   n=[int(s) for s in input().split()]
   d.append(n)
for i in range(m[0]):
   for j in range(m[1]):
      if(d[i][j]==0):
         f=[i,j]
         a.append(f)
for i in a:
   for j in range(m[1]):
      d[i[0]][j]=0
   for j in range(m[0]):
      d[j][i[1]]=0
for i in range(m[0]):
   for j in range(m[1]):
      d[i][j]=str(d[i][j])
      
for i in d:
   print(" ".join(i))
