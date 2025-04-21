import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def load_data_to_postgres():
    # Load environment variables
    load_dotenv()

    # Paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.dirname(os.path.dirname(current_dir)) + "/data/processed/processed_earthquake_data.csv"
    df = pd.read_csv(csv_file)
    print(df.head())

    # Get database credentials from environment
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    table_name = "earthquakes"

    try:
        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"✅ Loaded {len(df)} rows to table '{table_name}' in '{db_name}' database.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_data_to_postgres()
