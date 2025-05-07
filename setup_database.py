
import sqlite3
import pandas as pd

conn = sqlite3.connect("food.db")

providers = pd.read_csv("data/providers_data.csv")
receivers = pd.read_csv("data/receivers_data.csv")
food = pd.read_csv("data/food_listings_data.csv")
claims = pd.read_csv("data/claims_data.csv")

providers.to_sql("providers", conn, if_exists="replace", index=False)
receivers.to_sql("receivers", conn, if_exists="replace", index=False)
food.to_sql("food_listings", conn, if_exists="replace", index=False)
claims.to_sql("claims", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Database setup completed.")
