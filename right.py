N=int(raw_input())
b=1
for i in range(N):
  for j in range(N):
    print(b,end=' ')
  print("\r")
  N=N-1
