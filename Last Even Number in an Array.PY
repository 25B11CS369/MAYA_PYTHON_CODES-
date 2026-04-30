n = int(input())
arr = list(map(int, input().split()))
last_even = 0
for i in arr:
    if i % 2 == 0:
        last_even = i
print(last_even)
