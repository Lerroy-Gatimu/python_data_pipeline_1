import pandas as pd
import logging
from config.config import Config

def extract() -> pd.DataFrame:
    logging.info("Starting extraction from CSV...")
    try:
        df = pd.read_csv(Config.RAW_DATA_PATH)
        logging.info(f"Extracted {len(df)} rows from {Config.RAW_DATA_PATH}")
        return df
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise