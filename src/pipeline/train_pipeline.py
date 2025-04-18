from components.data_ingestion import DataIngestion
from components.data_cleaning import DataCleaning
import os
from dotenv import load_dotenv
load_dotenv()

DB_PATH = os.getenv("DB_PATH")
print(DB_PATH)
class TrainPipeline:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
    
    def run(self):
        # Ingest
        ingestion = DataIngestion(self.db_path, self.table_name)
        raw_data = ingestion.data_ingest()
        print(raw_data.dtypes)

        # cleaning
        cleaner = DataCleaning()
        df_cleaned = cleaner.clean(raw_data)

        return df_cleaned
    
if  __name__ == "__main__":
    pipeline = TrainPipeline(db_path=DB_PATH, table_name="metric_data")
    clean_df = pipeline.run()
    print(clean_df.head())
