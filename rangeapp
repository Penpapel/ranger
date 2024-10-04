import streamlit as st

# Set up a base number for calculation (like square footage)
base_number = 1000  # Example: Square footage or any other base value

# Define ranges for each slider (you can adjust min and max as needed)
st.title("Price Calculator with Sliders")

st.write("Adjust the sliders to calculate prices based on the base number.")

# Slider 1
slider1_value = st.slider("Price Multiplier 1 (in $)", min_value=0, max_value=100, value=50)
subtotal1 = slider1_value * base_number
st.write(f"Subtotal 1: ${subtotal1}")

# Slider 2
slider2_value = st.slider("Price Multiplier 2 (in $)", min_value=0, max_value=100, value=30)
subtotal2 = slider2_value * base_number
st.write(f"Subtotal 2: ${subtotal2}")

# Slider 3
slider3_value = st.slider("Price Multiplier 3 (in $)", min_value=0, max_value=100, value=20)
subtotal3 = slider3_value * base_number
st.write(f"Subtotal 3: ${subtotal3}")

# Display the total subtotal
total = subtotal1 + subtotal2 + subtotal3
st.write(f"Total: ${total}")

# Separate tab for displaying the average price
st.write("## Average Price")
average_price = total / 3
st.write(f"Average Price: ${average_price}")
