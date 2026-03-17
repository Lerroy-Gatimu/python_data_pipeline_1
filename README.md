# python_data_pipeline_1

A clean, modular, production-ready ETL pipeline using **Python + MySQL**.

## Features
- Full separation of concerns (Extract / Transform / Load)
- Environment-based configuration (`.env`)
- Comprehensive logging
- Data validation & type enforcement
- Batch loading for performance
- Ready for scheduling (cron, Airflow, etc.)

## Project Structure
python_data_pipeline_1/
├── data/raw/           ← input CSV files
├── logs/               ← pipeline.log
├── config/config.py
├── src/
|    |──__init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── .env
├── requirements.txt
└── README.md
text## Installation

1. Clone or create the project
2. `python -m venv venv`
3. Activate venv
4. `pip install -r requirements.txt`
5. Create `.env` (see `.env.example` if you make one)
6. Create MySQL database and table 

## Usage

bash:
python -m src.pipeline