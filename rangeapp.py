import streamlit as st
import matplotlib.pyplot as plt

# Add an image at the top of the app, resize it to fit the width of the app
st.image("chun.png", use_column_width=True)  # Replace "logo.png" with your actual image filename

# Set up the title of the app
st.title("OASYS ROM Calculator - Venue")

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

# Display the subtotals with commas for better readability
st.write(f"Subtotal for Venue Build: ${subtotal1:,.0f}")
st.write(f"Subtotal for Performance Space Architecture: ${subtotal2:,.0f}")
st.write(f"Subtotal for Gallery Architecture: ${subtotal3:,.0f}")

# Calculate the total price
total = subtotal1 + subtotal2 + subtotal3

# Display the total price in a box with the same gray color as input fields and black font
st.markdown(
    f"""
    <div style="background-color:#f1f1f1;padding:10px;border-radius:10px;width:100%;margin:auto;">
        <h3 style="color:black;text-align:center;">Total Price: ${total:,.0f}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Add extra space between Total Price and Pie Chart
st.write("")
st.write("")  # Adds two empty lines of space

# Pie chart to show the percentage contribution of each category to the total with grayscale color scheme
if total > 0:
    labels = ['Venue Build', 'Performance Space Architecture', 'Gallery Architecture']
    sizes = [subtotal1, subtotal2, subtotal3]
    # Grayscale color scheme
    colors = ['#d9d9d9', '#a6a6a6', '#595959']

    # Create a larger figure for mobile, separate percentages and labels for clarity
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjust the size as needed for mobile screens
    fig.patch.set_alpha(0)  # Set figure background to transparent
    ax.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90, 
        pctdistance=0.5,  # Bring percentages closer to the center
        labeldistance=1.1  # Move the label descriptions further out
    )
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.write("### Contribution of Each Category to the Total Price")
    st.pyplot(fig)
else:
    st.write("Enter valid square footage and price multipliers to see the pie chart.")
