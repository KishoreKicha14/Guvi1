n=int(input())
for i in range(2**n):
    s=str(bin(i))
    print((s[2:]).zfill(n))
