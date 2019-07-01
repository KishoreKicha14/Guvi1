n=input()
r=[]
q=[]
for i in range(len(n)):
    if i%2==0:
        r.append(n[i])
    else:
        q.append(n[i])
print("".join(r),"".join(q))
