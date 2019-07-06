n=[int(s) for s in input().split()]
m=[]
r=[]
for i in range(n[1]):
    k=[int(s) for s in input().split()]
    k.sort()
    m.append(k)
for i in range(n[0]):
    l=[]
    for j in range(n[1]):
        l.append(m[j][i])
        l.sort()
    r.append(l)
m=[]
for i in range(n[1]):
    l=[]
    for j in range(n[0]):
      l.append(str(r[j][i]))
    m.append(l)        
for i in m:
    print(" ".join(i))
