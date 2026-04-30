n = int(input())
arr = list(map(int, input().split()))

found = False
printed = []

for i in arr:
    if arr.count(i) == i and i not in printed:
        print(i, end=" ")
        printed.append(i)
        found = True

if not found:
    print(-1)
