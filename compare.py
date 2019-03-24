n=input().split()
list=[]
for i in n:
   list.append(i)
a=list[0]
b=list[1]
l=len(a)
l1=len(b)
le=min(l,l1)

dif=abs(l1-l)

for i in range(0,le):
     
   if(a[i]!=b[i]):
      dif=dif+1
      
print(dif)
