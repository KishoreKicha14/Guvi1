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
ma=[]
for i in range(n[1]):
    la=[]
    for j in range(n[0]):
      la.append(str(r[j][i]))
    ma.append(la)        
for i in ma:
    print(" ".join(i))
