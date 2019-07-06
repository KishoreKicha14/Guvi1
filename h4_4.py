from itertools import permutations
pu=permutations(input())
for i in pu:
    print("".join(list(i)))
