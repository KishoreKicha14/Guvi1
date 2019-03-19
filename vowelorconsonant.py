n=input()
a=ord(n)
f=0
if (a in range(97,123))or(a in range(65,98)):
   v=[65,69,73,79,85,97,101,105,111,117]
   for i in v:
      if(i==a):
         f=1
         print(vowel)
         break
   if(f==0):
      print("Consonant")
else:
   print("invalid")
