import pandas as pd

class DataCleaning:

    def clean_accident_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        df = df.drop_duplicates()

    # Convert numeric columns properly
        for col in df.columns:
            if any(x in col for x in ["2022", "2023"]):
                df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df.ffill()

        print("[INFO] Accident data cleaned (aggregated dataset detected)")
        return df
    
    def clean_traffic_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        df = df.drop_duplicates()

        # Convert time column if exists
        for col in df.columns:
            if "time" in col:
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        print("[INFO] Traffic data cleaned")
        return df
    
    def add_time_features(self, df: pd.DataFrame, time_column: str = None) -> pd.DataFrame:
    
        if time_column and time_column in df.columns:
            df[time_column] = pd.to_datetime(df[time_column], errors='coerce')

            df['hour'] = df[time_column].dt.hour
            df['day'] = df[time_column].dt.day
            df['month'] = df[time_column].dt.month
            df['day_of_week'] = df[time_column].dt.dayofweek

            df['is_rush_hour'] = df['hour'].apply(
                lambda x: 1 if pd.notnull(x) and (7 <= x <= 10 or 17 <= x <= 20) else 0
            )

            print("[INFO] Full time features added")

        else:
            print("[WARNING] No valid datetime column found. Creating limited features...")

            if 'year' in df.columns:
                df['year'] = df['year']

            if 'month' in df.columns:
                df['month'] = df['month']

        return df
    
    def create_location_key(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        df['location_key'] = df[columns].astype(str).agg('_'.join, axis=1)

        print("[INFO] Location key created")
        return df