s = input().split()
n = input().split()
count = 0
  
for i in n:
    if i == s[1]:
        count = count + 1
print(count)
