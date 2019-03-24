n=int(input())

pre=""
h=input()
l1=len(h)
for i in range(0,n-1):
   m=input()
   l=len(m)
   if l1>l:
      l1=l
      
   for j in range(0,l1):
      
      if(m[j]!=h[j]):
         pre=m[:j]
         l1=len(pre)
         break
      elif(j==l1-1):
         pre=m[:l1]
   
print(pre)
