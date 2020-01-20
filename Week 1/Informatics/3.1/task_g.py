import math
a = int(input())
if(a==1):
    print("1")

for i in range(2,a+1):
    if(a%i == 0):
        print(str(i))
        break