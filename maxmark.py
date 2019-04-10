n=input().split('#')
a=input().split('#')
sum1=int(n[1])+int(n[2])+int(n[3])
sum=int(a[1])+int(a[2])+int(a[3])
if(sum>sum1):
   print(a[0])
else:
   print(n[0])
