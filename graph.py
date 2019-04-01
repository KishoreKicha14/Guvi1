n=input().split()
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])

a=input().split()
for i in range(0,len(a)):
   a.insert(i,int(a[i]))
   a.remove(a[i+1])

q=[]

for i in range(n[1]):
   r=input().split()
   sum=0
   for j in range(int(r[0])-1,int(r[1])):
      sum=sum+a[j]
   q.append(sum)
for i in q:
   print(i)

