m=input()
sum=0
a=""
for i in m:
   sum=sum+int(i)
for i in str(sum):
   a=i+a
if str(sum)==a:
   print("yes")
else:
   print("no")
