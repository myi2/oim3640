def convert():
    """
    Prompts the user for an amount in USD and converts it to the equivalent amount in multiple currencies.
    """
    # Currency_Types:
    rates = {
        'eur': 0.93, 
        'gbp': 0.80,
        'cny': 7.18,
        'jpy': 148.75
    }
    ask_currency_type = float(input("Enter currency type. Options: eur, gbp, cny, and jpy: ")) 
    ask_amount_convert = float(input("Enter amount in USD: "))  
    convertion = ask_currency_type * ask_amount_convert  # 
    print(f"{ask_amount_convert} USD is equivalent to {convertion} EUR.") # Print the converted amount in EUR
# Test code to call the function
convert()


