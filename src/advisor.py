from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_advice(footprint_data):
    # Determine the highest-impact category in Python (reliable, not left to the model)
    categories = {
        "commute": footprint_data["commute_kg"],
        "diet": footprint_data["diet_kg"],
        "electricity": footprint_data["electricity_kg"],
    }
    highest_category = max(categories, key=categories.get)

    prompt = f"""A person's estimated monthly carbon footprint breakdown:
- Commute: {footprint_data['commute_kg']} kg CO2
- Diet: {footprint_data['diet_kg']} kg CO2
- Electricity: {footprint_data['electricity_kg']} kg CO2
- Total: {footprint_data['total_kg']} kg CO2

Their highest-impact category is: {highest_category}

Write a response with two parts:
1. A short (2-3 sentence) plain-language summary that correctly identifies {highest_category} as their biggest contributor.
2. Three specific, realistic reduction suggestions focused on {highest_category}, ordered by likely impact.

Keep the tone encouraging, not guilt-inducing. Avoid jargon. Keep the whole response under 150 words."""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
    )

    return response.choices[0].message.content