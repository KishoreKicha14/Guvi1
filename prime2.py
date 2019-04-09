n=int(input())
sum=0
for val in range(2, n + 1): 
   
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else:
          m=str(val)
          l=len(m)
          if(m[l-1]=="3"):
             sum=sum+val 
print(sum)
