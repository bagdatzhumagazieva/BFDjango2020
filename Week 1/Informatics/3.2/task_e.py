n = int(input())
k=1
s=2
if(n==1):
    print("0")
    exit()
i = 1
while(i<=1000000):
    if(s>=n):
        print(k)
        exit()
    else:
        k += 1
        s *= 2
    i += 1