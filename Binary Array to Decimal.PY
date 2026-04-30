n = int(input())
arr = list(map(int, input().split()))
decimal = 0
for i in range(n):
    decimal = decimal * 2 + arr[i]
print(decimal)
