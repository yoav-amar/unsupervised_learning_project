import kagglehub
from pathlib import Path
import pandas as pd
from utils import calculate_bmi
import numpy as np


CSV_NAME = "athlete_events.csv"
# Download latest version
path = kagglehub.dataset_download("heesoo37/120-years-of-olympic-history-athletes-and-results", path=CSV_NAME)

print("Path to dataset files:", path)
real_path = Path(path)

real_path.rename(f"./{CSV_NAME}")
print(real_path)

df = pd.read_csv(CSV_NAME)

# Remove a specific column (e.g., "ColumnToRemove")
df.drop(columns=["NOC"], inplace=True)
df["BMI"] = df.apply(lambda row: calculate_bmi(row["Weight"], row["Height"]), axis=1)

# remove rows with empty height and empty wight
df = df[~np.isnan(df["Height"])]
df = df[~np.isnan(df["Weight"])]

df.to_csv("bla.csv", index=False)
