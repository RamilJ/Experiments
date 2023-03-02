def tax(additional, taxable_salary, excess_over, rate):
    annual_tax = additional + ((taxable_salary - excess_over) * rate)
    return annual_tax

def month_tax(annual_tax):
    monthly_tax = annual_tax/12
    return monthly_tax

taxable_salary = float(input("Enter your taxable salary: "))

if taxable_salary <= 250000:
    print("You are exempted to income tax.")
elif 250000 < taxable_salary <= 400000:
    annual_tax = tax(0, taxable_salary, 250000, 0.15)
    monthly_tax = month_tax(annual_tax)
    print("Your annual income tax is: ", annual_tax)
    print("Your monthly income tax is: ", monthly_tax)
elif 400000 < taxable_salary <= 800000:
    annual_tax = tax(22500, taxable_salary, 400000, 0.20)
    monthly_tax = month_tax(annual_tax)
    print("Your annual income tax is: ", annual_tax)
    print("Your monthly income tax is: ", monthly_tax)
elif 800000 < taxable_salary <= 2000000:
    annual_tax = tax(102500, taxable_salary, 800000, 0.25)
    monthly_tax = month_tax(annual_tax)
    print("Your annual income tax is: ", annual_tax)
    print("Your monthly income tax is: ", monthly_tax)
elif 2000000 < taxable_salary <= 8000000:
    annual_tax = tax(402500, taxable_salary, 2000000, 0.30)
    monthly_tax = month_tax(annual_tax)
    print("Your annual income tax is: ", annual_tax)
    print("Your monthly income tax is: ", monthly_tax)
else:
    annual_tax = tax(2202500, taxable_salary, 8000000, 0.35)
    monthly_tax = month_tax(annual_tax)
    print("Your annual income tax is: ", annual_tax)
    print("Your monthly income tax is: ", monthly_tax)