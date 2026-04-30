N = int(input())
arr = list(map(int, input().split()))
last_odd_index = -1
for i in range(N):
    if arr[i] % 2 != 0:
        last_odd_index = i
print(last_odd_index)
