m=int(input())
n=[int(s) for s in input().split()]
for i in range(1,len(n)):
    if(n[i]<n[i-1]):
        print(i-1)
        break
