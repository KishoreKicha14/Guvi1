n=input()
r=[]
f=1
for i in n:
    if(i in r):
        print("No")
        f=0
        break
    else:
        r.append(i)
if(f==1):
    print("Yes")
