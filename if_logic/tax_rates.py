# federalTax.py
# 27 January 2025
# prof. lehman
# demonstrates nested if logic with updated 2024 tax rates
# filing as "single"
#
# see online calculator at https://www.nerdwallet.com/calculator/tax-calculator
# see tax tables at https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets

# federal tax rates (2024)
# 0 to 11,600 - 10%
# 11,601 to 47,150 - 12%
# 47,151 to 100,525 - 22%
# 100,526 to 191,950 - 24%

# Standard deduction for single filers (2024)
STANDARD_DEDUCTION = 14600

# input
print("Enter income:")
income = int(input())

# account for standard deduction
income = income - STANDARD_DEDUCTION

# processing
total_tax = 0
effective_rate = 0
marginal_rate = 0

# nested if-else statements (up to the 24% bracket)
if income <= 11600:
    total_tax = income * 0.10
    marginal_rate = 0.10
else:
    total_tax += (11600 - 0) * 0.10  # tax at first level
    if income <= 47150:
        total_tax += (income - 11600) * 0.12
        marginal_rate = 0.12
    else:
        total_tax += (47150 - 11600) * 0.12  # tax at second level
        if income <= 100525:
            total_tax += (income - 47150) * 0.22
            marginal_rate = 0.22
        else:
            total_tax += (100525 - 47150) * 0.22  # tax at third level
            if income <= 191950:
                total_tax += (income - 100525) * 0.24
                marginal_rate = 0.24
            else:
                print("Error: income out of range > 191,950")

# calculate effective rate
effective_rate = total_tax / income

# output
print()
print(f"         Total Tax: ${total_tax:,.2f}")
print(f"Effective Tax Rate: {effective_rate * 100:.2f}%")
print(f" Marginal Tax Rate: {marginal_rate * 100:.2f}%")
print()


# **************************
# *** alternate approach ***
# **************************

# reset outputs
total_tax = 0
effective_rate = 0
margional_rate = 0

# pre-calculate tax amounts at each range
tax_a = (11600 - 0) * .10       #
tax_b = (47150 - 11600) * .12
tax_c = (100525 - 47150) * .22
tax_d = (191950 - 100525) * .24

#print( tax_a )
#print( tax_b )
#print( tax_c )
#print( tax_d )

# elif statements
if income <= 11600:
    total_tax = income * .1
    margional_rate = .1  
    
elif income <= 47150:
    total_tax = tax_a + (income - 11600) * .12
    margional_rate = .12
    
elif income <= 100525:
    total_tax = tax_a + tax_b + (income - 47150) * .22
    margional_rate = .22
    
elif income <= 191950:
    total_tax = tax_a + tax_b + tax_c + (income - 100525) * .24
    margional_rate = .24

else:
    print("Error: income out of range <= 191950")

# calculate effective rate
effective_rate = total_tax / income

# output
print()
print(f"         Total Tax: ${total_tax:,.2f}")
print(f"Effective Tax Rate: {effective_rate * 100:.2f}%")
print(f" Marginal Tax Rate: {marginal_rate * 100:.2f}%")
print()