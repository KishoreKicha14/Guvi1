d=[]
def push(n):
   d.insert(0,n)
def pop():
   d.pop()
a=input()
for i in a:
   push(i)
d="".join(d)
if(a==d):
   print("YES")
else:
   print("NO")
