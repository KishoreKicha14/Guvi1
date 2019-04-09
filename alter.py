n=int(input())
a=[int(s) for s in input().split()]
a.sort(reverse=True)
b=a[1:]
for i in range(1,n):
   t=a[i]
   a[i]=a[n-1]
   a[n-1]=t
   if(i%2==0):
      b=a[i:]
      b.sort(reverse=True)
      a= a[:i]+b  
for i in range(n):
   a[i]=str(a[i])
print(" ".join(a))


