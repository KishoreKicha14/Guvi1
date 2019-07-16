n=[int(s) for s in input().split()]
m=[int(s) for s in input().split()]
f=1
for i in range(n[0]):
    for j in range(n[0]):
        if i!=j:
            if n[1]==m[i]+m[j]:
                f=0
                break
if f==0:
    print('YES')
else:
    print('NO')
