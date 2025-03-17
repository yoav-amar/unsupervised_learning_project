import kagglehub
from pathlib import Path
import pandas as pd
from utils import calculate_bmi, gender_to_number, long_event_to_short
import numpy as np
from gensim.models import word2vec


CSV_NAME = "athlete_events.csv"
# Download latest version
path = kagglehub.dataset_download("heesoo37/120-years-of-olympic-history-athletes-and-results", path=CSV_NAME)

print("Path to dataset files:", path)
real_path = Path(path)

real_path.rename(f"./{CSV_NAME}")
print(real_path)

df = pd.read_csv(CSV_NAME)

# Remove columns without information
df.drop(columns=["NOC"], inplace=True)
df.drop(columns=["Games"], inplace=True)
df.drop(columns=["Medal"], inplace=True)

# create bmi
df["BMI"] = df.apply(lambda row: calculate_bmi(row["Weight"], row["Height"]), axis=1)

# remove rows with empty height and empty wight
df = df[~np.isnan(df["Height"])]
df = df[~np.isnan(df["Weight"])]

# improve columns
df["Sex"] = df["Sex"].apply(gender_to_number)
df["Event"] = df.apply(lambda row: long_event_to_short(row["Sex"], row["Sport"], row["Event"]), axis=1)
df["Sport"] = df["Sport"].apply(gender_to_number)


df.to_csv("bla.csv", index=False)
