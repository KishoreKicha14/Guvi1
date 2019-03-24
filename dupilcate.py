n=list(map(int,input().split()))
n.sort()
d=[]
counter=1
f=0

for i in range(0,len(n)-1):
   
   if(n[i]==n[i+1]):
      if(f==0):         
         f=1
         d.append(n[i])
   else:
      
      f=0

for i in d:
   print(i,end=" ")
