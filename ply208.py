n=int(input())
r=[]
for i in range(n):
    r.append([int(s) for s in input().split()])
l=0
re=0
le=n-1
st=0
for i in range(n):
   l=l+r[i][st]
   st=st+1
   re=re+r[i][le]
   le=le-1
print(l*re)
