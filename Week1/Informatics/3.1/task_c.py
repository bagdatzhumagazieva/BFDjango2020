import math
a = int(input())
b = int(input())

for i in range(a,b+1):
    y = float(math.sqrt(i))
    x = int(math.sqrt(i))
    if(x == y):
        print(str(i)+" ")
    else:
        print("")