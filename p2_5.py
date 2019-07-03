b =[int(s) for s in input().split()]
ml=1
l=1
for i in range(1,len(b)):
    
    if(b[i]>b[i-1]):
        l=l+1
    else:
        if(l>ml):
            ml=l
            l=1
if(l>ml):
    ml=l
print(ml)
