import pandas as pd

df1 = pd.read_csv("2_Cleaning\dirty_data.csv")
df2 = pd.read_csv("2_Cleaning\dirty_data.csv")
dfr = pd.read_csv("2_Cleaning\dirty_data.csv")

# A DataFrame may sometimes contain data that is itself incorrect, despite being non-null with the right data-type
# To fix this issue, we can either delete the entire row or replace the data.

# OPTION I - Replacing the data

# Sometimes, we can get an idea whether a spelling mistake or typo was made in the data.
# In that case, we can replace the incorrect data with what it was supposed to be.

# For small data sets, we can simply use the label and column to specify the row which has to be cleaned using loc[row,col].
df1.loc[7, "Duration"] = 45
print(df1.to_string(),"\n")

# For larger data sets, we can simply create some bounds and replace values exceeding them.
for x in df2.index:
    if df2.loc[x, "Duration"] > 120:
        df2.loc[x, "Duration"] = 120
print(df2.to_string(), "\n")

# OPTION II - Removing the rows containing incorrect data
# Using a similar ruleset, we can use the drop() method to drop any rows that contain data exceeding our given bounds

for x in dfr.index:
    if dfr.loc[x, "Duration"] > 120:
        dfr.drop(x, inplace = True)
print(dfr.to_string())