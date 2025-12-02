# 📊 MarketPilot AI

**MarketPilot AI** is your AI-powered market research and go-to-market strategy assistant. Built with Streamlit and powered by Groq’s lightning-fast LLMs, it helps startups and teams analyze markets, assess competitors, and generate actionable GTM plans instantly.

---

## 🚀 Live App
[Launch MarketPilot AI](https://your-streamlit-app-link.com)

---

## 🧠 Key Features

- **📈 Market Analysis**: Evaluate market opportunities, trends, and risks.
- **🆚 Competitor Comparison**: Analyze rivals’ positioning, pricing, and gaps.
- **🚀 GTM Strategy Generator**: Create tailored launch strategies with KPIs.
- **📁 PDF/CSV Uploads**: Ingest internal docs for richer AI responses.
- **📤 Pitch-Ready Output**: Instantly usable for teams, advisors, or investors.

---

## 📂 Project Structure

```
marketpilot-ai/
├── streamlit_app.py
├── requirements.txt
├── .env               # (for local use)
└── README.md
```

---

## 🔧 Local Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/marketpilot-ai.git
cd marketpilot-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set your Groq API key**
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the app**
```bash
streamlit run streamlit_app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Set your `GROQ_API_KEY` in **Secrets**
4. Deploy and share your custom app URL

```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## 🛡 License

**MIT** — free to use, adapt, and commercialize with attribution.

---

> MarketPilot AI was built for founders, product teams, and consultants who need strategy-level insights — fast.
