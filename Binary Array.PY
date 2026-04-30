n = int(input())
arr = list(map(int, input().split()))
isBinary = True
for i in arr:
    if i != 0 and i != 1:
        isBinary = False
        break
print(isBinary)
