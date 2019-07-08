n=input()
s=0
f=0
for i in n:
    if i.isdigit():
        f=1
    elif i.isalpha():
        s=1
if(s==1)and(f==1):
    print("Yes")
else:
    print("No")
