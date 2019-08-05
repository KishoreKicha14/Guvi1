x,y=[int(s) for s in input().split()]
def isPower (x, y):  
    if (x == 1): 
        return (y == 1) 
    pow = 1
    while (pow < y): 
        pow = pow * x 
    return (pow == y)
if(isPower(y,x)==1):
    print("yes")
else:
    print("no")
