from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Database
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    
    # Paths
    RAW_DATA_PATH = "data/raw/sales_data.csv"
    LOG_FILE = "logs/pipeline.log"
    
    # Pipeline settings
    BATCH_SIZE = 1000
    IF_EXISTS = "append"   # "replace" or "append"