m=input()
sum=0
l=len(m)
for i,j in zip(m,range(len(m))):
   q=j+2
   if(j==len(m)-1):
      q=1
   r=int(i)**(q)
   sum=sum+r
print(sum)  
