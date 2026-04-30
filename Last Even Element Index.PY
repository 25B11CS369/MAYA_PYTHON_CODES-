n = int(input())
arr = list(map(int, input().split()))
last_index = -1
for i in range(n):
    if arr[i] % 2 == 0:
        last_index = i
print(last_index)
