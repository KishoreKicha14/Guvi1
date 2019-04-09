m=input().split()
a=[]
if(len(m[0])<len(m[1])):
   l=m[0]
   r=m[1]
else:
   l=m[1]
   r=m[0]
for i in range(len(l),len(r)):
   
   for j in range(1,abs(len(l)-len(r))+1):
      
      l=l+str(j)
      
if r==m[0]:
   m[1]=l
else:
   m[0]=l
for x,y in zip(m[0],m[1]):
   a.append(x)
   a.append(y)
print("".join(a))
