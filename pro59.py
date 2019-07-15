l,r=input().split('|')
wl=len(l)
wr=len(r)
n=input()
el=len(n)
if wl+el==wr:
    s=l+n
    print(s+"|"+r)
elif wr+el==wl:
    s=r+n
    print(l+"|"+s)
else:
    print("Impossible")
