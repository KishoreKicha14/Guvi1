from itertools import permutations
n=input()
p=permutations(n)
r=[]
for i in p:
    if("".join(list(i)) not in r):
        r.append("".join(list(i)))
if(len(r)==1):
    print("no")
else:
    print("yes")
