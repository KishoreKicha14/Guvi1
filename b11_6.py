m=[int(s) for s in input().split()]
n=[int(s) for s in input().split()]
c=0
for i in n:
   if(i%2==1):
       c=c+1
   if(c==m[1]):
       print(i)
       break
