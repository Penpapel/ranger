import streamlit as st
import matplotlib.pyplot as plt

# Set up the title of the app
st.title("Price Calculator with Custom Base Sqft and Pie Chart")

# Entry boxes to input base square footage for each category
base1 = st.number_input("Enter Base Sqft for Category 1", min_value=0, value=1000)
base2 = st.number_input("Enter Base Sqft for Category 2", min_value=0, value=1000)
base3 = st.number_input("Enter Base Sqft for Category 3", min_value=0, value=1000)

st.write("Adjust the sliders to calculate prices based on the base sqft values.")

# Sliders to set the price multiplier for each category
slider1_value = st.slider("Price Multiplier 1 (in $)", min_value=0, max_value=100, value=50)
slider2_value = st.slider("Price Multiplier 2 (in $)", min_value=0, max_value=100, value=30)
slider3_value = st.slider("Price Multiplier 3 (in $)", min_value=0, max_value=100, value=20)

# Calculate the subtotal for each category
subtotal1 = slider1_value * base1
subtotal2 = slider2_value * base2
subtotal3 = slider3_value * base3

# Display the subtotals
st.write(f"Subtotal for Category 1: ${subtotal1}")
st.write(f"Subtotal for Category 2: ${subtotal2}")
st.write(f"Subtotal for Category 3: ${subtotal3}")

# Calculate and display the total price
total = subtotal1 + subtotal2 + subtotal3
st.write(f"**Total Price: ${total}**")

# Calculate and display the average price
average_price = total / 3
st.write(f"**Average Price: ${average_price:.2f}**")

# Pie chart to show the percentage contribution of each category to the total
if total > 0:
    labels = ['Category 1', 'Category 2', 'Category 3']
    sizes = [subtotal1, subtotal2, subtotal3]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.write("### Contribution of Each Category to the Total Price")
    st.pyplot(fig)
else:
    st.write("Enter valid square footage and price multipliers to see the pie chart.")
