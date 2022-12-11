# Function to print a half pyramid of a given height

height = int(input("Enter the height of the pyramid: "))

while height > 23 or height < 0:
	height = int(input("Enter the height of the pyramid: "))


def print_half_pyramid(x):
	for i in range(1, x + 1):
		for j in range(1, x + 2):
			if j <= x-i:
				print(" ", end=" ")
			else:
				print("#", end=" ")
		print("")


# Print the pyramid
print_half_pyramid(height)
