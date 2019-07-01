n=input()
f=0
for i in n:
    if(int(i) in (1,0)):
        pass
    else:
        f=1
        break
if(f==1):
    print("no")
else:
    print("yes")
