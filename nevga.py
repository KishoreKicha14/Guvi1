m=int(input())
n=[int(s) for s in input().split()]
s=0
for i in n:
    if(i<0):
        s=s+i
print(s)
