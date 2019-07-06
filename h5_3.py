n=input()
r=[]
d=[]
h=[]
for i in n:
    if(i.isdigit()):
        d.append(i)
    elif(i.isalpha()):
        r.append(d)
        d=[]
        d.append(i)
r.append(d)
for i in range(1,len(r)):
    p=r[i]
    k="".join(p[1:])
    if(int(k)%2==0):
        for j in range(int(k)):
            h.append(p[0])
    else:
        h.extend(p)
print("".join(h))  
