import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Global Weather Dashboard", layout="wide")
st.title("Global Weather Dashboard")
st.write("Explore worldwide weather patterns.")

#Load data
conn = sqlite3.connect("db/weather.db")
df_weather = pd.read_sql_query("SELECT * FROM weather", conn)
df_avg = pd.read_sql_query("SELECT * FROM avg_temp", conn)
conn.close()

#st.write("Raw Data Preview")
#st.dataframe(df)

#Visualizations
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df_weather["Country"].unique(),
    default=df_weather["Country"].unique()
)

conditions = df_weather["Condition"].unique()
selected_conditions = st.sidebar.multiselect(
    "Select Weather Conditions",
    options=conditions,
    default=conditions
)

#Keep code from breaking when no filters are applied
if len(countries) == 0:
    countries = df_weather["Country"].unique()
if selected_conditions is None:
    selected_conditions = df_weather["Condition"].unique()

#Apply filters 
filtered = df_weather[
    (df_weather["Country"].isin(countries)) & 
    (df_weather["Condition"].isin(selected_conditions))
]


col1, col2, col3 = st.columns(3)
col1.metric("Highest Temperature", f"{filtered['Temperature'].max()}°F")
col2.metric("Lowest Temperature", f"{filtered['Temperature'].min()}°F")
col3.metric("Average Temperature", f"{filtered['Temperature'].mean():.1f}°F")


#Bar Chart (Showing temp by city)
fig1 = px.bar(
    filtered,
    x="City",
    y="Temperature",
    color="Country",
    title="Temperature by City"
)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    df_avg,
    x="Country",
    y="AveTemp",
    title="Average Temperature by Country"
)
st.plotly_chart(fig2, use_container_width=True)

#Histogram
fig3 = px.histogram(
    filtered,
    x="Temperature",
    nbins=20,
    title="Temperature Distribution"
)
st.plotly_chart(fig3, use_container_width=True)

st.write("""
### How to use this Dashboard
- Use sidebar filters to select a country or continent.
- Hover over charts to see more details.
- Compare temperature trends/conditions across different regions.
""")

st.write("rows after filtering:", len(filtered))