print("=== Laundromat Service Calculator ===")
print("Enter machine size: small, medium, or large")
print("Type 'done' when finished selecting loads")

    
prices = {"small": 4.50,"medium": 6.50,"large": 9.00}

total = 0.0

while True:
        machine_size = input("Enter machine size: ")

        if machine_size == "done":
            break

        if machine_size in prices:
            price = prices[machine_size]
            total += price
            print(f"Price: ${price:.2f}")
            print(f"Current total: ${total:.2f}")
        else:
            print("Invalid size. Please enter small, medium, or large.")

    
print("=== Service Summary ===")
print(f"Subtotal: ${total:.2f}")

    
discount = 4.00 if total > 0 else 0.00
final_total = total - discount

print(f"Frequent Customer Discount: ${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for your business!")
