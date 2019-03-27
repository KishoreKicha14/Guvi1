n=input().split()
m=n[0]
l=n[1]
lis=[]
k=[]
sum=0
d=[]
le=min(len(m),len(l))
gt=max(len(m),len(l))

   
for i in m:
   print(i)
   lis.append(ord(i))
for i in l:
   print(i)
   k.append(ord(i))
if gt==len(m):
   d=lis
else:
   d=k
for i in range(le):
   sum=sum+abs(lis[i]-k[i])
for i in range(le,gt):
   sum=sum+d[i]-ord('a')+1
print(sum)
