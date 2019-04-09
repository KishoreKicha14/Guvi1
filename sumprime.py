def prime(n):
   if n < 1:
      return(False)
   else:
      for i in range(2,n):
         if (n % i) == 0:
            return(False)
            break
         else:
            return(True)

c=0
n=[int(s) for s in input().split()]
for i in(n[0],n[1]+2):
   for j in range(i+1,n[1]+2):
      if(prime(i+j)):
         c=c+1
print(c)
      
