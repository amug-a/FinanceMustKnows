# Fixed Mortage Payment Based On Principal At Sign Up

loan_amount = float(input("Enter Loan Amount After Down Payment: "))
annual_interest_rate = float(input("Enter Annual Interest Rate: "))/100
loan_term_years = int(input("Enter Compound Years: "))
monthly_interest_rate = annual_interest_rate / 12
number_of_payments = loan_term_years * 12
monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)
print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")
print(f"Your monthly interest rate is: {monthly_interest_rate:.6f}% on your current Principal")