m=input()
sum=0
for i,j in zip(m,range(len(m))):
   sum=sum+int(i)**j
print(sum)  
