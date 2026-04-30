n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(1, 10):
    if arr.count(i) == i:
        count += 1

print(count)
