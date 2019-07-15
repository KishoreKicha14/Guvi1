te1,te2=input().split()
dum=0
for i in range(0,len(te1)):
  for j in range(0,len(te2)):
    if te1[i]==te2[j]:
      dum+=1
if dum>=2:
  print("yes")
else:
  print("no")
