n = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())

nums = []

for i in arr:
    if i < A or i > B:
        nums.append(i)

if len(nums) == 0:
    print(5)
else:
    print(max(nums))
