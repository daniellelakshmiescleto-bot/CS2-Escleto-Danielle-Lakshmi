# Movie Ticket Calculator with Proper Validation & Re-entry
TICKET_PRICE = 250

# 1. Customer name validation (loops until valid)
while True:
    customer_name = input("Enter customer name: ").strip()
    if customer_name != "":
        break
    print("Error: Customer name must not be empty.")

# 2. Movie choice validation (loops until valid)
while True:
    movie_choice = input("Select movie (1: Action, 2: Comedy, 3: Horror): ").strip()
    if movie_choice == "1":
        movie_title = "Action Blockbuster"
        break
    elif movie_choice == "2":
        movie_title = "Comedy Night"
        break
    elif movie_choice == "3":
        movie_title = "Horror Fest"
        break
    print("Error: Please choose a valid option (1, 2, or 3).")

# 3. Ticket quantity validation (loops until valid)
while True:
    try:
        tickets = int(input("Enter number of tickets: "))
        if tickets > 0:
            break
        print("Error: Number of tickets must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

# Calculation & Output
total_cost = tickets * TICKET_PRICE

print("\nCustomer:", customer_name)
print("Movie:", movie_title)
print("Total Cost: PHP", round(total_cost, 2))
