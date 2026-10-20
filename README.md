# 🌾 Agrios – AI-Based Smart Farming System

Agrios is a multi-module AI platform that gives farmers three kinds of advice in one place: what is wrong with their crop, what to grow, and when to sell. A bilingual (English/Hindi), voice-enabled assistant powered by the Gemini API lets farmers ask questions in plain language and routes them to the right module.

## Features

| Module | What it does | Model | Result |
|---|---|---|---|
| **Crop Disease Detection** | Identifies plant diseases from a leaf image | EfficientNetB0 (transfer learning) | 95% accuracy across 29 classes |
| **Crop Recommendation** | Suggests the best crop for given soil and climate conditions | Random Forest | 98.3% accuracy |
| **Market Price Forecasting** | Forecasts crop prices from historical mandi (market) data | LSTM | [add your metric, e.g. RMSE/MAPE] |
| **Conversational Assistant** | Answers farmer queries in English and Hindi, by text or voice, and routes them to the right module | Gemini API | n/a |

## How It Works

```
Farmer (text / voice, English or Hindi)
              │
              ▼
   Gemini-powered assistant
   (understands the query, picks a module)
              │
     ┌────────┼────────────────┐
     ▼        ▼                ▼
  Disease   Crop            Price
 detection  recommendation  forecasting
 (CNN)      (Random Forest) (LSTM)
     │        │                │
     └────────┴────────┬───────┘
                       ▼
          Flask app returns the result
```

## Tech Stack

- **Language:** Python
- **ML / Deep Learning:** TensorFlow/Keras [confirm], Scikit-learn, Pandas, NumPy
- **Backend:** Flask, REST APIs
- **LLM:** Gemini API
- **Frontend:** [HTML/CSS/JS, or whatever you used]
- **Cloud (if used):** [e.g. AWS EC2 / S3]

## Project Structure

> Replace this with your real folder layout.

```
agrios/
├── app.py                  # Flask entry point
├── models/                 # Trained model files
├── notebooks/              # Training notebooks
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── requirements.txt
└── README.md
```

## Getting Started

> Adjust the commands to match your repo.

```bash
# 1. Clone the repository
git clone https://github.com/Vaibhavi-VC/[repo-name].git
cd [repo-name]

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key
export GEMINI_API_KEY="your-key-here"    # Windows: set GEMINI_API_KEY=your-key-here

# 5. Run the app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Datasets

- **Crop disease images:** [source, e.g. PlantVillage], 29 classes
- **Crop recommendation:** [source], soil and climate features
- **Mandi prices:** [source, e.g. Agmarknet / data.gov.in], historical price series

## Screenshots
<img width="865" height="445" alt="image" src="https://github.com/user-attachments/assets/7a8742be-a69c-433d-a09e-7723090325a8" />
<img width="935" height="751" alt="Screenshot 2026-03-31 010527" src="https://github.com/user-attachments/assets/64869bc1-183e-463a-a0ff-d2344dc58641" />


## Challenges and Learnings

- **Integrating three ML systems into one Flask workflow** meant handling different input formats and keeping the experience simple for non-technical users.
- **Getting the LSTM forecaster to display correctly.** It initially returned incorrect values and empty charts. [Add what the cause was and how you fixed it.]
- **Designing for low-resource users** pushed me to support Hindi and voice input, so the product is usable beyond English-speaking, text-first users.

## Future Improvements

> Keep only the ones you would genuinely build.

- Add more crops and regional price data
- Support more regional languages
- Deploy as a mobile-friendly web app

## Author

**Vaibhavi Chauhan**
B.Tech Computer Science Engineering, VIT Bhopal
[GitHub](https://github.com/Vaibhavi-VC) · [LinkedIn](https://www.linkedin.com/in/vaibhavi-chauhan-721980293) · vaibhavic08@gmail.com
