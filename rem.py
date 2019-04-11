n=[int(s) for s in input().split()]
s=[int(s) for s in input().split()]
c=0
for i in s:
   if(i==n[1]):
      c=c+1
for i in range(c):
   s.remove(n[1])
if(s==[]):
   print("empty")
else:
   for i in range(n[0]-c):

      s[i]=str(s[i])
   print(" ".join(s))
