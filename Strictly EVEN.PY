n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] % 2 == 0 and i % 2 == 1:
        print(False)
        break
else:
    print(True)
