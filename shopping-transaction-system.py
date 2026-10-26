# This program calculates the total cost of a shopping order based on user input for the order total and delivery option.
# It includes try and except blocks to handle invalid inputs and ensure that the user provides valid data.

# Constants for free delivery threshold and delivery fee
FREE_DELIVERY_THRESHOLD = 100.0
DELIVERY_FEE = 8.0

# Get user input for the order total with error handling
while True:
    # Try block to catch ValueError if the input is not a valid float
    try:
        # Get the final cost of the shopping order from the user
        order_total = float(input("Enter the final cost of the shopping order: "))
        # Check if the order total is negative and prompt the user to try again if it is
        if order_total < 0:
            print("Error: the cost can't be negative. Please try again.")
            continue
        # If the input is valid, break out of the loop
        break
    # Handle ValueeError if the input is wrong
    except ValueError:
        print("Error please enter a number, e.g. *45.50*")

# Get user input for the delivery option with error handling
while True:
    try:
        # Get the delivery option from the user and ensure it is either 'collection' or 'delivery' uses strip and lower to clean the input
        decision = input("Would you like to collect your order or have it delivered? (collection/delivery): ").strip().lower()
        if decision in ("collection", "delivery"):
            break
        print("Error: please type either 'collection' or 'delivery'.")
    except ValueError:
        print("Error: please enter a valid option.")

# Print the cost of the shopping order and the delivery option chosen by the user
print(f"The cost of the shopping order is: €{order_total:.2f}")
if decision == "collection":
    print("Items will be collected.")
elif decision == "delivery":
    if order_total >= FREE_DELIVERY_THRESHOLD:
        print("Items will be delivered for free.")
    else:
        # If the order total is less than the free delivery threshold, inform the user of the delivery fee and calculate the new total
        print(f"Items will be delivered for a fee of €{DELIVERY_FEE:.2f}.")
        print(f"Your total is: €{order_total + DELIVERY_FEE:.2f}")