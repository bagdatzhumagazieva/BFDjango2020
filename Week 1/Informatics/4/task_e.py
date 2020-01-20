n = int(input())
arr = input().split()
cnt = 0
for i in range(1, n):
    if((int(arr[i])>0 and int(arr[i-1])>0) or (int(arr[i])<0 and int(arr[i-1])<0)):
        cnt += 1
if(cnt == 0):
    print("NO")
else:
    print("YES")