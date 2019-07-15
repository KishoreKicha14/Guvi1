n=[int(s) for s in input().split()]
m=[int(s) for s in input().split()]
P=n[1]
Q=n[2]
R=n[3]
max=0
for i in range(n[0]):
    for j in range(n[0]):
        for k in range(n[0]):
            s=P*m[i]+Q*m[j]+R*m[k]
            if max<s:
                max=s
print(max)
