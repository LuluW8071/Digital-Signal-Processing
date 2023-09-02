import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from fractions import Fraction

# Function to calculate the magnitude
def calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w):
    magnitude = (
        10 * math.log(1 + r1**2 - 2 * r1 * math.cos(w - x1), 10) +
        10 * math.log(1 + r2**2 - 2 * r2 * math.cos(w + x2), 10) -
        10 * math.log(1 + r3**2 - 2 * r3 * math.cos(w - x3), 10) -
        10 * math.log(1 + r4**2 - 2 * r4 * math.cos(w + x4), 10)
    )
    return magnitude

# Default values of w in radians
w_values = [0, math.pi/4, 2*math.pi/4, 3*math.pi/4, 4*math.pi/4, 5*math.pi/4, 6*math.pi/4, 7*math.pi/4, 8*math.pi/4]

# Values of x1, x2, x3, x4 in radians, r1, r2, r3, r4 in degrees
x1 = 0
x2 = 0
x3 = 69.5
x4 = 69.5
r1 = 0
r2 = 0.75
r3 = 0.5
r4 = 0.5

# Calculate magnitudes and create a list of points
magnitude_values = [calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

# Create a pretty table
table = PrettyTable()
table.field_names = ["w", "Magnitude"]
for w, magnitude in zip(w_values, magnitude_values):
    fraction_w = Fraction(w / math.pi).limit_denominator()
    fraction_str = f'{fraction_w}π'
    table.add_row([fraction_str, f'{magnitude:.3f}'])

# Print the pretty table
print(table)

# Plot the points and join them from 0 to 8*pi/4
plt.plot(w_values, magnitude_values, marker='o')
plt.xlabel('w (radians)')
plt.ylabel('Magnitude')
plt.title('Magnitude vs. w')
plt.grid(True)
plt.show()
