n=int(input())
s=[int(i) for i in input().split()]
s.append(0)
d=[]
i=0
while(i<n):
   if(s[i+1]>s[i]):
      d.append(str(s[i+1]))
      
      i=i+1
   else:
      p=i
      for j in range(p,n):
         if(s[j+1]>s[j]):
            i=j
            break
      for j in range(p,i+1):
         d.append(str(s[i+1]))
         
      i=i+1
     
print(" ".join(d))
