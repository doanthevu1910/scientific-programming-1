# Function to print a half pyramid of a given height
def print_half_pyramid(x):
	for row in range(1, x + 1):
		for space in range(1, x - row + 2):
			print(" ", end="")

		for hash in range(2, row + 1):
			print("# ", end="")

		print()


# Prompt the user to enter the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Print the pyramid
print_half_pyramid(height)
