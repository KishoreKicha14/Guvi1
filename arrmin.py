m=int(input())
n=input().split()
for i in range(m):
   n.insert(i,int(n[i]))
   
   n.remove(n[i+1])

n.sort()
print(n[0])
