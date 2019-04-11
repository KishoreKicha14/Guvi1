r=int(input())
sum=0
m=[]
for i in range(r):
   m.append([int(s) for s in input().split()])
   sum=sum+m[i][i]
print(sum)
