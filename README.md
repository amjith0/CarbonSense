# CarbonSense

**AI-Powered Personal Carbon Footprint Estimator**

Built for the 1M1B AI for Sustainability Virtual Internship (IBM SkillsBuild & AICTE) — SDG 13: Climate Action.

## Problem

Most people have no accessible way to understand the environmental impact of their daily choices. Commuting, diet, and electricity use all contribute to a personal carbon footprint, but the numbers stay abstract until measured. CarbonSense closes that gap by turning a few lifestyle questions into a personalized, actionable breakdown.

## How It Works

1. **User Input** — commute mode/distance, diet type, monthly electricity usage
2. **Calculate** — fixed, India-relevant emission-factor formulas (pure Python, deterministic)
3. **AI Advisor** — the highest-impact category is identified in code, then passed to a Groq-hosted LLM, which generates a personalized, plain-language summary and three prioritized reduction suggestions
4. **Display** — results shown in a Streamlit interface

**Why AI, not just a formula?** The arithmetic is handled entirely by code — fast, transparent, and accurate. AI's role is interpretation: turning raw numbers into a tailored explanation a static lookup table can't produce.

## Tech Stack

- Python (emission-factor calculation logic)
- Groq API (LLM inference — `openai/gpt-oss-20b`)
- Streamlit (interface)

## Target Users

General public and students seeking a simple way to understand their environmental impact, and anyone already motivated to reduce their footprint but lacking specific, prioritized guidance.

## Responsible AI Considerations

- **Fairness** — commute/diet options reflect Indian context (two-wheeler, auto-rickshaw, local diets), not Western-centric defaults
- **Transparency** — raw emission numbers are always shown alongside the AI-generated advice, never hidden behind a black-box score
- **Ethics** — advice is explicitly generated in an encouraging, non-judgmental tone
- **Privacy** — no data is stored, logged, or tied to an account; every calculation is per-session only

## Setup

```bash
git clone https://github.com/amjith0/CarbonSense.git
cd CarbonSense
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:
