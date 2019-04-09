n=int(input())
m=[int(s) for s in input().split()]
freq = {} 
for item in m:
   if (item in freq):
      freq[item] += 1
   else:
      freq[item] = 1
key_max = max(freq.keys(), key=(lambda k: freq[k]))
print(key_max)
