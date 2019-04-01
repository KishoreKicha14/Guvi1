def hcfnaive(a,b):
   
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 
n=input().split()
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])

a=input().split()
for i in range(0,len(a)):
   a.insert(i,int(a[i]))
   a.remove(a[i+1])

q=[]

for i in range(n[1]):
   r=input().split()
   q.append(hcfnaive(a[int(r[0])-1],a[int(r[1])-1]))
for i in q:
   print(i)
