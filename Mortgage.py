# Mortgage 

loan_amount = 270000
annual_interest_rate = 0.04
loan_term_years = 30
monthly_interest_rate = annual_interest_rate / 12
number_of_payments = loan_term_years * 12
monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)
print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")