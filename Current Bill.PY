units=int(input().strip())
if units<200:
    rate=1.20
elif units<400:
    rate=1.50
elif units<600:
    rate=1.80
else:
    rate=2.00
bill=units*rate
if bill>400:
    bill+=bill*0.15   
else:
    bill+=100
print(f"{bill:.2f}")
