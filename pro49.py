n=input()
m=input()
ln=len(n)
lm=len(m)
l=ln
c=0
p=0
for i in range(1,len(n)):
    if n[i]==n[0]:
        l=i
        break
c=ln//l
for i in range(1,c+1):
    if lm%(i*l)==0:
        p=p+1
print(p)
