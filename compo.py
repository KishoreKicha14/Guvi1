num = 11
if num > 1:  
   for i in range(2, num//2): 
       if (num % i) == 0: 
           print(num, "yes") 
           break
   else: 
       print(num, "no") 
 else: 
   print(num, "yes") 
