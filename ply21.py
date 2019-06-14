n=[int(s) for s in input().split()]
m=[int(s) for s in input().split()]
k=[int(s) for s in input().split()]
if((n[0]*(m[1]-k[1])+m[0]*(k[1]-n[1])+k[0]*(n[1]-m[1]))==0):
    print("yes")
else:
    print("no")
