n=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
a=list(set(a))
a.sort(reverse=True)
print(a[n[1]-1])
