#time: <td id="p0" class="r">
#temperature tag: <td class="rbi">
#weather condition tag: <img> title attribute
#scroll: <div class="tb-scroll"> 

import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 


map_continent = {
    "France": "Europe",
    "Egypt": "Africa",
    "Japan": "Asia",
    "Brazil": "South America",
    "Usa": "North America",
    "Guatemala": "Central America",
    "Australia": "Oceania",
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.timeanddate.com/weather/")
time.sleep(5)

rows = driver.find_elements(By.CSS_SELECTOR, "table.zebra.fw.tb-theme tbody tr")

all_weather_data = []

for row in rows: 
    try:
        city = row.find_element(By.CSS_SELECTOR, "td a").text
        condition = row.find_element(By.CSS_SELECTOR, "td img").get_attribute("alt")
        temp = row.find_element(By.CSS_SELECTOR, "td.rbi").text
        time = row.find_element(By.CSS_SELECTOR, "td.r").text

        href = row.find_element(By.CSS_SELECTOR, "td a").get_attribute("href")
        country_raw = href.split("/")[4]
        country = country_raw.replace("-", " ").title()

        continent = map_continent.get(country, "Unknown")

        all_weather_data.append({
            "City": city, 
            "Country": country, 
            "Continent": continent,
            "Temperature": temp,
            "Condition": condition
        })
    except Exception: 
        continue

driver.quit()

#Save to csv as raw data
data = pd.DataFrame(all_weather_data)
data.to_csv("data/raw/weather_raw.csv", index=False)

print("Scraping complete.")