cp, sp = map(int, input().split())
profit_percentage = ((sp - cp) / cp) * 100
print(f"{profit_percentage:.2f}")
