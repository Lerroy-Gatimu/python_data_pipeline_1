import pandas as pd
import logging
from datetime import datetime

def transform(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting transformation...")
    
    # 1. Copy to avoid modifying original
    df = df.copy()
    
    # 2. Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # 3. Data type enforcement
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    
    # 4. Derived column
    df["total_amount"] = df["quantity"] * df["unit_price"]
    
    # 5. Date conversion
    df["transaction_date"] = pd.to_datetime(df["transaction_date"]).dt.date
    
    # 6. Handle missing emails
    df["customer_email"] = df["customer_email"].fillna("no_email@domain.com")
    
    # 7. Validation
    if df["total_amount"].isnull().any():
        raise ValueError("Null values found in total_amount!")
    
    logging.info(f"Transformation complete. Final shape: {df.shape}")
    return df