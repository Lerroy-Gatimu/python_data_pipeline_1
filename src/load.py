from sqlalchemy import create_engine
import pandas as pd
import logging
from config.config import Config

def load(df: pd.DataFrame) -> None:
    logging.info("Starting load to MySQL...")
    
    connection_string = (
        f"mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@"
        f"{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    )
    
    engine = create_engine(connection_string, pool_pre_ping=True)
    
    try:
        df.to_sql(
            name="sales",
            con=engine,
            if_exists=Config.IF_EXISTS,
            index=False,
            chunksize=Config.BATCH_SIZE
        )
        logging.info(f"Successfully loaded {len(df)} rows into MySQL table 'sales'")
    except Exception as e:
        logging.error(f"Load failed: {e}")
        raise
    finally:
        engine.dispose()