N = int(input())
arr = list(map(int, input().split()))
odd_sum = sum(num for num in arr if num % 2 != 0)
print(odd_sum)
