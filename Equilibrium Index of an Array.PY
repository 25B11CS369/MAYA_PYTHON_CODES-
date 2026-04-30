t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = sum(arr)
    left_sum = 0
    index = -1
    
    for i in range(n):
        total -= arr[i]   # right side sum
        
        if left_sum == total:
            index = i
            break
        
        left_sum += arr[i]
    
    print(index)
