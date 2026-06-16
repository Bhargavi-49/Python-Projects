items = int(input("Number of items: "))
subtotal = 0
print("------ BILL -------")
for item in range(items):
    item_name = input("Item Name: ")
    quantity = int(input("Qty: "))
    price = float(input("Price: "))
    amount = quantity * price
    subtotal += amount
    print("Amount:",amount)
    print("----------------")

print("Subtotal:",subtotal)
Discount = float(input("discount(%): "))
Tax = float(input("tax(%): "))
discount_amount = (subtotal * Discount)/100
Amount_after_discount = (subtotal - discount_amount)
tax_amount = (Amount_after_discount * Tax) / 100
total = (subtotal - discount_amount) + tax_amount
print("=========================")
print(f"Total Bill:{total:.2f}")
print("=========================")