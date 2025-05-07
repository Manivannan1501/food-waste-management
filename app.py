
import streamlit as st
import sqlite3
import pandas as pd
import os

if not os.path.exists("food.db"):
    import setup_database

conn = sqlite3.connect("food.db")

st.title("🍲 Local Food Wastage Management System")

# Sidebar Filters
st.sidebar.header("Filter Listings")
city = st.sidebar.text_input("City")
provider_type = st.sidebar.selectbox("Provider Type", ["All", "Restaurant", "Grocery Store", "Supermarket"])
meal_type = st.sidebar.selectbox("Meal Type", ["All", "Breakfast", "Lunch", "Dinner", "Snacks"])

query = "SELECT * FROM food_listings WHERE 1=1"
if city:
    query += f" AND Location LIKE '%{city}%'"
if provider_type != "All":
    query += f" AND Provider_Type = '{provider_type}'"
if meal_type != "All":
    query += f" AND Meal_Type = '{meal_type}'"

df = pd.read_sql_query(query, conn)
st.subheader("Available Food Listings")
st.dataframe(df)

st.subheader("📊 Data Insights")

st.write("**1. Providers per City**")
query1 = "SELECT City, COUNT(*) as Provider_Count FROM providers GROUP BY City"
st.dataframe(pd.read_sql_query(query1, conn))

st.write("**2. Provider Type with Most Contributions**")
query2 = "SELECT Type, COUNT(*) as Count FROM providers GROUP BY Type"
st.dataframe(pd.read_sql_query(query2, conn))

st.write("**3. Most Claimed Food Types**")
query3 = "SELECT Food_Type, COUNT(*) AS Total_Claims FROM claims JOIN food_listings ON claims.Food_ID = food_listings.Food_ID GROUP BY Food_Type ORDER BY Total_Claims DESC"
st.dataframe(pd.read_sql_query(query3, conn))

st.write("**4. Most Active Receivers**")
query4 = "SELECT receivers.Name, COUNT(*) AS Claims FROM claims JOIN receivers ON claims.Receiver_ID = receivers.Receiver_ID GROUP BY claims.Receiver_ID ORDER BY Claims DESC"
st.dataframe(pd.read_sql_query(query4, conn))

st.write("**5. Listings per Provider**")
query5 = "SELECT providers.Name, COUNT(*) AS Listings FROM food_listings JOIN providers ON food_listings.Provider_ID = providers.Provider_ID GROUP BY food_listings.Provider_ID"
st.dataframe(pd.read_sql_query(query5, conn))

st.write("**6. Unclaimed Food Listings**")
query6 = "SELECT * FROM food_listings WHERE Food_ID NOT IN (SELECT Food_ID FROM claims)"
st.dataframe(pd.read_sql_query(query6, conn))

st.write("**7. Food Quantity Summary by Type**")
query7 = "SELECT Food_Type, SUM(Quantity) AS Total_Quantity FROM food_listings GROUP BY Food_Type"
st.dataframe(pd.read_sql_query(query7, conn))

st.write("**8. Receiver Requests by City**")
query8 = "SELECT City, COUNT(*) AS Total_Receivers FROM receivers GROUP BY City"
st.dataframe(pd.read_sql_query(query8, conn))

st.write("**9. Provider Contribution Summary**")
query9 = "SELECT Provider_ID, COUNT(*) AS Listings_Contributed FROM food_listings GROUP BY Provider_ID"
st.dataframe(pd.read_sql_query(query9, conn))

st.write("**10. Most Common Meal Type**")
query10 = "SELECT Meal_Type, COUNT(*) AS Count FROM food_listings GROUP BY Meal_Type ORDER BY Count DESC"
st.dataframe(pd.read_sql_query(query10, conn))

conn.close()
