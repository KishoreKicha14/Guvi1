n=input()
f=0
for i in n:
    if i in ('a',"i","e","o","u","A","I","E","O","U"):
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
