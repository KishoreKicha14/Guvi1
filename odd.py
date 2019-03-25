n=input().split()
list=[]
for i in range(int(n[0])+1,int(n[1])):
   if(i%2==1):
      list.append(str(i))
print(" ".join(list)) 
