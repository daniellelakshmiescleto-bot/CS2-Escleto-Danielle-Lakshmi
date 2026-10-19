# Movie Ticket Calculator (Simple Version)
TICKET_PRICE = 250

customer_name = input("Enter customer name: ")
movie_choice = input("Select movie (1: Action, 2: Comedy, 3: Horror): ")
tickets = int(input("Enter number of tickets: "))

# Simple validation check
if customer_name == "" or tickets <= 0:
    print("Error: Invalid name or ticket quantity.")
else:
    if movie_choice == "1":
        movie_title = "Action Blockbuster"
    elif movie_choice == "2":
        movie_title = "Comedy Night"
    else:
        movie_title = "Horror Fest"

    total_cost = tickets * TICKET_PRICE

    print("\nCustomer:", customer_name)
    print("Movie:", movie_title)
    print("Total Cost: PHP", round(total_cost, 2))
