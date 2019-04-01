def printRepeating(arr, size): 
      for i in range(0, size): 
          
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            print (abs(arr[i]))
            break
m=int(input())
n=input().split()
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])
printRepeating(n,m-1)
