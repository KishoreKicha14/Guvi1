n=input()
r=[]
q=[]
f=0
for i in range(65,91):
    r.append(i)
for i in range(97,122):
    q.append(i)
for x,y in zip(r,q):
    

    if(chr(x) in n)or(chr(y) in n):
        pass
    else:
        f=1
        break
if(f==1):
    print("no")
else:
    print("yes")
