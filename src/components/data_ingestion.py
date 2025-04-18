import sqlite3
import pandas as pd
import os
DB_PATH = os.getenv("DB_PATH")
class DataIngestion:
    def __init__(self, db_path:str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name

    def data_ingest(self) -> pd.DataFrame:
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"DB not found: {self.db_path}")
        with sqlite3.connect(self.db_path) as conn:
            raw_df = pd.read_sql(f"Select * from {self.table_name}",conn)
            return raw_df

