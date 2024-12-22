# Compund Interest
principal_amt = float(input("Enter Principal Amt: "))
annual_interest_rate = float(input("Enter Annual Interest Rate: "))/100
compound_years = int(input("Enter Compound Years: "))
amount_after_compound_years = principal_amt * (1 + annual_interest_rate)**compound_years
print(f"Total amound after these years is: ${amount_after_compound_years:.2f}")



