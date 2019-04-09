n=input()
s=input()
n1=[]
s1=[]
r=[]
for i in n:
   n1.append(ord(i)-ord('a'))
for i in s:
   s1.append(ord(i)-ord('a'))
for i,j in zip(s1,n1):
   r.append(chr(ord('a')+(i+j)%26+1))
print("".join(r))
