print("currency converter")
amount = float(input("Enter amount: "))
from_currency = input("Enter source currency(USD/INR/EUR): ").upper()
to_currency = input("Enter target currency(INR/USD/EUR): ").upper()

if from_currency == "USD" and to_currency == "INR":
    result = amount * 83
elif from_currency == "INR" and to_currency == "USD":
    result = amount / 83
elif from_currency == "EUR" and to_currency == "INR":
    result = amount * 90
elif from_currency == "INR" and to_currency == "EUR":
    result = amount / 90
elif from_currency == "USD" and to_currency == "EUR":  
    result = amount * 0.85      
elif from_currency == "EUR" and to_currency == "USD":    
    result = amount / 0.85

else:
    print("Invalid currency choice")
print("Converted amount =", f"{result:.2f}", to_currency)


