n=int(input())
m=[int(s) for s in input().split()]
a=max(m)
b=min(m)
for i in range(n):
   if(a==m[i]):
      a1=i+1
   if(b==m[i]):
      b1=i+1
r=[str(b1),str(a1)]
print(" ".join(r))
