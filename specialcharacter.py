m=input()
l=len(m)
c=0
for i in range(l):
      if m[i].isalnum()or m[i].isspace():
         pass
      else:
         c=c+1
print(c)
