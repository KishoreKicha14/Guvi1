n=input()
try:
   f=0
   m=n.split("@")
   for i in m[0]:
      if i ==".":
         f=1
         break
   if(len(m)!=2):      
      print("NO")
   else:
      r=m[1].split(".")
      if(len(r)==2 and len(m[0])>=3 and len(r[0])>=3 and r[1]=="com" and f==0):
         print("YES")
      else:
         print("NO")
      
   pass
except:
   print("NO")
