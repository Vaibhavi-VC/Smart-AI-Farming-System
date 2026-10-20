import os
import joblib
import pandas as pd

# ------------------------------------------------------------------
# Resolve absolute project root path safely
# ------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "model", "arima_results_all_commodities.pkl")

# DEBUG (temporary – proves path correctness)
print("ARIMA PKL PATH:", MODEL_PATH)
print("FILE EXISTS:", os.path.exists(MODEL_PATH))


def load_results():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"ARIMA file not found at: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def get_all_commodities():
    data = load_results()

    if isinstance(data, pd.DataFrame):
        return data["Commodity"].unique().tolist()

    return list(data.keys())


def get_forecast_details(commodity):
    data = load_results()

    if isinstance(data, pd.DataFrame):
        row = data[data["Commodity"] == commodity]
        if row.empty:
            return None
        return row.iloc[0].to_dict()

    return data.get(commodity)
