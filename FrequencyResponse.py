import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from fractions import Fraction

def calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w):
    magnitude = (
        10 * math.log(1 + r1**2 - 2 * r1 * math.cos(w - x1), 10) +
        10 * math.log(1 + r2**2 - 2 * r2 * math.cos(w + x2), 10) -
        10 * math.log(1 + r3**2 - 2 * r3 * math.cos(w - x3), 10) -
        10 * math.log(1 + r4**2 - 2 * r4 * math.cos(w + x4), 10)
    )
    return magnitude

def calculate_phase(x1, x2, x3, x4, r1, r2, r3, r4, w):
    phase = (
        math.atan2(r1 * math.sin(w - x1), 1 - r1 * math.cos(w - x1)) +
        math.atan2(r2 * math.sin(w - x2), 1 - r2 * math.cos(w - x2)) -
        math.atan2(r3 * math.sin(w - x3), 1 - r3 * math.cos(w - x3)) -
         math.atan2(r4 * math.sin(w - x4), 1 - r4 * math.cos(w - x4))
    )
    return phase

w_values = [0, math.pi/4, 2*math.pi/4, 3*math.pi/4, 4*math.pi/4, 5*math.pi/4, 6*math.pi/4, 7*math.pi/4, 8*math.pi/4]

# Values of magnitude r1, r2, r3, r4 and angles x1, x2, x3, x4 
r1 = 2.14
r2 = 2.14
r3 = 0.477
r4 = 0.477

x1 = 1.29
x2 = 1.29
x3 = 0.34
x4 = 0.34

# Calculate magnitudes 
magnitude_values = [calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

# Calculate phase
phase_result = [calculate_phase(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

# Create table
table = PrettyTable()
table.field_names = ["w", "Magnitude", "Phase"]
for w, magnitude, phase in zip(w_values, magnitude_values, phase_result):
    fraction_w = Fraction(w / math.pi).limit_denominator()
    fraction_str = f'{fraction_w}π'
    table.add_row([fraction_str, f'{magnitude:.3f}',f'{phase:.3f}'])

print(table)

# Create the first subplot for magnitude
fig1, ax1 = plt.subplots(figsize=(6, 4))
ax1.plot(w_values, magnitude_values, marker='o', label='Magnitude')
ax1.set_xticks(w_values)
ax1.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values]) 
ax1.set_xlabel('w (radians)')
ax1.set_ylabel('Magnitude(dB)')
ax1.set_title('Magnitude vs. w')
ax1.grid(True)

# Add Y-axis values near each marker in the magnitude subplot
for x, y in zip(w_values, magnitude_values):
    ax1.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

# Create the second subplot for phase
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(w_values, phase_result, marker='o', color='orange', label='Phase')
ax2.set_xticks(w_values)
ax2.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])  
ax2.set_xlabel('w (radians)')
ax2.set_ylabel('Phase (radians)')
ax2.set_title('Phase vs. w')
ax2.grid(True)

# Add Y-axis values near each marker in the phase subplot
for x, y in zip(w_values, phase_result):
    ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

ax1.legend()
ax2.legend()

plt.tight_layout()
plt.show()