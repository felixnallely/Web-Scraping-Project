import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

#Compare temp by Country 
df = pd.read_csv("data/clean/weather_clean.csv")

#Average temperature 
avg_temp = df.groupby("Country")["Temperature"].mean().reset_index()
#sort temp 
avg_temp  = avg_temp.sort_values(by="Temperature", ascending=False)

print("Average temperature by Country:")
print(avg_temp)

#Try--> compare 2 countries 
country1 = "Usa"
country2 = "Spain"

temp1 = avg_temp.loc[avg_temp["Country"] == country1, "Temperature"].values[0]
temp2 = avg_temp.loc[avg_temp["Country"] == country2, "Temperature"].values[0]

print(f"\nComparison between {country1} and {country2}:") 
if temp1 > temp2: 
    print(f"{country1} is warmer ({temp1:.1f}°F) than {country2} ({temp2:.1f}°F).")
elif temp1 < temp2: 
    print(f"{country2} is warmer ({temp2:.1f}°F) than {country1} ({temp1:.1f}°F).")
else: 
    print(f"Both have the same average temperature({temp1:.1f}°F).")