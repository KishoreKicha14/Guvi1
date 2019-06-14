m=[int(s) for s in input().split()]
n=[int(s) for s in input().split()]
f=1
for i in m:
    if(f==1):
        for j in n:
            r=0
            if(i==j):
                r=1
                break
        if(r==0):
             f=0
if(f==0):
    print("No")
else:
    print("Yes")

