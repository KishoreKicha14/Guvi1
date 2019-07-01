n=[int(s) for s in input().split()]
p=n[0]*n[1]
r=int(p**0.5)
if(r*r==p):
    print("yes")
else:
    print("no")
