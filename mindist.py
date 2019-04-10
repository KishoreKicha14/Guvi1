d=[]
def index(n,a):
   for i in range(len(n)):
      if(a==n[i]):
         d.append(i)
m=int(input())
n=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
index(n,a[0])
index(n,a[1])
print(abs(d[0]-d[1]))
