m=int(input())
r=[]
r.append(str(1))
r.append(str(1))
a=1
b=1
for i in range(m-2):
    t=a+b
    b=a
    a=t
    r.append(str(a))
print(" ".join(r))
