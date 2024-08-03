import pandas as pd

df = pd.read_csv("2_Cleaning\dirty_data.csv")

# Incorrect formats can prevent us from analysing data altogether. To prevent this, we change the formats manually.
# The Date column has a couple of rows which don't match the format of the column.
# We fix it using the to_datetime() method.

df['Date'] = pd.to_datetime(df['Date'], errors="coerce") # Any row that can't switch to datetime format will become NAT
print(df.to_string(), "\n")

# Now, we can remove the rows with NULL values, i.e, NaT
df.dropna(subset = ["Date"], inplace = True) #subset attribute selects only specific columns
print(df.to_string())