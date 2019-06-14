m=input()
r=[]
for i in m:
    a=65+(ord(i)-65+3)%26
    r.append(chr(a))
print("".join(r))
