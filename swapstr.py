n=input()
l=[]
for i in n:
   l.append(i)
for i in range(0,len(n),2):
   if(i!=len(n)-1):
      t=l[i]
      l[i]=l[i+1]
      l[i+1]=t
print("".join(l))
