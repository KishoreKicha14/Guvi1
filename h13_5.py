n=input()
r=[]
d=[]
for i in n:
    if i not in d:
        if i in r:
            r.remove(i)
            d.append(i)
        else:
            r.append(i)
        
    
print("".join(r))
