from itertools import combinations_with_replacement,permutations
n=int(input())
# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([0,1], n)
f=[]
# Print the obtained combinations 
for i in list(comb): 
    p=permutations(list(i))
    for j in list(p):
        if(j not in f):
            f.append(j)
            m=list(j)
            r=[]
            for k in m:
                r.append(str(k))
            print("".join(r))
