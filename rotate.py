n=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
for j in range(n[1]):
   for i in range(n[0]-1):
      t=a[i]
      a[i]=a[i+1]
      a[i+1]=t 
print(a)
