numbers = []
while len(numbers) < 3:
    numbers.extend(map(int, input().split()))
X, Y, Z = numbers
max_mangoes = (Z - Y) // X
print(max_mangoes)
