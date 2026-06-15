#Clean data --> 
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

import pandas as pd 
import os 

df = pd.read_csv("data/raw/weather_raw.csv")
print("CSV before cleaning:", df.shape)

#Cleaning the temperature 
df["Temperature"] = (
    df["Temperature"].str.replace("°F", "", regex=False).str.replace("F", "", regex=False).str.strip()
)

df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

#Cleaning condition
df["Condition"] = df["Condition"].astype(str).str.strip()

#get rid of duplicates 
df.drop_duplicates(inplace=True)

#drop if missing city/temp
df.dropna(subset=["City", "Continent"], inplace=True)
print("CSV after cleaning:", df.shape)

#Save clean csv
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/weather_clean.csv", index=False)
print("Saved cleaned csv.")