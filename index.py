m=int(input())
n=input().split()
lis=[]
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])
for i in range(m):
   if(i%2==0 and n[i]%2==1)or(i%2==1 and n[i]%2==0):
      lis.append(str(n[i]))
print(" ".join(lis))
