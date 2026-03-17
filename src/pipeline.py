import logging
from datetime import datetime
from src.extract import extract
from src.transform import transform
from src.load import load

def setup_logging():
    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger("").addHandler(console)

def run_pipeline():
    start_time = datetime.now()
    setup_logging()
    
    logging.info("="*50)
    logging.info("STARTING PYTHON DATA PIPELINE 1")
    logging.info("="*50)
    
    try:
        # Extract
        df_raw = extract()
        
        # Transform
        df_clean = transform(df_raw)
        
        # Load
        load(df_clean)
        
        duration = datetime.now() - start_time
        logging.info(f"✅ PIPELINE COMPLETED SUCCESSFULLY in {duration}")
        
    except Exception as e:
        logging.error(f"❌ PIPELINE FAILED: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()