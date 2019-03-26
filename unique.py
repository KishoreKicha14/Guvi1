m=int(input())
n=input().split()
for i in range(0,m):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])
n.sort()
d=[]
f=0

for i in range(0,len(n)-1):
   
   if(n[i]==n[i+1]):
      if(f==0):         
         f=1
         d.append(n[i])
   else:
      
      f=0

for i in d:
   n.remove(i)
   n.remove(i)
print(n[0])

