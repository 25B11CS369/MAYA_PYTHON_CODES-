salary = float(input())
hra = float(input())
da = float(input())
pf = 0.12 * salary
gross_salary = salary + hra + da + pf
print(f"{pf:.2f}")
print(f"{gross_salary:.2f}")
