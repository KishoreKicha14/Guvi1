def catalan(n):
    if n<=1:
        return 1
    res =0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
        print(res,i)
    return res
for i in range(4):
    r.append(str(catalan(i)))
print(" ".join(r))
