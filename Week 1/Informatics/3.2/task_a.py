import math
a = int(input())
i = 1
while(i <= a):
    c = int(math.sqrt(i))
    d = float(math.sqrt(i))
    if(c == d):
        print(i)
    i += 1