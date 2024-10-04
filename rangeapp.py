import streamlit as st
import matplotlib.pyplot as plt

# Set up the title of the app
st.title("Performance venue ROM Cost Calculator")

# Entry boxes to input base square footage for each category with default values
base1 = st.number_input("Enter Base Sqft for Venue Build", min_value=0, value=20000)
base2 = st.number_input("Enter Base Sqft for Performance Space Architecture", min_value=0, value=10000)
base3 = st.number_input("Enter Base Sqft for Gallery Architecture", min_value=0, value=8500)

st.write("Adjust the sliders to calculate prices based on the base sqft values.")

# Sliders with specific ranges for each category
slider1_value = st.slider("Venue Build (in $)", min_value=150, max_value=250, value=200)
slider2_value = st.slider("Performance Space Architecture (in $)", min_value=100, max_value=150, value=125)
slider3_value = st.slider("Gallery Architecture (in $)", min_value=50, max_value=100, value=75)

# Calculate the subtotal for each category
subtotal1 = slider1_value * base1
subtotal2 = slider2_value * base2
subtotal3 = slider3_value * base3

# Display the subtotals
st.write(f"Subtotal for Venue Build: ${subtotal1}")
st.write(f"Subtotal for Performance Space Architecture: ${subtotal2}")
st.write(f"Subtotal for Gallery Architecture: ${subtotal3}")

# Calculate the total price
total = subtotal1 + subtotal2 + subtotal3

# Display the total price in a prominent colored box with rounded edges
st.markdown(
    f"""
    <div style="background-color:#f0f4c3;padding:20px;border-radius:10px;">
        <h2 style="color:#3f51b5;text-align:center;">Total Price: ${total}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Pie chart to show the percentage contribution of each category to the total
if total > 0:
    labels = ['Venue Build', 'Performance Space Architecture', 'Gallery Architecture']
    sizes = [subtotal1, subtotal2, subtotal3]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.write("### Contribution of Each Category to the Total Price")
    st.pyplot(fig)
else:
    st.write("Enter valid square footage and price multipliers to see the pie chart.")
