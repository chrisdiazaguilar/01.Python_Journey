"""
To-Do

1) As a User, I should have a personalized experience so that I feel welcomed by the brand.

2) As a User, I should have errors reported in a user-friendly manner

3) As a User, I should be able to request a certain amount of tickets and be told the total cost,
so that I can determine if I want to purchase the tickets

4) As a result, I should be able to confirm my order, so that I do not accidentally purchase more
tickets than intended

5)As a User, I should not be offered tickets if there aren't any available

6) As a User, I should be shown the number of tickets left remaining, so I can
understand the importance of buying now.

7) As an owner, I should receive a service charge so that I can pay other to maintain the software
"""

TICKET_PRICE = 10

ticket_remaining = 100

SERVICE_CHARGE = 2


# Create the calculate_price function. It takes number of tickets and returns num_tickets * Ticket_PRICE
def calculate_price(number_of_tickets):
    # Create a new constant for the $2 service charge, Add the service charge to our results
    return (CustomerTicketRequest * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuously until we run of tickets
while ticket_remaining >= 1:
    # Line 26 goes over the amount of tickets remaining - To-Do #6
    print("There are {} tickets remaining.".format(ticket_remaining))

    # Gather the user's name and assign it to a new variable - To-Do #1
    CustomerName = input("Welcome to Ticket Master, lets start with your name. What is your name? ")

    CustomerTicketRequest = input("Thank you {} for choosing Ticket Master, how many tickets would you like to "
                                  "purchase? ".format(CustomerName))
    # Expect a ValueError lets use a Try block
    try:
        CustomerTicketRequest = int(CustomerTicketRequest)
        # Raise a ValueError if the request is for more tickets than are available
        if CustomerTicketRequest > ticket_remaining:
            raise ValueError("There are not enough tickets, {} tickets remaining.".format(ticket_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:
        # Calculate the price (Number of tickets multiplied by the price) and assign it to a variable. Output the
        # price - To-Do #3

        TicketCalculation = calculate_price(CustomerTicketRequest)
        print("Your total ticket cost is ${}".format(TicketCalculation))

        # Prompt user if they want to proceed. Y/N? To-Do #4, If "Yes" print out a message saying "Sold!" To confirm
        # purchase, and then decrease the amount of tickets available If "No" Thank them by name

        CustomerConfirmation = str(
            input("If you would like to continue with your purchase, type 'yes' or 'no'. ")).lower()

        if CustomerConfirmation == "yes":
            print("Thank you for choosing Ticket Master, your purchased ticket cost is ${}".format(TicketCalculation))
            ticket_remaining -= CustomerTicketRequest

        else:
            print("Thank you for choosing Ticket Master {}, please come again".format(CustomerName))

# Notify the user that the tickets are sold out
print("Thank you for choosing Ticket Master but we are sold out.")
