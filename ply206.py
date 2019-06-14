l=0
m=input()
r=[]
for i in m:
    if(i.isupper()):
        r.append(i.lower())
    elif(i.islower()):
        r.append(i.upper())
        
print("".join(r))
