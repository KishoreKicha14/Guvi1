n=input()
r=[]
q=[]
for i in n:
    r.append(ord(i))
r.sort()
for i in range(len(r)):
    q.append(chr(r[i]))
print("".join(q))
