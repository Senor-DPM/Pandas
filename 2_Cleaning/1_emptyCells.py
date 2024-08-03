import pandas as pd

old_df = pd.read_csv("2_Cleaning\dirty_data.csv")

# We must make sure to clean any and all empty cells, as they can alter our results during analysis.
# There are two ways to clean these empty cells :

# Option 1 : Delete rows containing empty cells using dropna() method : 
new_df = old_df.dropna() # Creates a new DataFrame
print(new_df.to_string(),"\n")

# if you want to delete empty cells in the original DataFrame, set the inplace attribute to True
old_df_2 = pd.read_csv("2_Cleaning\dirty_data.csv")
old_df_2.dropna(inplace=True)
print(old_df_2.to_string())