n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n):
    left = arr[(i-1) % n]
    right = arr[(i+1) % n]

    if (left % 2 == 0 and right % 2 != 0) or (left % 2 != 0 and right % 2 == 0):
        count += 1

print(count)
