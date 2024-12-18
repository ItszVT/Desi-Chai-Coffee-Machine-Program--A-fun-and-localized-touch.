MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,  # Cost in rupees
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 120,
    },
    "masala chai": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "tea": 10,
        },
        "cost": 40,
    },
    "filter coffee": {
        "ingredients": {
            "water": 150,
            "milk": 150,
            "coffee": 20,
        },
        "cost": 70,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
    "tea": 100,
    "sugar": 200,  # Sugar stock in grams
}

# Function to check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Function to process payment
def process_payment(drink_cost):
    """Handles payment via cash, UPI, or card."""
    global profit  # Declare global at the start
    print("Payment options: 1) Cash 2) UPI 3) Card")
    payment_method = input("Choose your payment method (1/2/3): ")

    if payment_method == "1":
        amount = int(input("Enter the amount in cash (₹): "))
        if amount >= drink_cost:
            change = amount - drink_cost
            if change > 0:
                print(f"Here’s ₹{change} in change.")
            profit += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
    elif payment_method == "2":
        print(f"Please scan the UPI QR code to pay ₹{drink_cost}.")
        print("UPI payment successful.")
        profit += drink_cost
        return True
    elif payment_method == "3":
        print(f"Processing card payment for ₹{drink_cost}...")
        print("Card payment successful.")
        profit += drink_cost
        return True
    else:
        print("Invalid payment method. Transaction canceled.")
        return False

# Function to make coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here’s your {drink_name} ☕. Enjoy!")

# Function to display the menu with prices
def display_menu():
    print("\nMenu:")
    for drink, details in MENU.items():
        print(f"{drink.capitalize()} - ₹{details['cost']}")

# Function to refill resources
def refill_resources():
    print("Refilling resources...")
    resources["water"] += 500
    resources["milk"] += 300
    resources["coffee"] += 100
    resources["tea"] += 50
    resources["sugar"] += 100
    print("Resources have been refilled!")

# Function to handle maintenance tasks
def maintenance():
    print("Performing maintenance...")
    print("Cleaning machine and checking systems...")
    print("Maintenance completed successfully!")

is_on = True

while is_on:
    display_menu()
    choice = input("\nWhat would you like? (espresso/latte/cappuccino/masala chai/filter coffee/report/refill/maintenance/off): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Tea: {resources['tea']}g")
        print(f"Sugar: {resources['sugar']}g")
        print(f"Money: ₹{profit}")
    elif choice == "refill":
        refill_resources()
    elif choice == "maintenance":
        maintenance()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            sugar_level = input("How much sugar? (low/medium/high): ").lower()
            if sugar_level == "low":
                sugar_needed = 5
            elif sugar_level == "medium":
                sugar_needed = 10
            elif sugar_level == "high":
                sugar_needed = 15
            else:
                print("Invalid choice. Defaulting to medium sugar.")
                sugar_needed = 10

            if resources["sugar"] >= sugar_needed:
                resources["sugar"] -= sugar_needed
                if process_payment(drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, there is not enough sugar.")
    else:
        print("Invalid choice. Please select from the menu.")
