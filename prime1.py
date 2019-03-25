n=input().split()
list=[]
for i in range(int(n[0])+1,int(n[1])):
   f=0
   for j in range (2,i//2):
      if(i%2==0):
         f=1
         break
   if f==0:
      list.append(str(i))
print(" ".join(list))
