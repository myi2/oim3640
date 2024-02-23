# Pseudo-code:

# 1. Define the function with a meaningful name, such as convert_usd_to_eur.

# 2. Inside the function:
#     a. Prompt the user to enter an amount in USD (float).
#     b. Convert the entered USD amount to EUR using the conversion rate (1 USD = 0.93 EUR).
#     c. Print the converted amount in EUR.

# 3. Write a docstring at the beginning of the function to explain its purpose, inputs, and outputs.

# 4. Outside the function, call the function to test its functionality.

def convert_usd_to_eur():
    """
    Prompts the user for an amount in USD and converts it to the equivalent amount in EUR.
    """
    usd_to_eur = 0.93 # Conversion rate from USD to EUR
    usd_amount = float(input("Enter amount in USD: "))  # Prompt the user to enter an amount in USD
    eur_amount = usd_amount * usd_to_eur  # Convert the amount to EUR
    print(f"{usd_amount} USD is equivalent to {eur_amount} EUR.") # Print the converted amount in EUR
# Test code to call the function
convert_usd_to_eur()

def convert(currency_exchange):
    """
    Prompts the user for an amount in USD and converts it to the equivalent amount in multiple currencies.
    """
    # Currency_Types:
    eur = 0.93 
    gbp = 0.80
    cny = 7.18
    jpy = 148.75
        
    ask_currency_type = float(input("Enter currency type. Options: eur, gbp, cny, and jpy: ")) 
    
    currency_exchange_type = float(input("Enter amount in USD: "))  
    eur_amount = usd_amount * usd_to_eur  # Convert the amount to EUR
    print(f"{usd_amount} USD is equivalent to {eur_amount} EUR.") # Print the converted amount in EUR
# Test code to call the function
convert()