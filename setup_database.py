import pandas as pd
import sqlite3

# Read CSV files (flat structure, no "data/" folder)
providers = pd.read_csv("providers_data.csv")
receivers = pd.read_csv("receivers_data.csv")
food_listings = pd.read_csv("food_listings_data.csv")
claims = pd.read_csv("claims_data.csv")

# Create SQLite DB and connection
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

# Save data to tables
providers.to_sql("providers", conn, if_exists="replace", index=False)
receivers.to_sql("receivers", conn, if_exists="replace", index=False)
food_listings.to_sql("food_listings", conn, if_exists="replace", index=False)
claims.to_sql("claims", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("Database setup complete!")