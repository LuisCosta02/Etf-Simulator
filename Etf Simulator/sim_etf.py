def calculate_etf_future_value(initial_investment, monthly_deposit, annual_rate, years):
    """
    Calculate the future value of an ETF investment.
    
    :param initial_investment: Initial investment amount (P)
    :param monthly_deposit: Regular monthly deposit amount (D)
    :param annual_rate: Annual performance rate (as a decimal, e.g., 0.06 for 6%)
    :param years: Number of years the investment will grow (n)
    :return: Tuple containing future value of initial investment, future value of deposits, and total future value
    """
    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / 12
    
    # Total number of months
    total_months = years * 12
    
    # Future Value of the initial investment
    fv_initial_investment = initial_investment * (1 + monthly_rate)**total_months
    
    # Future Value of the regular monthly deposits (Annuity)
    fv_deposits = monthly_deposit * (((1 + monthly_rate)**total_months - 1) / monthly_rate)
    
    # Total Future Value
    total_future_value = fv_initial_investment + fv_deposits
    
    return fv_initial_investment, fv_deposits, total_future_value

# Example usage with input validation
try:
    initial_investment = float(input("Enter the initial investment amount: "))
    monthly_deposit = float(input("Enter the monthly deposit amount: "))
    annual_rate = float(input("Enter the annual performance rate (as a decimal, e.g., 0.06 for 6%): "))
    years = int(input("Enter the number of years: "))

    if annual_rate > 1:
        annual_rate = annual_rate / 100  # Convert percentage to decimal if user entered a whole number

    fv_initial, fv_deposits, fv_total = calculate_etf_future_value(initial_investment, monthly_deposit, annual_rate, years)

    print(f"\nFuture Value of the Initial Investment: ${fv_initial:,.2f}")
    print(f"Future Value of the Monthly Deposits: ${fv_deposits:,.2f}") 
    print(f"Total Future Value: ${fv_total:,.2f}")
    print(f"\nSo, after {years} years, with an initial investment of ${initial_investment:,.2f} and monthly deposits of ${monthly_deposit:,.2f}, growing at an annual rate of {annual_rate*100:.2f}%, the total future value of the investment would be approximately ${fv_total:,.2f}.")

    input("\nPress Enter to exit...")

except ValueError:
    print("Please enter valid numeric values for the inputs.")
    input("\nPress Enter to exit...")
