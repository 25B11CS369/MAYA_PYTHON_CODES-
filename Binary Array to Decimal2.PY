n = int(input())
arr = list(map(int, input().split()))

result = 0
for bit in arr:
    result = result * 2 + bit

print(result)
