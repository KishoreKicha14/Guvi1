N=int(raw_input())
b=1
for i in range(0,N):
  for j in range(0,N):
    print(b,end=' ')
  print("\r")
  N=N-1
