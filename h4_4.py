from itertools import permutations
p=permutations(input())
l=[]
for i in p:
    if(i not in l):
        print("".join(list(i)))
        l.append(i)
