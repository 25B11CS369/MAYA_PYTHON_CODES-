N = int(input())
arr = list(map(int, input().split()))
avg = sum(arr) // N
if avg in arr:
    print("True")
else:
    print("False")
