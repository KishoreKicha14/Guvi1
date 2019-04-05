a=[]
def rev(n):
   str=""
   for i in n:
      str=i+str
   a.append(str)
n=input().split()
str=""
for i in n:
   rev(i)
print(" ".join(a))
