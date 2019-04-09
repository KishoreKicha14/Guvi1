n=int(input())
sum=0
r=[]
for i in range(n):
   r.append([int(s) for s in input().split()])
   sum=sum+r[i][i]
print(sum)
