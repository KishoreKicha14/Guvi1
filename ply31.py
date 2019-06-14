m=input()
c=0
o=0
f=1
for i in m:
    if(f==1):
        if(i==')'):
            c=c+1
            if(c>o):
                f=0
        elif(i=="("):            
            o=o+1
if(f==1 and c==o):
    print("yes")
else:
    print("no")
