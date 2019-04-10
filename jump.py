n=int(input())
c=0
for i in range(n+1):
   l=str(i)
   f=0
   if i in (0,1,2,3,4,5,6,7,8,9):
      c=c+1
   for j in range(len(l)-1):
      if(abs(int(l[j])-int(l[j+1]))==1):
         f=1
      else:
         f=0
         break
   if(f==1):
      c=c+1
print(c)
      
