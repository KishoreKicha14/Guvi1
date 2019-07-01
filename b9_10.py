n=input()
r=[]
for i in n:
    if i.isdigit():
        r.append(str(i))
print("".join(r))
