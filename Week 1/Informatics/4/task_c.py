n = int(input())
arr = input().split()
cnt = 0
for i in range(n):
    if(int(arr[i]) > 0):
        cnt += 1
        
print(cnt)