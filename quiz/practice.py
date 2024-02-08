def convert():
    """
    Prompts the user for an amount in USD and converts it to the equivalent amount in multiple currencies.
    """
    # Currency rates with respect to USD
    rates = {
        'eur': 0.93,
        'gbp': 0.80,
        'cny': 7.18,
        'jpy': 148.75
    }
    
    # Ask the user for the currency type
    currency_type = input("Enter currency type. Options: eur, gbp, cny, jpy: ").lower() # Convert input to lowercase to match dictionary keys
    if currency_type not in rates:
        print("Invalid currency type.")
        return
    
    # Ask the user for the amount in USD to convert
    try:
        ask_amount_convert = float(input("Enter amount in USD: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    # Perform the conversion
    conversion_rate = rates[currency_type]
    converted_amount = conversion_rate * ask_amount_convert
    
    # Print the converted amount in the chosen currency
    print(f"{ask_amount_convert} USD is equivalent to {converted_amount} {currency_type.upper()}.")
    
# Test code to call the function
convert()
