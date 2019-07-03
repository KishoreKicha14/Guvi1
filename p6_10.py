n=int(input())
f=3
m=3
t=1
for i in range(n-1):
    if(f==1):
        f=m*2
        m=f
    else:
        f=f-1
print(f)   
