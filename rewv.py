m=int(input())
n=input()
a=""
for i in n:
   if(i not in ('a','i','e','o','u','A','I','E','O','U')):
      a=i+a
print(a)
   
