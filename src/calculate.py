# Emission factors (kg CO2 per unit)
# Sources: India-specific figures from CEA (Central Electricity Authority)
# grid emission factor, and commonly cited transport/diet averages.

ELECTRICITY_FACTOR = 0.82      # kg CO2 per kWh (India grid average)

COMMUTE_FACTORS = {             # kg CO2 per km
    "car_petrol": 0.192,
    "car_diesel": 0.171,
    "two_wheeler": 0.070,
    "bus": 0.089,
    "auto_rickshaw": 0.130,
    "walk_cycle": 0.0,
}

DIET_FACTORS = {                # kg CO2 per day, by diet type (rough averages)
    "heavy_meat": 7.2,
    "moderate_meat": 5.6,
    "vegetarian": 3.8,
    "vegan": 2.9,
}


def calculate_footprint(commute_mode, commute_km_per_day, diet_type, electricity_kwh_per_month):
    """
    Returns total estimated monthly CO2 footprint (kg), broken down by category.
    """
    # Commute: daily km -> monthly (assume ~22 working days)
    commute_monthly = COMMUTE_FACTORS[commute_mode] * commute_km_per_day * 22

    # Diet: daily factor -> monthly (30 days)
    diet_monthly = DIET_FACTORS[diet_type] * 30

    # Electricity: already monthly input
    electricity_monthly = ELECTRICITY_FACTOR * electricity_kwh_per_month

    total = commute_monthly + diet_monthly + electricity_monthly

    return {
        "commute_kg": round(commute_monthly, 2),
        "diet_kg": round(diet_monthly, 2),
        "electricity_kg": round(electricity_monthly, 2),
        "total_kg": round(total, 2),
    }


if __name__ == "__main__":
    # Test case: car commuter, moderate meat diet, average electricity use
    result = calculate_footprint(
        commute_mode="car_petrol",
        commute_km_per_day=15,
        diet_type="moderate_meat",
        electricity_kwh_per_month=250,
    )
    print(result)
    