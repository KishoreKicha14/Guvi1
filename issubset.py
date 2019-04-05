n=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
b=[int(s) for s in input().split()]
A=set(a)
B=set(b)
if(B.issubset(A)):
   print("YES")
else:
   print("NO")

