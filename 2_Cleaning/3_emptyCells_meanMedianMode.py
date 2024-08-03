import pandas as pd

old_df_mean = pd.read_csv("2_Cleaning\dirty_data.csv")
old_df_med = pd.read_csv("2_Cleaning\dirty_data.csv")
old_df_mode = pd.read_csv("2_Cleaning\dirty_data.csv")

#A common way to fill empty cells is using Mean, Median or Mode.

#Option I - Mean using mean()
x = old_df_mean["Calories"].mean()
old_df_mean.fillna({"Calories" : x}, inplace = True)
print(old_df_mean.to_string(), "\n")

#Option I - Median using median()
x = old_df_med["Calories"].median()
old_df_med.fillna({"Calories" : x}, inplace = True)
print(old_df_med.to_string(), "\n")

#Option I - Mode using mode()
x = old_df_mode["Calories"].mode()[0]
old_df_mode.fillna({"Calories" : x}, inplace = True)
print(old_df_mode.to_string())