n=int(input())
a=[]
sum=0
for i in range(n):
   a.append([int(s) for s in input().split()])
for i in range(n):
   for j in range(n):
      sum=sum+a[i][j]
l=n**2
avg=sum/l
print('{:.6f}'.format(avg))
