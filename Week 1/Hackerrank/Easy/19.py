n = int(input())
results = {}
for i in range(n):
    a = input().split(' ')
    results[a[0]] = [float(x) for x in a[1:]]
name = input()
output = (results[name][0]+results[name][1]+results[name][2])/3
print ("%.2f" % output)