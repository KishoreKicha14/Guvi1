def printRepeating(arr, size): 
      for i in range(0, size): 
          
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            lis.append(abs(arr[i]))
m=int(input())
n=input().split()
lis=[]
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])
printRepeating(n,m-1)
if lis==[]:
   print("unique")
else:
   print(lis[0])
