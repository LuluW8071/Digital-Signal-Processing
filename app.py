import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
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
        math.atan2(r2 * math.sin(w + x2), 1 - r2 * math.cos(w + x2)) -
        math.atan2(r3 * math.sin(w - x3), 1 - r3 * math.cos(w - x3)) -
        math.atan2(r4 * math.sin(w + x4), 1 - r4 * math.cos(w + x4))
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
    st.pyplot(fig)

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
    st.pyplot(fig)

def main():
    st.title("Frequency Response Calculator")

    st.sidebar.header("Input Parameters")
    
    r1 = st.sidebar.number_input("r1", value=2.14)
    r2 = r1
    x1 = st.sidebar.number_input("x1", value=1.29)
    x2 = x1
    r3 = st.sidebar.number_input("r3", value=0.477)
    r4 =  r3
    x3 = st.sidebar.number_input("x3", value=0.34)
    x4 = x3

    w_values = [i * math.pi / 4 for i in range(9)]

    if st.sidebar.button("Calculate"):
        magnitude_values = [calculate_magnitude(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]
        phase_result = [calculate_phase(x1, x2, x3, x4, r1, r2, r3, r4, w) for w in w_values]

        data = {
            "w (radians)": [f'{Fraction(w / math.pi).limit_denominator()}π' for w in w_values],
            "Magnitude (dB)": [f'{magnitude:.3f}' for magnitude in magnitude_values],
            "Phase (radians)": [f'{phase:.3f}' for phase in phase_result]
        }
        df = pd.DataFrame(data)
        st.table(df)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        ax1.plot(w_values, magnitude_values, marker='o', label='Magnitude')
        ax1.set_xticks(w_values)
        ax1.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
        ax1.set_xlabel('w (radians)')
        ax1.set_ylabel('Magnitude (dB)')
        ax1.set_title('Magnitude vs. w')
        ax1.grid(True)

        ax2.plot(w_values, phase_result, marker='o', color='orange', label='Phase')
        ax2.set_xticks(w_values)
        ax2.set_xticklabels([f'{Fraction(w/math.pi).limit_denominator()} π' for w in w_values])
        ax2.set_xlabel('w (radians)')
        ax2.set_ylabel('Phase (radians)')
        ax2.set_title('Phase vs. w')
        ax2.grid(True)

        for x, y in zip(w_values, magnitude_values):
            ax1.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        for x, y in zip(w_values, phase_result):
            ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        ax1.legend()
        ax2.legend()

        st.pyplot(fig)

if __name__ == "__main__":
    main()
