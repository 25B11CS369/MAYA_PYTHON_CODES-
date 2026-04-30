n = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())
max_val = -1
for i in arr:
    if A <= i <= B:
        if i > max_val:
            max_val = i

print(max_val)
