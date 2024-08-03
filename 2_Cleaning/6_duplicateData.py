import pandas as pd

df = pd.read_csv("2_Cleaning\dirty_data.csv")

# Duplicate rows may exist in any DataFrame, which can alter our analysis.
# To clean them, we first check if any duplicate rows exist using duplicated() method.

print(df.duplicated(), "\n")

# This returns a True/False value for each row in the DataFrame. Duplicate rows will return True.
# We can easily remove these duplicate rows using the drop_duplicated() method.

df.drop_duplicates(inplace = True)
print(df)