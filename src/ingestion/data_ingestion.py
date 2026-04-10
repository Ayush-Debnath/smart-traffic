import os
import pandas as pd

class DataIngestion:
    def __init__(self):
        self.base_path = "data/raw"

    def load_csv(self, folder: str, file_name: str) -> pd.DataFrame:
        path = os.path.join(self.base_path, folder, file_name)

        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found")

        df = pd.read_csv(path)
        print(f"[INFO] Loaded CSV: {file_name}, Shape: {df.shape}")
        return df

    def load_excel(self, folder: str, file_name: str) -> pd.DataFrame:
        path = os.path.join(self.base_path, folder, file_name)

        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found")

        df = pd.read_excel(path)
        print(f"[INFO] Loaded Excel: {file_name}, Shape: {df.shape}")
        return df

    def save_interim(self, df: pd.DataFrame, file_name: str):
        path = "data/interim"
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, file_name)
        df.to_csv(file_path, index=False)

        print(f"[INFO] Saved interim file: {file_path}")

    def save_processed(self, df: pd.DataFrame, file_name: str):
        path = "data/processed"
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, file_name)
        df.to_csv(file_path, index=False)

        print(f"[INFO] Saved processed file: {file_path}")