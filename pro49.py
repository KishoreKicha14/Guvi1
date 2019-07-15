n=input()
m=input()
ln=len(n)
lm=len(m)
if(ln<=lm):
    a=n
    b=m
else:
    b=n
    a=m
ml=min(ln,lm)
ml1=max(ln,lm)
l=ml
c=0
p=0
for i in range(1,len(a)):
    if a[i]==a[0]:
        l=i
        break
c=ml//l
for i in range(1,c+1):
   
    if ml1%(i*l)==0:
        p=p+1
print(p)

