m=int(input())
n=input().split()
list=[]
for i in range(0,m):
   list.append(int(n[i]))
list.sort(reverse=True)
for i in list:
   print(i,end="")
