def ang(n):
   sum = 0  
   temp = n
   while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
   if n == sum:
      list.append(str(n))
   

        
    

n=input().split()
list=[]
for i in range(int(n[0])+1,int(n[1])):
   ang(i)
      
      
print(" ".join(list))
