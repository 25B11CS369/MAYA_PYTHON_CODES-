# Input
U = int(input().strip())

# Determine cost per unit
if U <= 199:
    cost_per_unit = 1.20
elif U < 400:
    cost_per_unit = 1.40
elif U < 600:
    cost_per_unit = 1.60
elif U < 800:
    cost_per_unit = 1.80
else:
    cost_per_unit = 2.00

# Calculate bill
bill = U * cost_per_unit

# Apply surcharge
if bill > 400:
    surcharge = bill * 0.15
else:
    surcharge = 0.00

total_amount = bill + surcharge

# Output
print(f"Units Consumed: {U}")
print(f"Cost per Unit: {cost_per_unit:.2f}")
print(f"Bill: {bill:.2f}")
print(f"Surcharge: {surcharge:.2f}")
print(f"Total Amount: {total_amount:.2f}")
