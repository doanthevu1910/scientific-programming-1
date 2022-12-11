import math
import matplotlib.pyplot as plt

# Calculate the function y = x^x for a range of x-values
x_values = [x / 100 for x in range(0, 151)]
y_values = [math.pow(x, x) for x in x_values]

# Calculate the minimum of the function
min_y = y_values[0]
min_x = x_values[0]
for i in range(1, len(y_values)):
    if y_values[i] < min_y:
        min_y = y_values[i]
        min_x = x_values[i]

# Plot the graph of the function
plt.plot(x_values, y_values, 'b')

# Indicate the minimum in the graph
plt.plot(min_x, min_y, 'ro')
plt.text(0.4, 1.3, f"(xmin, ymin) = ({min_x:.2f}, {min_y:.2f})")

# Show the graph
plt.show()

# Print the minimum
print(f"(xmin, ymin) = ({min_x:.2f}, {min_y:.2f})")
