def catalan(n):
    if n<=1:
        return 1
    res =0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
        print(res,i)
    return res
for i in range(int(input())):
    print(catalan(i))
