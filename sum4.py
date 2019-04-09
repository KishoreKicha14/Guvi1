m=int(input())
a=[int(s) for s in input().split()]
c=0
for i in range(m):
   for j in range(m):
      for k in range(m):
         if(a[i]+a[j]==a[k])and(i<j<k):
            c=c+1

print(c)
      
