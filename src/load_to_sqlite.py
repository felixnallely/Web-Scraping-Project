import pandas as pd 
import sqlite3
import os 

DB_PATH = "db/weather.db"
clean_path = "data/clean/weather_clean.csv"

os.makedirs("db", exist_ok=True)

#Load cleaned csv 
df = pd.read_csv(clean_path)
print("Clean data:", df.shape)

#connect to SQlite
conn = sqlite3.connect(DB_PATH)

#Table
df. to_sql("weather", conn, if_exists="replace", index=False)
conn.close()
print("Data successfully saved at db/weather.db")

#Transformation 
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS avg_temp AS 
    SELECT Country, AVG(Temperature) AS AveTemp
    FROM weather 
    GROUP BY Country
""")

conn.commit()
conn.close()