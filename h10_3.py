n=input().split()
c=0
m=[]
for i in n:
    r=[]
    for j in range(len(i)):
        if(c%2==0):
            r.append(i[j].capitalize())
        else:
            r.append(i[j])
        c=c+1
    m.append("".join(r))
print(" ".join(m))  
