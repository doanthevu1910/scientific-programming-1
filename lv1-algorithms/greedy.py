# Define the values of the coins in cents
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1


# Function to calculate the minimum number of coins required for a given amount of change
def min_num_coins(change):
    # Initialize the number of coins to 0
    num_coins = 0

    while change > QUARTER:
        # Calculate the number of quarters required and subtract their value from the change
        num_coins += change // QUARTER
        change -= (num_coins * QUARTER)

    while QUARTER > change > DIME:
        # Calculate the number of dimes required and subtract their value from the change
        num_coins += change // DIME
        change -= (num_coins * DIME)

    while DIME > change > NICKEL:
        # Calculate the number of nickels required and subtract their value from the change
        num_coins += change // NICKEL
        change -= (num_coins * NICKEL)

    while NICKEL > change > PENNY:
        # Calculate the number of pennies required and subtract their value from the change
        num_coins += change // PENNY
        change -= (num_coins * PENNY)

    return num_coins


# Prompt the user to enter the amount of change owed
change_owed = float(input("How much change is owed?"))

# Calculate the minimum number of coins required
min_coins = min_num_coins(change_owed * 100) + 2

# Print the result
print("The minimum number of coins required is:", int(min_coins))