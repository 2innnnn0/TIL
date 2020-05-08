# 01.Loading & examining our data.py
# Import pandas 
import pandas as pd

# Load the customer_data
customer_data = pd.read_csv("customer_data.csv")

# Load the app_purchases
app_purchases = pd.read_csv("inapp_purchases.csv")

# Print the columns of customer data
print(customer_data.columns)

# Print the columns of app_purchases
print(app_purchases.columns)