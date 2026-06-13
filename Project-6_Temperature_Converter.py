print("Temperature Converter")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("4.Kelvin to Celsius")

temperature = float(input("Enter Temperature: "))
choice = input("enter choice (1/2/3/4): ")
if choice == "1":
    result = (temperature * (9/5)) + 32
    print(f"Temperature in Fahrenheit: {result:.2f}F")
elif choice == "2":
    result = (5/9)* (temperature - 32)
    print(f"Temperature in Celsius:.2f : {result:.2f}C")
elif choice == "3":
    result = temperature +273.15
    print(f"Temperature in Kelvin: {result}K")
elif choice == "4":
    result = temperature - 273.15
    print(f"Temperature in Celsius : {result}C")
else:
    print("invalid choice")
