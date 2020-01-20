n = int(input())
a = int(n % 4)
b = int(n % 100)
c = int(n % 400)
if ((a == 0 and b != 0) or (c == 0)):
    print("YES")
else:
    print("NO")