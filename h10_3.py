n=input().split()
m=[]
for i in n:
    r=[]
    for j in range(len(i)):
        if(j%2==0):
            r.append(i[j].capitalize())
        else:
            r.append(i[j])
    m.append("".join(r))
print(" ".join(m))  
