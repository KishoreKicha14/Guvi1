def rev(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
n=input()
if n==rev(n):
   print("yes")
else:
   print("no")
