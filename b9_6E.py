n=input()
r=[]
f=1
for i in n:
    if(i in r):
        print("no")
        f=0
        break
    else:
        r.append(i)
if(f==1):
    print("yes")
