def camel(s):
    return s != s.lower() and s != s.upper() and "_" not in s
s=input().split()
f=0
for i in s:
   if(camel(i)):
      f=1
   else:
      f=0
      print("no")
      break
   
if(f==1):
   print("yes")
