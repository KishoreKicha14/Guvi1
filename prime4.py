kk=int(input())
if kk< 1:
   
     print("no")
    
else:
   for i in range(2,kk):
       if (kk % i) == 0:
           print("no")
           break
           
   else:
       
       print("yes")
