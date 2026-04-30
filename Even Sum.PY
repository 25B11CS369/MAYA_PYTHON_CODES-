N = int(input())
arr = list(map(int, input().split()))
even_sum = sum(num for num in arr if num % 2 == 0)
print(even_sum)
