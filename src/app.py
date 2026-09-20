import streamlit as st
from calculate import calculate_footprint
from advisor import generate_advice

st.set_page_config(page_title="Carbon Footprint Estimator", page_icon="🌍")
st.title("Carbon Footprint Estimator")
st.caption("SDG 13 — Climate Action")

st.write("Answer a few questions about your daily habits to estimate your monthly carbon footprint.")

# --- Input form ---
commute_mode = st.selectbox(
    "How do you usually commute?",
    options=["car_petrol", "car_diesel", "two_wheeler", "bus", "auto_rickshaw", "walk_cycle"],
    format_func=lambda x: {
        "car_petrol": "Car (Petrol)",
        "car_diesel": "Car (Diesel)",
        "two_wheeler": "Two-wheeler",
        "bus": "Bus",
        "auto_rickshaw": "Auto-rickshaw",
        "walk_cycle": "Walk / Cycle",
    }[x],
)

commute_km = st.slider("Commute distance per day (km, one-way)", 0, 50, 10)

diet_type = st.selectbox(
    "Which best describes your diet?",
    options=["heavy_meat", "moderate_meat", "vegetarian", "vegan"],
    format_func=lambda x: {
        "heavy_meat": "Meat with most meals",
        "moderate_meat": "Meat a few times a week",
        "vegetarian": "Vegetarian",
        "vegan": "Vegan",
    }[x],
)

electricity_kwh = st.slider("Monthly household electricity usage (kWh)", 0, 1000, 250)

# --- Calculate button ---
if st.button("Calculate My Footprint"):
    footprint = calculate_footprint(commute_mode, commute_km, diet_type, electricity_kwh)

    st.subheader("Your Monthly Footprint")
    col1, col2, col3 = st.columns(3)
    col1.metric("Commute", f"{footprint['commute_kg']} kg")
    col2.metric("Diet", f"{footprint['diet_kg']} kg")
    col3.metric("Electricity", f"{footprint['electricity_kg']} kg")

    st.metric("Total CO2", f"{footprint['total_kg']} kg / month")

    with st.spinner("Generating personalized advice..."):
        advice = generate_advice(footprint)

    st.subheader("Personalized Advice")
    st.write(advice)

st.markdown("---")
st.caption(
    "Estimates are based on approximate emission factors and are for general awareness, "
    "not precise carbon accounting."
)