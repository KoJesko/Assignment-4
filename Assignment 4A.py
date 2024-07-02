# Ask the user for the number of movie tickets they want to buy
number_of_tickets = int(input("Enter the number of movie tickets you want to buy: "))

# Define the ticket price
ticket_price = 11

# Check if the order qualifies for a bulk discount
if number_of_tickets > 20:
    ticket_price = 7

# Calculate the total price
total_price = number_of_tickets * ticket_price

# Print out the total price
print(f"The total price for the movie tickets is: ${total_price}")