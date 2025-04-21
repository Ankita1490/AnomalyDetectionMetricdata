
import pandas as pd

class DataCleaning:
    def __init__(self):
        pass

    def clean(self, df):
        df = df.copy()
        df["memory_usage"] = df["memory_usage"].str.replace("GB", "").astype(float)
        df["network_in"] = df["network_in"].str.replace("GB", "").astype(float)
        df["network_out"] = df["network_out"].str.replace("GB", "").astype(float)
        df["disk_free_space"] = df["disk_free_space"].str.replace("GB", "").astype(float)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hour"] = df["timestamp"].dt.hour
        df["day_of_week"] = df["timestamp"].dt.dayofweek
        df.set_index("timestamp", inplace =True) # setting timestamp as index
        df["is_weekend"] =df["day_of_week"] >= 5
        df["is_weekend"] = df["is_weekend"].astype(int)

        df.dropna(inplace=True)
        return df