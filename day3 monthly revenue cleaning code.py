import pandas as pd  
df = pd.read_csv("sales_data.csv")

# Overview of the Dataset
print(df.shape)
print(df.info())
print(df.head())

# Converting Sale_Date to datetime
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'], errors='coerce')

# Creating calculated columns
df['Profit'] = (df['Unit_Price'] - df['Unit_Cost']) * df['Quantity_Sold']
df['Revenue'] = df['Sales_Amount'] * (1 - df['Discount']/100)
df['Profit_Margin'] = (df['Profit'] / df['Revenue']) * 100

# Extracting time features
df['Year'] = df['Sale_Date'].dt.year
df['Month'] = df['Sale_Date'].dt.month_name()
df['Quarter'] = df['Sale_Date'].dt.to_period('Q')

# chacking for duplicates (if any)
print("Total duplicates:", df.duplicated().sum())

# Checking quick
print(df.info())
print(df.head())

# Saving cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)


