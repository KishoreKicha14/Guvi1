n=input()
m=[]
for i in n:
    if i not in m:
        m.append(i)
print("".join(m))
