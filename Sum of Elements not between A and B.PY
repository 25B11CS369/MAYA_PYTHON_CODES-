n = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())

total = 0

for i in arr:
    if i < A or i > B:
        total += i

print(total)
