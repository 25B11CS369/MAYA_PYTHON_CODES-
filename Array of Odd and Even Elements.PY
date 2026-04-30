n = int(input())
arr = list(map(int, input().split()))

odd = []
even = []

for i in arr:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

result = odd + even
print(*result)
