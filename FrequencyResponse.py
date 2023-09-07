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

def plot_magnitude(w_values, magnitude_values):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(w_values, magnitude_values, marker='o', label='Magnitude')
    ax.set_xticks(w_values)
    ax.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
    ax.set_xlabel('w (radians)')
    ax.set_ylabel('Magnitude(dB)')
    ax.set_title('Magnitude vs. w')
    ax.grid(True)

    # Add Y-axis values near each marker
    for x, y in zip(w_values, magnitude_values):
        ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    ax.legend()
    plt.tight_layout()
    plt.show()

def plot_phase(w_values, phase_result):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(w_values, phase_result, marker='o', color='orange', label='Phase')
    ax.set_xticks(w_values)
    ax.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
    ax.set_xlabel('w (radians)')
    ax.set_ylabel('Phase (radians)')
    ax.set_title('Phase vs. w')
    ax.grid(True)

    # Add Y-axis values near each marker
    for x, y in zip(w_values, phase_result):
        ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    ax.legend()
    plt.tight_layout()
    plt.show()

# Take values of magnitude r1, r2, r3, r4 and radian angles x1, x2, x3, x4 as input
# Zeroes magnitude and angle
r1 = r2 = 2.14
x1 = x2 = 1.29

# Poles magnitude and angle
r3 = r4 = 0.477
x3 = x4 = 0.34

print("Select an option:")
print("1. Calculate Magnitude Response")
print("2. Calculate Phase Response")
print("3. Calculate Frequency Response(Both)")

choice = int(input("Enter your choice (1/2/3): "))

# Values of w in radians
w_values = [i * math.pi/4 for i in range(9)]


if choice == 1:
    # Calculate magnitudes 
    magnitude_values = [calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

    result_table = PrettyTable()
    result_table.field_names = ["w (radians)", "Magnitude (dB)"]
    for w, magnitude in zip(w_values, magnitude_values):
        fraction_w = Fraction(w / math.pi).limit_denominator()
        fraction_str = f'{fraction_w}π'
        result_table.add_row([fraction_str, f'{magnitude:.3f}'])

    print(result_table)

    plot_magnitude(w_values, magnitude_values)

elif choice == 2:
    # Calculate phase
    phase_result = [calculate_phase(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

    result_table = PrettyTable()
    result_table.field_names = ["w (radians)", "Phase (radians)"]
    for w, phase in zip(w_values, phase_result):
        fraction_w = Fraction(w / math.pi).limit_denominator()
        fraction_str = f'{fraction_w}π'
        result_table.add_row([fraction_str, f'{phase:.3f}'])
    print(result_table)

    plot_phase(w_values, phase_result)

elif choice == 3:
    # Calculate both magnitude and phase
    magnitude_values = [calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]
    phase_result = [calculate_phase(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

    result_table = PrettyTable()
    result_table.field_names = ["w (radians)", "Magnitude (dB)", "Phase (radians)"]
    for w, magnitude, phase in zip(w_values, magnitude_values, phase_result):
        fraction_w = Fraction(w / math.pi).limit_denominator()
        fraction_str = f'{fraction_w}π'
        result_table.add_row([fraction_str, f'{magnitude:.3f}', f'{phase:.3f}'])
    print(result_table)

    # Create subplots for magnitude and phase
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Plot magnitude response
    ax1.plot(w_values, magnitude_values, marker='o', label='Magnitude')
    ax1.set_xticks(w_values)
    ax1.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
    ax1.set_xlabel('w (radians)')
    ax1.set_ylabel('Magnitude (dB)')
    ax1.set_title('Magnitude vs. w')
    ax1.grid(True)

    # Plot phase response
    ax2.plot(w_values, phase_result, marker='o', color='orange', label='Phase')
    ax2.set_xticks(w_values)
    ax2.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
    ax2.set_xlabel('w (radians)')
    ax2.set_ylabel('Phase (radians)')
    ax2.set_title('Phase vs. w')
    ax2.grid(True)

    # Add Y-axis values near each marker in the magnitude subplot
    for x, y in zip(w_values, magnitude_values):
        ax1.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Add Y-axis values near each marker in the phase subplot
    for x, y in zip(w_values, phase_result):
        ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    ax1.legend()
    ax2.legend()

    plt.tight_layout()
    plt.show()
else:
    print("Invalid choice. Please select 1, 2, or 3.")