# currency converter program 
# Build a program that converts an amount from one currency to another. For example, converting an amount in US Dollars (USD) to Euros (EUR) or vice versa.

# program will be able to convert different currency type in python 
# program will be able to convert 
# The program will prompt the user to enter an amount and specify both the source currency (the currency they have) and the target currency (the currency they want).
# USD TO NGN
# USD TO CAD
# USD TO GBP 
# USD TO CHF 
# USD TO JPY 
# USD TO AUD 
# USD TO NZD 
# USD TO KWD 
# USD TO BHD
# USD TO OMR 
# USD TO DHK 
# USD TO SEK 
# USD TO NOK 
# USD TO SGD 
# USD TO HKD
# USD TO CNY
# USD TO ILS
# USD TO AED 
# USD TO KRW 

# Recieving user input to determine the amount, currency type and code and the target currency type and code 
# we are not working with currency symbols only currency code eg USD 

print("Available currencies:USD, NGN, CAD, GBP, CHF, JPY, AUD, NZD, KWD, BHD, OMR, DHK, SEK, NOK, SGD, NOK, SGD, HKD, CNY, ILS, AED, KRW")


# function to handle amount, source currency and target currency 




# store the fixed values in a dictionary and then start pulling from the dictionary 
    
exchange_rate = {
     "USD": 1.00,
     "EUR": 0.91,    # 1 USD = 0.91 EUR
     "GBP": 0.78,    # 1 USD = 0.78 GBP
     "INR": 82.5,    # 1 USD = 82.5 INR
     "JPY": 150.2,   # 1 USD = 150.2 JPY
     
}

def currency_converter(amount, source, target ):
    if source not in exchange_rate or target not in exchange_rate:
        return "Invalid currency code "
    
    amount_in_usd = amount / exchange_rate[source]

    converted_amount = amount_in_usd * exchange_rate[target]

    return round(converted_amount, 2)

amount = float(input("INPUT THE AMOUNT FOR SOURCE CURRENCY")) 
source = (input("INPUT THE SOURCE CURRENCY CODE YOU ARE CONVERTING FROM:")).upper()
target =(input("INPUT THE TARGET CURRENCY CODE YOU ARE CONVERTING TO:")).upper()

result = currency_converter(amount, source, target)
print(f"{amount} {source} is equals to {result} {target}")














