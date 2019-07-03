b =[int(s) for s in input().split()]
m=1
l=1
for i in range(1,len(b)):
    
    if(b[i]>b[i-1]):
        l=l+1
    else:
        if(l>m):
            m=l
            l=1
if(l>m):
    m=l
print(m)
          
