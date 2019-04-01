n=int(input())
m=input().split()
for i in range(0,len(m)):
      m.insert(i,int(m[i]))
      m.remove(m[i+1])
for i in range(n-1):
   r=input().split()
   for i in range(0,len(r)):
      m.append(int(r[i]))
   m.sort()

for i in range(0,len(m)):
      m.insert(i,str(m[i]))
      m.remove(m[i+1])
print(" ".join(m))
