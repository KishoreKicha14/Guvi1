m=input()
r=[]
for i in range(len(m)):
    if(len(m)//2==i):
        r.append("*")
    else:
        r.append(m[i])
print("".join(r))
