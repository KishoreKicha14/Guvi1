m=input()
n=int(m)
sum=0
for i in range(len(m)):
   l=n%10
   n=n//10
   sum=sum+l**2
print(sum)
