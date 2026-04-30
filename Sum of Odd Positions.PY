N = int(input())
arr = list(map(int, input().split()))
odd_sum = sum(arr[i] for i in range(N) if i % 2 == 1)
print(odd_sum)
