m=int(input())
n=input().split()
for i in range(m):
   n.insert(i,int(n[i]))
   
   n.remove(n[i+1])

n.sort()
'''
for i in range(m):
   n.insert(i,str(n[i]))
   
   n.remove(n[i+1])
n=" ".join(n)
'''
if(m%2==1):
   l=m//2
   print(n[l])
else:
   l=(m//2)-1
   print((n[l]+n[l+1])/2)
