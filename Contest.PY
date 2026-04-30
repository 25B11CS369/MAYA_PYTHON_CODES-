X, A, B = map(int, input().split())
score = A * 1 + B * 2
if score >= X:
    print("Qualify")
else:
    print("Not Qualify")
