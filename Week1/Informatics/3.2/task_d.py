import math
a = int(input())
a1 = a
x = 0
i = 0
while(i <= a1):
    x += int(a%2)
    a/=2
    i += 1
if(x == 1):
    print("YES")
else:
    print("NO")