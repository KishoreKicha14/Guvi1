n=int(input())
m=input().split()
a=input()
c=0
for i in m:
   if(i[:2]==a):
      c=c+1
print(c)
