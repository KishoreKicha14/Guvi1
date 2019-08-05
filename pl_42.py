
n=int(input())
a=[int(s) for s in input().split()]
b=[]
for i in range(len(a)):
    b.append(a[i])
b.sort()
if a==b:
    print("yes")
else:
    print("no")
