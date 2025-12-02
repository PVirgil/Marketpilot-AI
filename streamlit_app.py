# streamlit_app.py

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from groq import Groq
import pdfplumber
import logging

# Setup
logging.basicConfig(level=logging.INFO)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# LLM Wrapper

def call_llm(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a market strategy and competitive intelligence expert."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# File Parsing

def extract_pdf_text(file) -> str:
    try:
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_csv_text(file) -> str:
    try:
        df = pd.read_csv(file)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error reading CSV: {e}"

# AI Modules

def generate_market_analysis(idea: str, market: str) -> str:
    prompt = (
        f"Product idea: {idea}\nTarget market: {market}\n"
        "Generate a market opportunity analysis including demand, trends, risks, and entry barriers."
    )
    return call_llm(prompt)

def compare_competitors(competitors: str) -> str:
    prompt = (
        f"Competitors: {competitors}\n"
        "Create a side-by-side comparison, highlighting features, pricing, positioning, and gaps."
    )
    return call_llm(prompt)

def generate_gtm_plan(idea: str, product_stage: str) -> str:
    prompt = (
        f"Product: {idea}\nStage: {product_stage}\n"
        "Develop a go-to-market strategy including positioning, channels, launch tactics, and KPIs."
    )
    return call_llm(prompt)

# Streamlit UI

def main():
    st.set_page_config("MarketPilot AI", page_icon="📊", layout="wide")
    st.title("📊 MarketPilot AI")
    st.write("AI-powered market strategy and go-to-market planning assistant.")

    idea = st.text_input("Describe your product or idea")
    market = st.text_input("Target Market or Industry")
    product_stage = st.selectbox("Product Stage", ["Idea", "Prototype", "Beta", "Launched"])
    competitors = st.text_area("Known Competitors (comma-separated)")
    uploaded_files = st.file_uploader("Optional: Upload strategy docs (PDF/CSV)", type=["pdf", "csv"], accept_multiple_files=True)

    file_texts = ""
    if uploaded_files:
        for file in uploaded_files:
            if file.name.endswith(".pdf"):
                file_texts += extract_pdf_text(file) + "\n"
            elif file.name.endswith(".csv"):
                file_texts += extract_csv_text(file) + "\n"
        st.success("Documents processed.")

    tab1, tab2, tab3 = st.tabs(["📈 Market Analysis", "🆚 Competitor Insight", "🚀 GTM Plan"])

    with tab1:
        st.subheader("📈 Market Opportunity Analysis")
        if st.button("Analyze Market"):
            if not idea or not market:
                st.error("Please enter both product idea and market.")
            else:
                output = generate_market_analysis(idea, market + "\n" + file_texts)
                st.text_area("Market Analysis", value=output, height=400)

    with tab2:
        st.subheader("🆚 Competitor Landscape")
        if st.button("Compare Competitors"):
            if not competitors:
                st.error("Please enter competitors.")
            else:
                output = compare_competitors(competitors + "\n" + file_texts)
                st.text_area("Competitive Intelligence", value=output, height=400)

    with tab3:
        st.subheader("🚀 Go-to-Market Strategy")
        if st.button("Generate GTM Plan"):
            if not idea:
                st.error("Please enter your product.")
            else:
                output = generate_gtm_plan(idea, product_stage + "\n" + file_texts)
                st.text_area("GTM Plan", value=output, height=400)

if __name__ == "__main__":
    main()
