# Python program to compute US Federal Personal Income Tax for 2009 tax year
# Based on the 2009 tax brackets provided in the document

# Tax brackets for 2009
tax_brackets = {
    "single": [
        (10, 0, 8350),
        (15, 8350, 33950),
        (25, 33950, 82250),
        (28, 82250, 171550),
        (33, 171550, 372950),
        (35, 372950, float('inf'))  # Above this is 35%
    ],
    "married_joint": [  # Married Filing Jointly or Qualifying Widow(er)
        (10, 0, 16700),
        (15, 16700, 67900),
        (25, 67900, 137050),
        (28, 137050, 208850),
        (33, 208850, 372950),
        (35, 372950, float('inf'))
    ],
    "married_separate": [
        (10, 0, 8350),
        (15, 8350, 33950),
        (25, 33950, 68525),
        (28, 68525, 104425),
        (33, 104425, 186475),
        (35, 186475, float('inf'))
    ],
    "head_household": [
        (10, 0, 11950),
        (15, 11950, 45500),
        (25, 45500, 117450),
        (28, 117450, 190200),
        (33, 190200, 372950),
        (35, 372950, float('inf'))
    ]
}

def calculate_tax(income, brackets):
    """Calculate tax based on progressive brackets"""
    tax = 0
    remaining_income = income
    
    for rate, lower, upper in brackets:
        if remaining_income <= 0:
            break
        # Amount in this bracket
        taxable_in_bracket = min(remaining_income, upper - lower)
        if income > lower:
            taxable_in_bracket = min(remaining_income, upper - max(lower, income - remaining_income))
        tax += taxable_in_bracket * (rate / 100)
        remaining_income -= taxable_in_bracket
    
    return tax

def main():
    print("US Federal Income Tax Calculator (2009 Tax Year)")
    print("=" * 50)
    
    # Get filing status
    print("\nFiling Status Options:")
    print("1 - Single")
    print("2 - Married Filing Jointly or Qualifying Widow(er)")
    print("3 - Married Filing Separately")
    print("4 - Head of Household")
    
    while True:
        try:
            choice = int(input("\nEnter your filing status (1-4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Map choice to status key
    status_map = {1: "single", 2: "married_joint", 3: "married_separate", 4: "head_household"}
    status = status_map[choice]
    
    # Get taxable income
    while True:
        try:
            income = float(input("\nEnter your taxable income (in USD): $"))
            if income >= 0:
                break
            else:
                print("Income cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate tax
    brackets = tax_brackets[status]
    tax_amount = calculate_tax(income, brackets)
    
    # Display result
    print("\n" + "=" * 50)
    print(f"Filing Status: {status.replace('_', ' ').title()}")
    print(f"Taxable Income: ${income:,.2f}")
    print(f"Calculated Tax: ${tax_amount:,.2f}")
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    main()
