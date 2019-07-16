def kadane(A):
    c=A[0]
    g=A[0]
    for i in range(1,len(A)):
        c=max(A[i],c+A[i])
        if c>g:
            g=c
    return g
m=int(input())
n=[int(s) for s in input().split()]
j=kadane(n)
print(j)
